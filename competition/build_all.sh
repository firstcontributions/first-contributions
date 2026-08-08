#!/bin/bash
# 통합 대시보드 전체 생성 — 6개 뷰 + 리포트 + 허브(index.html).
# 데이터/영상이 있어야 하는 뷰는 없으면 건너뜀. 마지막에 허브가 링크를 잡는다.
#
# 사용: bash competition/build_all.sh
#   (선택) 71471 프레임 CSV: AIHUB_71471=<csv> bash competition/build_all.sh
set -u
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"
SRC=competition/src
run(){ echo "── $*"; python3 "$@" || echo "  (건너뜀: 데이터/영상 필요)"; }

# 분석 리포트
run $SRC/build_reference_report.py ${AIHUB_71471:-}
run $SRC/build_analysis_report.py
run $SRC/build_edinburgh_dashboard.py competition/data/edinburgh_frames.csv
run $SRC/build_activity_analysis.py
run $SRC/build_eval_report.py
run $SRC/build_repro_dashboard.py
run $SRC/build_alert_console.py
# 탐색 뷰
run $SRC/build_detection_viewer.py
run $SRC/build_posture_gallery.py
# 행동 갤러리(영상 필요: 000009)
VID=$(ls /tmp/edvid/color.mp4 /tmp/edin_vids/2019_11_05_000009/color.mp4 2>/dev/null | head -1)
[ -n "$VID" ] && run $SRC/build_behavior_gallery.py competition/data/edinburgh/2019_11_05/000009 "$VID"
# 통합 허브(마지막)
VID2=$(ls /tmp/edvid/color.mp4 /tmp/edin_vids/2019_11_05_000009/color.mp4 2>/dev/null | head -1)
[ -n "$VID2" ] && run $SRC/build_estrus_timeline.py competition/data/edinburgh/2019_11_05/000009 "$VID2"
run $SRC/build_dashboard_hub.py
echo "완료 → competition/dashboard/index.html 를 브라우저로 여세요."
