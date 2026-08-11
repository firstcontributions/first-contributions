#!/usr/bin/env python3
"""내려받은 파일이 왜 tar 가 아닌지 진단한다.

    python competition/tools/check_download.py <파일 또는 디렉터리>

"tar: This does not look like a tar archive" 는 원인이 여러 개인데 메시지가
하나라서 구분이 안 된다. 실제로 이 저장소에서도 82바이트짜리 `.tar` 가 나온
적이 있는데, 열어 보니 내용이 이거였다:

    AI 허브는 해외에서의 데이터 다운로드를 제한하고 있습니다.

즉 서버가 **에러 문구를 tar 파일 이름으로 내려준 것**이다. tar 는 그걸
아카이브로 읽으려다 실패한다. 파일을 열어 보기 전에는 알 수 없다.

진단하는 것:
  1. 에러 문구가 tar 로 위장했는가        (해외 IP 차단 · 키 오류 · 활용신청 미승인)
  2. 분할 조각(.partNN)이 병합 안 됐는가   AI Hub 는 대용량을 쪼개서 준다
  3. 사실 gzip/zip/bz2/xz 인가            확장자만 tar
  4. 전송이 중간에 끊겼는가                tar 헤더는 맞는데 끝이 잘림
"""
from __future__ import annotations

import os
import re
import subprocess
import sys
import tarfile

# (오프셋, 매직, 이름, 푸는 법)
MAGIC = [
    (0, b"\x1f\x8b", "gzip", "tar -xzf <파일>   (또는 gunzip)"),
    (0, b"PK\x03\x04", "zip", "unzip <파일>"),
    (0, b"PK\x05\x06", "zip(빈 아카이브)", "unzip <파일> — 내용이 없다"),
    (0, b"BZh", "bzip2", "tar -xjf <파일>"),
    (0, b"\xfd7zXZ", "xz", "tar -xJf <파일>"),
    (0, b"7z\xbc\xaf", "7-zip", "7z x <파일>"),
    (0, b"Rar!", "rar", "unrar x <파일>"),
    (0, b"%PDF", "PDF", "tar 가 아니다 — 문서를 받았다"),
    (257, b"ustar", "tar (POSIX)", "tar -xvf <파일>"),
]

# 위에서부터 먼저 맞는 것을 쓴다. 해외 차단이 가장 구체적이고 흔하므로 먼저.
HINTS = [
    (r"해외|overseas|국외", "**해외 IP 차단.** AI Hub 는 국내망에서만 내려받을 수 있다. "
                            "국내 회선/서버에서 다시 받아야 한다."),
    (r"승인|권한|신청|approval|permission",
     "**활용신청 미승인.** AI Hub 에서 해당 데이터셋 활용신청이 승인돼야 한다 "
     "(보통 1~2 영업일)."),
    (r"로그인|인증|apikey|api_key|token|unauthor",
     "**인증 실패.** AIHUB_APIKEY 를 확인한다. 키는 절대 커밋하지 않는다."),
    (r"페이지가 존재하지|존재하지 않|not found|404",
     "**주소가 틀렸다(filekey 만료·오타).** AI Hub 는 데이터셋이 갱신되면 filekey 가\n"
     "     바뀐다. 받기 전에 최신값부터 조회할 것:\n"
     "       python competition/src/aihub.py tree <datasetkey>\n"
     "     브라우저에서 받는 중이라면 다운로드 링크가 만료된 것이므로 목록에서 다시 연다."),
]
TAR_BLOCK = 512


def human(n: int) -> str:
    for u in ("B", "KB", "MB", "GB", "TB"):
        if n < 1024 or u == "TB":
            return f"{n:.0f}{u}" if u == "B" else f"{n:.1f}{u}"
        n /= 1024.0
    return str(n)


def sniff(path: str) -> tuple:
    with open(path, "rb") as f:
        head = f.read(512)
    for off, mag, name, how in MAGIC:
        if head[off:off + len(mag)] == mag:
            return name, how
    return None, None


def as_text(path: str, limit: int = 4000) -> str | None:
    """작은 파일이면 텍스트로 읽어 본다 — 에러 문구일 확률이 높다."""
    if os.path.getsize(path) > 200_000:
        return None
    try:
        with open(path, encoding="utf-8") as f:
            t = f.read(limit)
    except UnicodeDecodeError:
        return None
    # 제어문자가 많으면 바이너리로 본다
    ctrl = sum(1 for c in t if ord(c) < 9 or 13 < ord(c) < 32)
    return None if ctrl > len(t) * 0.02 else t


def find_parts(path: str) -> list:
    """같은 이름의 분할 조각을 찾는다. AI Hub 는 대용량을 .partNN 으로 쪼갠다."""
    d = os.path.dirname(os.path.abspath(path)) or "."
    base = re.sub(r"\.part\d+$", "", os.path.basename(path))
    stem = os.path.splitext(base)[0]
    parts = [f for f in os.listdir(d)
             if re.match(re.escape(stem) + r".*\.part\d+$", f)]
    return sorted(parts, key=lambda x: int(re.search(r"\d+$", x).group()))


