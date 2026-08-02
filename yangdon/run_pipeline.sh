#!/bin/bash
# 양돈 AI 원커맨드 파이프라인.
#   1) AI Hub 라벨링데이터 다운로드(확정 3종)
#   2) 압축 해제
#   3) 라벨 JSON 구조 점검(파일 목록 + 샘플 1건)
#   4) (스키마 확인 후) JSON→data/train.csv 가공은 별도 파서에서 수행
#      이어서 EDA/모델 학습은 eda.py / train.py 로.
#
# 사용: AIHUB_APIKEY 등록된 세션에서  bash yangdon/run_pipeline.sh
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"
DL_DIR="yangdon/data/aihub"
mkdir -p "$DL_DIR"

if [ -z "${AIHUB_APIKEY:-}" ]; then
  echo "AIHUB_APIKEY 가 없습니다. 환경 시크릿에 등록 후 새 세션에서 실행하세요." >&2
  exit 1
fi

# 확정 3종 라벨 filekey (docs/AIHUB.md 치트시트 기준)
declare -A LABELS=(
  [71763]="528771,528774"                                   # 양돈 생체 에너지(2023)
  [622]="533707,533708,533709,533717,533718,533719"         # 스마트축사(양돈)
  # 71471: 양돈(돼지+흑돼지) 핵심 라벨 bbox+keypoints+polygon
  [71471]="511410,511411,511412,511416,511417,511418,511458,511459,511460,511464,511465,511466"
)

for key in 71763 622 71471; do
  echo "=========================================="
  echo "다운로드: datasetkey=$key filekey=${LABELS[$key]}"
  echo "=========================================="
  mkdir -p "$DL_DIR/$key"
  ( cd "$DL_DIR/$key" && python3 "$ROOT/yangdon/src/aihub.py" download "$key" "${LABELS[$key]}" ) \
    || { echo "[$key] 다운로드 실패 — 활용신청 승인 여부를 확인하세요." >&2; continue; }
done

echo
echo "=========================================="
echo "압축 해제"
echo "=========================================="
find "$DL_DIR" -name '*.zip' -print 2>/dev/null | while read -r z; do
  echo "해제: $z"
  unzip -o -q "$z" -d "${z%.zip}" || echo "  (unzip 실패: $z)"
done

echo
echo "=========================================="
echo "파싱: 라벨 → CSV (스키마 기반)"
echo "=========================================="
for key in 71763 622 71471; do
  [ -d "$DL_DIR/$key" ] || continue
  python3 "$ROOT/yangdon/src/parse_aihub.py" "$key" "$DL_DIR/$key" \
    "yangdon/data/${key}_parsed.csv" || echo "  [$key] 파싱 건너뜀"
done

echo
echo "=========================================="
echo "모델링: 71763 생체에너지 회귀"
echo "=========================================="
if [ -d "$DL_DIR/71763" ]; then
  python3 "$ROOT/yangdon/src/model_71763.py" "$DL_DIR/71763" || true
fi

echo
echo "완료. 결과: yangdon/data/*_parsed.csv, yangdon/outputs/importance_*.csv"
echo "622(XML)·71471(발정) 모델링은 스키마 확인 후 model 스크립트 확장 예정."
