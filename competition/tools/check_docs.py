"""문서에 박힌 숫자가 실제와 맞는지 검사한다.

발표자료·README 의 수치는 손으로 적은 것이라 코드가 바뀌면 조용히 어긋난다.
실제로 테스트를 47개에서 53개로 늘렸는데 문서 세 곳이 47 로 남아 있었다.
심사에서 숫자가 어긋나면 나머지 숫자도 못 믿게 되므로, 자동으로 잡는다.

검사 대상:
  1. 규모       테스트 수 · 모듈 수 · 대시보드 뷰 수
  2. 성능       posture_crossview.json / polygon_shape_eval.json 의 실측값
  3. 링크       문서가 가리키는 파일이 실제로 있는지
  4. 비밀값     API 키처럼 보이는 문자열이 커밋될 위치에 있는지

    python competition/tools/check_docs.py
"""
from __future__ import annotations

import glob
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
COMP = os.path.dirname(HERE)
ROOT = os.path.dirname(COMP)
DOCS = [os.path.join(COMP, "README.md"),
        os.path.join(COMP, "docs", "PRESENTATION.md"),
        # 현황 브리핑도 모듈·뷰·테스트 수를 인용한다. 검사 대상에 안 넣으면
        # 다른 대화로 퍼 나른 뒤에 조용히 낡는다.
        os.path.join(COMP, "docs", "STATUS.md")]


# -- 실제값 수집 -----------------------------------------------------------
def actual_counts() -> dict:
    src = glob.glob(os.path.join(COMP, "src", "*.py"))
    builders = [f for f in src if os.path.basename(f).startswith("build_")]
    sys.path.insert(0, os.path.join(COMP, "src"))
    import build_dashboard_hub as hub
    tests = os.path.join(COMP, "tests", "smoke_test.py")
    txt = open(tests, encoding="utf-8").read()
    # main() 의 tests 리스트에 등록된 것만 실제로 돈다
    body = txt.split("tests = [", 1)[1].split("]", 1)[0]
    n_tests = len([x for x in re.findall(r"test_\w+", body)])
    return {
        "modules": len(src) - len(builders),
        "builders": len(builders),
        "src_total": len(src),
        "views": len(hub.VIEWS),
        "tests": n_tests,
    }


def actual_metrics() -> dict:
    """저장된 실측 JSON 에서 핵심 수치를 뽑는다."""
    m = {}
    p = os.path.join(COMP, "data", "posture_crossview.json")
    if os.path.exists(p):
        r = json.load(open(p, encoding="utf-8"))
        best = max(r["configs"], key=lambda c: c["cls3"]["acc_w"])
        geom = next(c for c in r["configs"] if "기존" in c["tag"])
        m["posture3_best_acc"] = round(best["cls3"]["acc_w"], 3)
        m["posture3_best_mf1"] = round(best["cls3"]["mf1_w"], 3)
        m["posture3_geom_acc"] = round(geom["cls3"]["acc_w"], 3)
        m["posture5_ceiling"] = round(r["ceiling"]["ceiling"], 3)
        m["posture3_baseline"] = round(r["baseline"]["cls3"]["acc_w"], 3)
    p = os.path.join(COMP, "data", "polygon_shape_eval.json")
    if os.path.exists(p):
        r = json.load(open(p, encoding="utf-8"))
        m["poly_gain_posture"] = round(r["posture"]["mf1_gain"], 3)
        m["poly_bbox_mf1"] = round(r["posture"]["bbox"]["mf1_mean"], 3)
    return m


# -- 검사 ------------------------------------------------------------------
def check_counts(report: list) -> None:
    a = actual_counts()
    for path in DOCS:
        if not os.path.exists(path):
            continue
        t = open(path, encoding="utf-8").read()
        name = os.path.basename(path)
        # 뷰 수는 **대시보드 문맥에서만** 센다. "뷰 8개 중 2개만 held-out" 은
        # 카메라 뷰 얘기라서 그냥 잡으면 오탐이다(실제로 두 건 났다).
        for pat, key, label, need in (
            (r"테스트\s*(\d+)\s*개", "tests", "테스트 수", None),
            (r"(\d+)\s*/\s*\d+\s*통과", "tests", "테스트 통과 수", None),
            (r"뷰\s*(\d+)\s*개", "views", "대시보드 뷰 수", "대시보드"),
            (r"(\d+)\s*뷰", "views", "대시보드 뷰 수", "대시보드"),
            (r"모듈\s*(\d+)\s*개", "modules", "모듈 수", None),
            (r"src/\s*\((\d+)개\)", "src_total", "src 파일 수", None),
        ):
            for mobj in re.finditer(pat, t):
                ls = t.rfind("\n", 0, mobj.start()) + 1
                le = t.find("\n", mobj.end())
                line_txt = t[ls:le if le > 0 else len(t)]
                if need and need not in line_txt:
                    continue
                got = int(mobj.group(1))
                if got != a[key]:
                    line = t[:mobj.start()].count("\n") + 1
                    report.append(
                        f"{name}:{line}  {label} {got} → 실제 {a[key]}"
                        f"   ({mobj.group(0).strip()})")


