#!/bin/bash
# 양돈 AI 프로젝트 SessionStart 훅.
# 새 세션마다 파이썬 의존성을 설치하고, AI Hub 키/데이터 상태를 점검해
# 곧바로 분석·모델링을 이어갈 수 있게 준비한다.
set -euo pipefail

# 원격(Claude Code on the web) 세션에서만 실행.
if [ "${CLAUDE_CODE_REMOTE:-}" != "true" ]; then
  exit 0
fi

ROOT="${CLAUDE_PROJECT_DIR:-.}"
REQ="$ROOT/competition/requirements.txt"

echo "[session-start] 양돈 AI 프로젝트 준비 중..."

# 1) 파이썬 의존성 설치 (idempotent: 이미 있으면 빠르게 통과)
if [ -f "$REQ" ]; then
  python3 -m pip install --quiet --disable-pip-version-check \
    --root-user-action=ignore -r "$REQ" || {
    echo "[session-start] 의존성 설치 실패" >&2
    exit 1
  }
  echo "[session-start] 의존성 설치 완료 ($REQ)"
fi

# 2) AI Hub API 키 상태 점검 (값은 절대 출력하지 않음)
if [ -n "${AIHUB_APIKEY:-}" ]; then
  echo "[session-start] AIHUB_APIKEY 감지됨 → 라벨 다운로드 가능"
  echo "[session-start] 다음: python $ROOT/competition/run_pipeline.sh 로 다운로드→EDA→학습"
else
  echo "[session-start] AIHUB_APIKEY 없음 → 환경 시크릿 등록 후 새 세션에서 진행"
  echo "[session-start] (키 없이도 python competition/src/aihub.py search 양돈 등 조회는 가능)"
fi

echo "[session-start] 준비 완료."