def check(path: str) -> int:
    print(f"\n{'=' * 70}\n  {path}\n{'=' * 70}")
    if not os.path.exists(path):
        print("  파일이 없다.")
        return 1
    size = os.path.getsize(path)
    print(f"  크기 {human(size)} ({size:,} 바이트)")

    if size == 0:
        print("\n  ❌ **빈 파일.** 전송이 시작되지도 못했다. 네트워크·인증을 먼저 본다.")
        return 1

    # 1) 에러 문구가 tar 로 위장한 경우 — 가장 흔하고 가장 안 보인다
    txt = as_text(path)
    if txt is not None:
        print("\n  ❌ **이건 아카이브가 아니라 텍스트다.** 내용:")
        print("  " + "─" * 66)
        for line in txt.strip().splitlines()[:15]:
            print(f"  │ {line}")
        print("  " + "─" * 66)
        if re.search(r"<!DOCTYPE|<html", txt, re.I):
            print("\n  → **HTML 페이지를 받았다** — 로그인 리다이렉트거나 에러 페이지다.")
        for pat, msg in HINTS:
            if re.search(pat, txt, re.I):
                print(f"  → {msg}")
                break
        else:
            print("  → 서버가 에러 응답을 파일로 내려줬다. 위 문구가 원인이다.")
        return 1

    # 2) 분할 조각
    parts = find_parts(path)
    if parts:
        d = os.path.dirname(os.path.abspath(path)) or "."
        total = sum(os.path.getsize(os.path.join(d, p)) for p in parts)
        print(f"\n  ⚠️  분할 조각 {len(parts)}개 발견 (합계 {human(total)}):")
        for p in parts[:6]:
            print(f"      {p}  {human(os.path.getsize(os.path.join(d, p)))}")
        if len(parts) > 6:
            print(f"      ... 외 {len(parts) - 6}개")
        stem = re.sub(r"\.part\d+$", "", parts[0])
        print("\n  → 조각을 **순서대로 이어붙인 뒤** 풀어야 한다:")
        print(f"      cd {d}")
        print(f"      ls -v {stem}.part* | xargs cat > merged.tar")
        print("      tar -xvf merged.tar")
        print("     `ls -v` 를 쓰는 이유: 기본 알파벳 순은 part10 이 part2 보다")
        print("     앞에 와서, 조각이 10개를 넘으면 `cat *.part*` 가 순서를 뒤섞는다.")
        print("     이어붙인 크기가 조각 합계와 같은지 확인하고 풀 것.")
        return 1

    # 3) 다른 압축 형식
    kind, how = sniff(path)
    if kind and kind.startswith("tar"):
        print(f"\n  ✅ tar 헤더 정상 ({kind}).")
    elif kind:
        print(f"\n  ⚠️  실제 형식은 **{kind}** 다. 확장자만 tar 인 것.")
        print(f"  → {how.replace('<파일>', path)}")
        return 1
    else:
        print(f"\n  ❌ 알려진 아카이브 매직이 없다. 첫 32바이트:")
        with open(path, "rb") as f:
            print("      " + f.read(32).hex(" "))
        print("  → 전송이 깨졌거나 형식이 다르다. 다시 받는 것이 빠르다.")
        return 1

    # 4) 잘림 검사 — **tarfile 은 잘린 파일을 조용히 통과시킨다.**
    #    앞부분 엔트리만 온전하면 예외 없이 끝나므로, 실제로 이 검사를 안 넣었을 때
    #    2,000바이트로 자른 파일이 "정상"으로 나왔다. tar 는 512바이트 블록 단위이고
    #    끝에 0으로 채운 블록 2개(1,024바이트)가 와야 아카이브가 닫힌 것이다.
    truncated = []
    if size % TAR_BLOCK:
        truncated.append(f"크기 {size:,} 가 {TAR_BLOCK}의 배수가 아니다")
    if size >= 2 * TAR_BLOCK:
        with open(path, "rb") as f:
            f.seek(-2 * TAR_BLOCK, os.SEEK_END)
            if f.read(2 * TAR_BLOCK) != b"\0" * (2 * TAR_BLOCK):
                truncated.append("끝에 종료 블록(0 × 1,024바이트)이 없다")
    else:
        truncated.append("파일이 tar 최소 크기보다 작다")

    try:
        with tarfile.open(path) as t:
            names, n = [], 0
            for m in t:
                if n < 5:
                    names.append(f"{m.name}  ({human(m.size)})")
                n += 1
                if n > 200_000:
                    break
    except tarfile.ReadError as e:
        # 잘린 위치가 엔트리 한가운데면 여기로, 엔트리 경계면 아래 truncated 로
        # 온다. 원인은 같으므로 **같은 문장으로** 말한다.
        truncated.append(f"읽다가 실패: {e}")
        n, names = -1, []

    if truncated:
        got = f"항목 {n:,}개까지는 읽히지만" if n >= 0 else "아카이브가 온전하지 않다"
        print(f"\n  ❌ **전송이 잘렸다.** {got}:")
        for r in truncated:
            print(f"      · {r}")
        print("  → tar 는 앞부분만 온전해도 그만큼은 풀어 주므로 '되는 것처럼' 보인다.")
        print("     원본 크기와 대조하고 다시 받는 것이 맞다. 급하면:")
        print(f"      tar -xvf {path} --ignore-zeros   # 읽히는 데까지만")
        return 1

    print(f"  ✅ 정상 — 항목 {n:,}개, 종료 블록 확인")
    for x in names:
        print(f"      {x}")
    if n > 5:
        print("      ...")
    return 0


def main(argv) -> int:
    if len(argv) < 2:
        print(__doc__)
        return 2
    rc = 0
    for target in argv[1:]:
        if os.path.isdir(target):
            files = [os.path.join(target, f) for f in sorted(os.listdir(target))
                     if os.path.isfile(os.path.join(target, f))]
            if not files:
                print(f"{target}: 빈 디렉터리")
                rc = 1
            for f in files:
                rc |= check(f)
        else:
            rc |= check(target)
    return rc


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
