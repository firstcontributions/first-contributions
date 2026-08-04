"""AI Hub(aihub.or.kr) 데이터 API 클라이언트.

AI Hub 공식 `aihubshell`(v0.6) 이 사용하는 것과 동일한 엔드포인트를 감싼다.

  - 데이터셋 목록 / 파일 트리 조회 : API 키 불필요
  - 데이터 다운로드                 : API 키 필요 (+ 해당 데이터셋 '활용신청' 승인)

API 키는 코드에 넣지 말고 환경변수 AIHUB_APIKEY 로 전달한다.
    export AIHUB_APIKEY="발급받은_키"

사용 예:
    python competitive/src/aihub.py search 양돈
    python competitive/src/aihub.py list
    python competitive/src/aihub.py tree 71408
    python competitive/src/aihub.py download 71408 509489,509492   # 라벨링데이터만
"""
from __future__ import annotations

import os
import subprocess
import sys
import urllib.request

BASE_URL = "https://api.aihub.or.kr"
DATASET_URL = f"{BASE_URL}/info/dataset.do"          # 전체 데이터셋 목록
FILETREE_URL = f"{BASE_URL}/info/{{key}}.do"          # 데이터셋 파일 트리
# 다운로드/병합은 검증된 공식 스크립트에 위임한다.
AIHUBSHELL = os.path.join(os.path.dirname(__file__), "..", "tools", "aihubshell")


def _get(url: str) -> str:
    # AI Hub info 엔드포인트는 상태코드로 502를 반환하면서도 본문에는 정상
    # 데이터를 담아 보낸다. 공식 aihubshell 이 `curl -s` 로 상태코드를 무시하고
    # 본문만 읽는 것과 동일하게, HTTPError 여도 본문을 그대로 읽는다.
    try:
        with urllib.request.urlopen(url, timeout=60) as r:  # noqa: S310
            return r.read().decode("utf-8", errors="replace")
    except urllib.error.HTTPError as e:
        return e.read().decode("utf-8", errors="replace")


def list_datasets() -> str:
    """전체 데이터셋 목록(키 불필요)."""
    return _get(DATASET_URL)


def file_tree(datasetkey: str) -> str:
    """특정 데이터셋의 파일 트리(파일명 | 크기 | filekey). 키 불필요."""
    return _get(FILETREE_URL.format(key=datasetkey))


def search(keyword: str) -> list[str]:
    """데이터셋 목록에서 키워드가 포함된 행을 반환."""
    return [ln for ln in list_datasets().splitlines() if keyword in ln]


def download(datasetkey: str, filekeys: str = "all") -> int:
    """데이터셋(일부) 다운로드. AIHUB_APIKEY 필요.

    filekeys: 파일 트리에서 확인한 filekey들을 콤마로 구분 (예: "509489,509492").
              "all" 이면 전체(원천 포함 → 수백 GB일 수 있으니 주의).
    """
    apikey = os.environ.get("AIHUB_APIKEY")
    if not apikey:
        raise SystemExit(
            "AIHUB_APIKEY 환경변수가 없습니다. AI Hub 마이페이지에서 API 키를\n"
            "발급받고 export AIHUB_APIKEY=... 로 설정한 뒤 다시 실행하세요.\n"
            "(다운로드하려는 데이터셋의 '활용신청' 승인도 필요합니다.)")

    cmd = ["bash", os.path.abspath(AIHUBSHELL),
           "-aihubapikey", apikey,
           "-mode", "d",
           "-datasetkey", str(datasetkey),
           "-filekey", filekeys]
    print(f"실행: aihubshell -mode d -datasetkey {datasetkey} -filekey {filekeys}")
    return subprocess.call(cmd)


def _usage() -> None:
    print(__doc__)


def main(argv: list[str]) -> int:
    if not argv:
        _usage()
        return 1
    cmd = argv[0]
    if cmd == "list":
        print(list_datasets())
    elif cmd == "search" and len(argv) >= 2:
        hits = search(argv[1])
        print("\n".join(hits) if hits else f"'{argv[1]}' 검색 결과 없음")
    elif cmd == "tree" and len(argv) >= 2:
        print(file_tree(argv[1]))
    elif cmd == "download" and len(argv) >= 2:
        filekeys = argv[2] if len(argv) >= 3 else "all"
        return download(argv[1], filekeys)
    else:
        _usage()
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