def check_metrics(report: list) -> None:
    m = actual_metrics()
    if not m:
        report.append("실측 JSON 이 없다 — 성능 수치를 검증할 수 없다")
        return
    # 문서가 이 수치를 언급한다면 실제와 같아야 한다
    watched = [
        ("posture3_best_acc", r"0\.636"),
        ("posture5_ceiling", r"0\.861"),
        ("posture3_baseline", r"0\.547"),
        ("poly_bbox_mf1", r"0\.431"),
    ]
    for key, pat in watched:
        if key not in m:
            continue
        want = f"{m[key]:.3f}"
        for path in DOCS:
            if not os.path.exists(path):
                continue
            t = open(path, encoding="utf-8").read()
            # 문서가 옛 값을 쓰고 있는데 실제가 다르면 잡는다
            if re.search(pat, t) and pat.replace("\\", "") != want:
                report.append(
                    f"{os.path.basename(path)}  {key}: 문서 "
                    f"{pat.replace(chr(92), '')} → 실제 {want}")


def check_links(report: list) -> None:
    """문서가 가리키는 파일이 실제로 있는지."""
    for path in DOCS:
        if not os.path.exists(path):
            continue
        t = open(path, encoding="utf-8").read()
        name = os.path.basename(path)
        for mobj in re.finditer(r"`(competition/[\w/\.\-]+\.(?:py|md|sh|yaml))`", t):
            rel = mobj.group(1)
            if not os.path.exists(os.path.join(ROOT, rel)):
                line = t[:mobj.start()].count("\n") + 1
                report.append(f"{name}:{line}  없는 파일: {rel}")
        # 대시보드 뷰 파일명이 허브에 등록돼 있는지
        sys.path.insert(0, os.path.join(COMP, "src"))
        import build_dashboard_hub as hub
        known = {v[0] for v in hub.VIEWS}
        for mobj in re.finditer(r"`(\w+\.html)`", t):
            fn = mobj.group(1)
            if fn not in known and fn != "index.html":
                line = t[:mobj.start()].count("\n") + 1
                report.append(f"{name}:{line}  허브에 없는 뷰: {fn}")


# 키처럼 보이는 것 — 실제로 노출된 적이 있어 검사한다
KEYLIKE = [
    (r"\b[0-9A-F]{8}-[0-9A-F]{4}-[0-9A-F]{4}-[0-9A-F]{4}-[0-9A-F]{12}\b",
     "AI Hub API 키 형식(UUID 대문자)"),
    (r"\b[a-f0-9]{32}\b", "32자리 16진 토큰(Kaggle 등)"),
]
KEY_SKIP_DIRS = {".git", "__pycache__", "node_modules", "dashboard", "data",
                 "outputs", "models"}


def check_secrets(report: list) -> None:
    """커밋되는 위치에 키가 있으면 잡는다. 노출은 되돌릴 수 없다."""
    for base, dirs, files in os.walk(COMP):
        dirs[:] = [d for d in dirs if d not in KEY_SKIP_DIRS]
        for f in files:
            if not f.endswith((".py", ".md", ".sh", ".yaml", ".yml", ".txt",
                               ".json")):
                continue
            p = os.path.join(base, f)
            try:
                t = open(p, encoding="utf-8", errors="ignore").read()
            except OSError:
                continue
            for pat, what in KEYLIKE:
                for mobj in re.finditer(pat, t):
                    s = mobj.group(0)
                    # 예시·자리표시자는 넘어간다
                    ctx = t[max(0, mobj.start() - 60):mobj.start()].lower()
                    if any(w in ctx for w in ("예시", "example", "발급받은",
                                              "your_", "<", "sha256")):
                        continue
                    line = t[:mobj.start()].count("\n") + 1
                    report.append(
                        f"{os.path.relpath(p, ROOT)}:{line}  "
                        f"**{what}로 보이는 문자열**: {s[:8]}…")


