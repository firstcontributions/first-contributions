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
  ( cd "$DL_DIR" && python3 "$ROOT/yangdon/src/aihub.py" download "$key" "${LABELS[$key]}" ) \
    || { echo "[$key] 다운로드 실패 — 활용신청 승인 여부를 확인하세요." >&2; continue; }
done

echo
echo "=========================================="
echo "라벨 구조 점검"
echo "=========================================="
find "$DL_DIR" -name '*.zip' -print 2>/dev/null | while read -r z; do
  echo "압축 해제: $z"
  unzip -o -q "$z" -d "${z%.zip}" || echo "  (unzip 실패: $z)"
done

echo "--- JSON 파일 개수 ---"
json_count=$(find "$DL_DIR" -name '*.json' | wc -l)
echo "$json_count 개"
if [ "$json_count" -gt 0 ]; then
  sample=$(find "$DL_DIR" -name '*.json' | head -1)
  echo "--- 샘플 JSON ($sample) 앞부분 ---"
  head -c 1200 "$sample"; echo
fi

echo
echo "다음 단계: 위 JSON 스키마에 맞춰 파서를 작성해 data/train.csv 생성 후"
echo "  python yangdon/src/eda.py && python yangdon/src/train.py"
