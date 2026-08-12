"""622 폴리곤 학습 세트 받기 — 국내망에서 한 번에.

    export AIHUB_APIKEY="발급받은_키"        # 절대 커밋하지 않는다
    python competition/src/fetch_622.py            # 라벨만 (85MB)
    python competition/src/fetch_622.py --images   # 라벨 + TS06 (10GB)

**라벨만 받으면 학습을 못 한다.** TL01(77MB)에는 폴리곤 좌표만 있고 이미지가
없다. 폴리곤 원천은 TS01~05 가 80~89GB 씩인데 TS06 만 10GB 라, 라벨 전체 +
TS06 하나가 현실적인 진입점이다.

## 왜 이 스크립트가 따로 있나

브라우저나 구버전 도구로 받으면 39바이트짜리 `페이지가 존재하지 않습니다.` 가
떨어진다. 실측으로 원인을 특정했다:

    /down/0.6/622.do?fileSn=533708   502  인증실패, 권한이 거부되었습니다  ← 정상
    /down/622.do?fileSn=533708       404  페이지가 존재하지 않습니다.      ← 39바이트

**버전 세그먼트 `/0.6/` 이 빠진 것**이 원인이었고, filekey 는 멀쩡했다. 이
스크립트는 v0.6 aihubshell 을 경유하므로 그 실수가 구조적으로 안 난다. 받은
뒤에는 tools/check_download.py 로 자동 검증한다 — 0바이트·에러문구·잘림을
그 자리에서 잡는다.
"""
from __future__ import annotations

import argparse
import os
import shutil
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, HERE)

DATASET = "622"
# tree 622 실측(2026-08). 갱신되면 `aihub.py tree 622` 로 다시 확인할 것.
FILES = {
    "labels": [
        ("533708", "Training 폴리곤 라벨 TL01.zip", 77),
        ("533718", "Validation 폴리곤 라벨 VL01.zip", 8),
    ],
    "images": [
        ("533695", "Training 폴리곤 원천 TS06.zip (가장 작은 것)", 10_240),
    ],
}
# 원천 zip 을 풀면 대략 압축 크기만큼 더 쓴다. 10GB zip → 여유 25GB 는 봐야 한다.
DISK_FACTOR = 2.5


def free_gb(path: str) -> float:
    return shutil.disk_usage(path).free / 1024 ** 3


def run(datasetkey: str, filekeys: str, out_dir: str) -> int:
    """v0.6 aihubshell 경유 — URL 을 직접 만들지 않는다."""
    import aihub
    os.makedirs(out_dir, exist_ok=True)
    cwd = os.getcwd()
    try:
        os.chdir(out_dir)          # aihubshell 은 현재 디렉터리에 받는다
        return aihub.download(datasetkey, filekeys)
    finally:
        os.chdir(cwd)


def verify(out_dir: str) -> int:
    import check_download
    sys.path.insert(0, os.path.join(ROOT, "competition", "tools"))
    return check_download.main(["check_download", out_dir])


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(prog="fetch_622")
    ap.add_argument("--images", action="store_true",
                    help="원천 TS06(10GB)도 받는다. 없으면 학습 불가")
    ap.add_argument("--out", default=os.path.join(ROOT, "competition", "data",
                                                  "aihub622"))
    ap.add_argument("--dry-run", action="store_true",
                    help="받지 않고 계획만 출력")
    a = ap.parse_args(argv)

    plan = list(FILES["labels"]) + (list(FILES["images"]) if a.images else [])
    total_mb = sum(mb for _k, _d, mb in plan)
    print("=" * 72)
    print(f"  AI Hub {DATASET} 폴리곤 — 받을 파일 {len(plan)}개")
    print("=" * 72)
    for k, desc, mb in plan:
        size = f"{mb / 1024:.1f} GB" if mb >= 1024 else f"{mb} MB"
        print(f"  {k}  {desc:<45} {size:>9}")
    print(f"  합계 {total_mb / 1024:.1f} GB  →  {a.out}")

    if not a.images:
        print("\n  ⚠️  라벨만 받는다. **이것만으로는 학습할 수 없다** —")
        print("     폴리곤 좌표만 있고 이미지가 없다. 학습하려면 --images 를 붙여")
        print("     TS06(10GB)까지 받을 것. 라벨 먼저 받아 내용을 확인하고 싶다면")
        print("     지금 그대로 진행해도 된다.")

    os.makedirs(a.out, exist_ok=True)
    need = total_mb / 1024 * DISK_FACTOR
    have = free_gb(a.out)
    print(f"\n  디스크 여유 {have:.1f} GB · 필요 약 {need:.1f} GB "
          f"(압축 해제분 포함)")
    if have < need:
        print(f"  ❌ 공간이 부족하다. {need - have:.1f} GB 를 더 확보할 것.")
        return 1

    if not os.environ.get("AIHUB_APIKEY"):
        print("\n  ❌ AIHUB_APIKEY 가 없다:")
        print('       export AIHUB_APIKEY="발급받은_키"')
        print("     키는 AI Hub 마이페이지에서 발급하고, **저장소에 커밋하지 않는다**.")
        print("     해당 데이터셋 '활용신청'도 승인돼 있어야 한다.")
        return 1

    if a.dry_run:
        print("\n  (--dry-run: 여기까지)")
        return 0

    keys = ",".join(k for k, _d, _m in plan)
    print(f"\n  다운로드 시작 — filekey {keys}")
    print("  10GB 는 회선에 따라 수십 분 걸린다. 끊기면 같은 명령을 다시 "
          "실행하면 이어받는다(curl -C -).")
    rc = run(DATASET, keys, a.out)
    if rc != 0:
        print(f"\n  aihubshell 종료코드 {rc} — 아래 검증 결과에서 원인을 본다.")

    print(f"\n{'=' * 72}\n  검증\n{'=' * 72}")
    vrc = verify(a.out)
    if vrc == 0:
        print("\n  ✅ 모두 정상. 다음 단계:")
        print(f"       unzip -o '{a.out}/*.zip' -d {a.out}/extracted")
        print(f"       python competition/src/finetune_polygon.py prep \\")
        print(f"           {a.out}/extracted {a.out}/extracted")
        print("     prep 이 라벨-이미지 **매칭률**을 알려준다. TS06 이 라벨의")
        print("     몇 %를 덮는지 보고 다음 zip(TS01~05)을 받을지 정하면 된다.")
    else:
        print("\n  ❌ 문제가 있는 파일이 있다. 위 진단의 대처법을 따를 것.")
    return vrc or rc


if __name__ == "__main__":
    raise SystemExit(main())