def gap_figures() -> dict:
    """포지셔닝 표가 인용하는 진단 수치를 **다시 계산해서** 돌려준다.

    이 표는 "NPD +19일 → PSY −1.50두 → 연 5,627만원" 같은 값을 싣는다.
    처음 쓸 때 다른 조건(NPD·이유두수를 동시에 나쁘게 준 경우)의 값을
    베껴 와서 −1.37두 / 5,102만원 으로 잘못 적었다. 사람 눈으로는 안
    잡히니 여기서 계산해 대조한다.
    """
    sys.path.insert(0, os.path.join(COMP, "src"))
    sys.path.insert(0, COMP)
    import farm_gap as fg
    from pigflow.config import BREEDING_DEFAULTS as B

    st = fg.load_stats()
    med = {k: v["p50"] for k, v in st["quantiles"].items()}

    # ① NPD 만 실측 하위(62일)로 놓았을 때 — 표의 "격차의 크기" 칸
    d = fg.diagnose({"npd": 62.0}, st, n_sows=300)
    npd = next(r for r in d["rows"] if r["metric"] == "npd")
    won = next(m for m in d["won_per_year"] if m["metric"] == "npd")

    # ② 프로그램 가정값 대 중앙 농장 — 표의 "낙관 폭" 칸
    prog = fg.diagnose(
        {"weaned": B["weaned_per_litter"], "lactation": B["lactation_days"],
         "gestation": B["gestation_days"],
         "farrowing_rate": B["farrowing_rate"] * 100,
         "wean_to_estrus": B["wean_to_service_days"],
         "npd": fg.npd_floor_annual(B)}, st)
    pnpd = next(r for r in prog["rows"] if r["metric"] == "npd")
    return {
        "npd_gap_days": round(62.0 - med["npd"]),
        "npd_psy": abs(npd["psy_recover"]),
        "npd_won_eok": won["won_year"],
        "prog_psy": prog["psy"],
        "med_psy": prog["psy_median_farm"],
        "prog_npd_psy": pnpd["psy_recover"],
    }


def check_gap_figures(report: list) -> None:
    try:
        g = gap_figures()
    except Exception as e:                                   # noqa: BLE001
        report.append(f"진단 수치를 재계산하지 못했다: {e}")
        return
    # 문서에 이 문자열 그대로 실려 있어야 한다. 데이터가 바뀌면 재계산값이
    # 바뀌고, 문서가 옛 값을 들고 있으면 여기서 걸린다.
    want = {
        "NPD 격차 일수": f"{g['npd_gap_days']}일",
        "NPD 회수 PSY": f"{g['npd_psy']:.2f}두",
        "NPD 금액": f"{g['npd_won_eok'] / 10_000:,.0f}만원",
        "가정 PSY": f"{g['prog_psy']}",
        "중앙 농장 PSY": f"{g['med_psy']}",
        "가정 NPD 낙관 폭": f"{g['prog_npd_psy']:.2f}두",
    }
    for path in DOCS:
        if not os.path.exists(path):
            continue
        # 문서는 조판용 유니코드 빼기(U+2212)를 쓴다. ASCII 로 맞춰 놓지
        # 않으면 '-2.02두' 가 '−2.02두' 와 안 맞아 헛경보가 난다.
        t = open(path, encoding="utf-8").read().replace("−", "-")
        if "격차의 크기" not in t and "성적 격차" not in t:
            continue        # 포지셔닝 표가 없는 문서는 건너뛴다
        for label, s in want.items():
            if s not in t:
                report.append(
                    f"{os.path.basename(path)}  포지셔닝 표의 {label}: "
                    f"재계산값 '{s}' 가 문서에 없다")


def main() -> int:
    report: list = []
    check_counts(report)
    check_metrics(report)
    check_gap_figures(report)
    check_links(report)
    check_secrets(report)

    a = actual_counts()
    print("=" * 72)
    print("  문서 일관성 검사")
    print("=" * 72)
    print(f"  실제: 모듈 {a['modules']} · 빌더 {a['builders']} "
          f"(src {a['src_total']}) · 뷰 {a['views']} · 테스트 {a['tests']}")
    m = actual_metrics()
    if m:
        print("  실측: " + " · ".join(f"{k} {v}" for k, v in m.items()))
    if not report:
        print("\n  ✅ 불일치 없음")
        return 0
    print(f"\n  ❌ {len(report)}건")
    for r in report:
        print(f"     {r}")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
