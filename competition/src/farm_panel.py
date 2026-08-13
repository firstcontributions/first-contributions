"""같은 농장의 **연도별 변화** — 성적은 실제로 얼마나 움직이나.

지금까지 466행을 농장 466개처럼 다뤘다. 실제로는 **202개 농장 × 4년**
패널이다. 같은 농장을 따라가면 횡단면으로는 못 하는 질문에 답할 수 있다.

## 왜 횡단면보다 강한가

"NPD 가 낮은 농장이 PSY 가 높다"(횡단면 ρ −0.737)는 교란에 약하다. 시설이
좋고 사람이 많은 농장이 둘 다 좋을 뿐일 수 있다. **같은 농장의 전년 대비
변화**를 보면 시설·유전자·관리 문화가 차분으로 지워진다.

## 이 모듈이 내놓는 것

1. **개선폭의 현실성** — "PSY +1두 올리자"가 현실적인 요구인가.
   실측: 농장-연 239건 중 +1두 이상 오른 건 28%. 상위 4분의 1 수준의 한 해다.
2. **평균회귀 경고** — 낮은 농장이 더 오른다(ρ −0.296). 일부는 개선이
   아니라 잡음의 되돌림이다. 그래서 전년 수준을 맞춘 층에서 다시 본다.
3. **하락의 비대칭** — 이 프로젝트의 핵심 발견이다. 전년 수준을 맞춰도
   떨어질 때는 NPD 가 +11.6일 늘고 **이유두수는 그대로**(0.00두)다.
   즉 하락은 사양이 아니라 **발정·교배 관리**에서 온다.
4. **방어의 값** — 농장-연의 33%가 1두 이상 떨어진다(중앙 −2.40두).
   올리는 것보다 지키는 쪽이 기댓값이 크다.

    python competition/src/farm_panel.py --sows 300
"""
from __future__ import annotations

import argparse
import json
import os
import sys

import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, HERE)

OUT_JSON = os.path.join(ROOT, "competition", "data", "farm_panel.json")

# 변화를 추적하는 지표. sows 는 규모 변동을 걸러내기 위한 대조군이다 —
# ΔPSY 와 상관이 없어야 정상이고, 있으면 규모 변화가 섞였다는 뜻이다.
TRACK = ["psy", "npd", "weaned", "farrowing_rate", "turnover",
         "wean_to_estrus", "sows"]
KO = {"psy": "PSY", "npd": "비생산일수", "weaned": "이유두수",
      "farrowing_rate": "분만율", "turnover": "모돈회전율",
      "wean_to_estrus": "재귀발정일", "sows": "모돈두수(대조)"}
BIG = 1.0        # "의미 있는 변화" 기준(두). 실측 IQR 절반 정도다.


def pairs(d: pd.DataFrame) -> pd.DataFrame:
    """연속한 두 해가 있는 농장만 골라 전년 대비 차분을 만든다.

    **연도가 붙어 있는 경우만** 쓴다. 2020→2022 를 한 칸으로 세면 2년치
    변화가 1년치인 척하게 된다(패널이 불균형이라 실제로 그런 쌍이 있다).
    """
    d = d.dropna(subset=["psy"]).sort_values(["farm", "year"])
    rows = []
    for farm, x in d.groupby("farm"):
        x = x.sort_values("year")
        for i in range(1, len(x)):
            a, b = x.iloc[i - 1], x.iloc[i]
            if int(b["year"]) - int(a["year"]) != 1:
                continue
            r = {"farm": farm, "y0": int(a["year"]), "y1": int(b["year"]),
                 "psy0": float(a["psy"]), "npd0": float(a["npd"])}
            for m in TRACK:
                r["d_" + m] = float(b[m]) - float(a[m])
            rows.append(r)
    return pd.DataFrame(rows)


def movement(p: pd.DataFrame) -> dict:
    """ΔPSY 분포 — "+1두" 가 어느 정도 요구인지 눈금을 준다."""
    s = p["d_psy"]
    return {
        "n_pairs": int(len(p)), "n_farms": int(p["farm"].nunique()),
        "p10": round(float(s.quantile(.10)), 2),
        "p25": round(float(s.quantile(.25)), 2),
        "median": round(float(s.median()), 2),
        "p75": round(float(s.quantile(.75)), 2),
        "p90": round(float(s.quantile(.90)), 2),
        "share_up": round(float((s > 0).mean()), 3),
        "share_up_1": round(float((s >= BIG).mean()), 3),
        "share_down_1": round(float((s <= -BIG).mean()), 3),
        # +1두는 상위 몇 %의 한 해인가 — 지렛대 주장을 이 눈금에 맞춘다
        "pct_rank_of_plus1": round(float((s < BIG).mean()), 3),
    }


def mean_reversion(p: pd.DataFrame) -> dict:
    """낮은 농장이 더 오르는 정도 — **개선이 아니라 잡음일 수 있다.**

    전년 성적과 변화가 음의 상관이면 되돌림이 섞였다는 뜻이다. 이걸 안
    보고하면 "하위 농장은 +0.7두 오른다" 를 개선 여지로 오독하게 된다.
    """
    q25, q75 = p["psy0"].quantile(.25), p["psy0"].quantile(.75)
    lo, hi = p[p["psy0"] <= q25], p[p["psy0"] >= q75]
    return {
        "rho_prev_vs_delta": round(
            float(p["psy0"].corr(p["d_psy"], method="spearman")), 3),
        "q25_cut": round(float(q25), 1), "q75_cut": round(float(q75), 1),
        "low_n": int(len(lo)), "low_delta_median": round(float(lo["d_psy"].median()), 2),
        "high_n": int(len(hi)), "high_delta_median": round(float(hi["d_psy"].median()), 2),
    }


def drivers(p: pd.DataFrame) -> list:
    """ΔPSY 와 각 지표 변화의 상관.

    **항등식 항(NPD·이유두수·회전율)은 인과의 증거가 아니다** — 정의상
    묶여 있다. 여기서 새로운 건 분만율·재귀발정일처럼 항등식 밖에 있는
    지표도 같이 움직인다는 점과, 대조군(모돈두수)이 안 움직인다는 점이다.
    """
    out = []
    for m in TRACK:
        if m == "psy":
            continue
        s = p[["d_psy", "d_" + m]].dropna()
        out.append({"metric": m, "name_ko": KO[m], "n": int(len(s)),
                    "rho": round(float(s["d_psy"].corr(
                        s["d_" + m], method="spearman")), 3),
                    "in_identity": m in ("npd", "weaned", "turnover")})
    out.sort(key=lambda r: -abs(r["rho"]))
    return out


def paths(p: pd.DataFrame, matched: bool = True) -> dict:
    """오른 농장과 떨어진 농장은 **무엇이 달랐나**.

    matched=True 면 전년 PSY 중간층(사분위 사이)만 쓴다. 상승군은 원래
    낮았고 하락군은 원래 높았기 때문에(22.8 vs 25.1), 층을 안 맞추면
    평균회귀가 비대칭처럼 보인다.
    """
    src = p
    note = "전체"
    if matched:
        q25, q75 = p["psy0"].quantile(.25), p["psy0"].quantile(.75)
        src = p[(p["psy0"] > q25) & (p["psy0"] < q75)]
        note = f"전년 PSY {q25:.1f}~{q75:.1f} 중간층만"
    out = {"basis": note, "n": int(len(src)), "groups": []}
    for label, sel in (("상승", src["d_psy"] >= BIG),
                       ("하락", src["d_psy"] <= -BIG)):
        g = src[sel]
        row = {"label": label, "n": int(len(g)),
               "d_psy": round(float(g["d_psy"].median()), 2)}
        for m in ("npd", "weaned", "farrowing_rate"):
            row["d_" + m] = round(float(g["d_" + m].median()), 2)
        out["groups"].append(row)
    return out


def downside(p: pd.DataFrame, n_sows: int) -> dict:
    """하락을 막는 것의 기댓값 — 올리는 것과 같은 자에 놓고 잰다.

    지금까지 손익은 "PSY +1두 = 얼마" 로만 냈다. 실측으로는 농장-연의
    33%가 1두 이상 떨어지고 그 중앙이 −2.40두다. 방어를 안 세면 제품
    가치를 절반만 세는 셈이다.
    """
    import farm_economics as fe
    lo = p[p["d_psy"] <= -BIG]
    freq = float((p["d_psy"] <= -BIG).mean())
    size = float(lo["d_psy"].median())
    base_psy = 24.1                     # 실측 PSY 열 중앙
    surv = 0.86
    now = fe.per_sow_year(base_psy, surv)["net_per_sow"] * n_sows
    fell = fe.per_sow_year(base_psy + size, surv)["net_per_sow"] * n_sows
    return {
        "freq": round(freq, 3), "size_psy": round(size, 2),
        "loss_if_falls_won": round(now - fell),
        "expected_won_year": round((now - fell) * freq),
        "n_sows": n_sows, "base_psy": base_psy,
    }


def attrition(d: pd.DataFrame) -> dict:
    """보고를 멈춘 농장이 나쁜 농장이면 변화 분석이 낙관 쪽으로 기운다."""
    last = d.groupby("farm")["year"].max()
    lastpsy = d.sort_values("year").groupby("farm").last()["psy"]
    gone, stay = last[last < 2023].index, last[last == 2023].index
    return {"n_left": int(len(gone)), "n_stayed": int(len(stay)),
            "psy_left": round(float(lastpsy[gone].median()), 1),
            "psy_stayed": round(float(lastpsy[stay].median()), 1)}


def summary(n_sows: int = 300, path: str | None = None) -> dict:
    import korean_farm_stats as ks
    d = ks.load(path)
    p = pairs(d)
    return {"movement": movement(p), "mean_reversion": mean_reversion(p),
            "drivers": drivers(p), "paths_matched": paths(p, True),
            "paths_all": paths(p, False), "downside": downside(p, n_sows),
            "attrition": attrition(d),
            "basis": "국내 202농장 2020~2023 패널 · 연속 2년 쌍만"}


def _print(r: dict) -> None:
    m, mr, pa, dn = (r["movement"], r["mean_reversion"],
                     r["paths_matched"], r["downside"])
    print("=" * 74)
    print(f"  같은 농장의 연도별 변화 — {m['n_farms']}농장 · "
          f"연속 2년 쌍 {m['n_pairs']}건")
    print("=" * 74)

    print("\n① 성적은 실제로 얼마나 움직이나 (ΔPSY, 전년 대비)")
    print(f"   하위10% {m['p10']:+.2f} · 25% {m['p25']:+.2f} · "
          f"중앙 {m['median']:+.2f} · 75% {m['p75']:+.2f} · 90% {m['p90']:+.2f}")
    print(f"   오른 농장 {m['share_up']:.0%} · "
          f"+1두 이상 {m['share_up_1']:.0%} · -1두 이하 {m['share_down_1']:.0%}")
    print(f"   → \"PSY +1두\"는 상위 {1 - m['pct_rank_of_plus1']:.0%} 안에 드는 한 해다."
          f" 쉬운 요구가 아니다.")

    print("\n② 평균회귀 경고 — 낮은 농장이 더 오른다")
    print(f"   전년 성적 vs 변화 상관 {mr['rho_prev_vs_delta']:+.3f}")
    print(f"   전년 하위25%(≤{mr['q25_cut']}) {mr['low_delta_median']:+.2f}두 · "
          f"상위25%(≥{mr['q75_cut']}) {mr['high_delta_median']:+.2f}두")
    print("   → 일부는 개선이 아니라 잡음의 되돌림이다. 아래 ③은 층을 맞춰서 본다.")

    print(f"\n③ 오른 농장 vs 떨어진 농장 — 무엇이 달랐나 ({pa['basis']}, n={pa['n']})")
    print(f"   {'':6}{'건수':>5}{'ΔPSY':>8}{'ΔNPD':>8}{'Δ이유두수':>10}{'Δ분만율':>9}")
    for g in pa["groups"]:
        print(f"   {g['label']:<6}{g['n']:>5}{g['d_psy']:>+8.2f}"
              f"{g['d_npd']:>+8.1f}{g['d_weaned']:>+10.2f}"
              f"{g['d_farrowing_rate']:>+9.1f}")
    print("   → **떨어질 때 이유두수는 그대로다.** 하락은 사양이 아니라")
    print("     발정·교배 관리(NPD·분만율)에서 온다. 이 프로젝트가 겨냥한 자리다.")

    print("\n④ ΔPSY 와 함께 움직인 것")
    for x in r["drivers"]:
        tag = "항등식 항" if x["in_identity"] else ""
        print(f"   Δ{x['name_ko']:<14}{x['rho']:>+7.3f}  {tag}")
    print("   → 항등식 항은 정의상 묶여 있어 인과의 증거가 아니다. 대조군인")
    print("     모돈두수가 0 근처인 것이 규모 변동이 안 섞였다는 확인이다.")

    print(f"\n⑤ 지키는 값 (모돈 {dn['n_sows']}두 기준)")
    print(f"   농장-연의 {dn['freq']:.0%}가 1두 이상 떨어진다 · 중앙 {dn['size_psy']:+.2f}두")
    print(f"   떨어지면 연 {dn['loss_if_falls_won']:,}원 손실 → "
          f"기댓값 연 {dn['expected_won_year']:,}원")
    print("   → 지금까지 손익은 '올리면 얼마'만 셌다. 방어가 같은 크기의 자리다.")

    at = r["attrition"]
    print(f"\n※ 표본 주의. 불균형 패널이다(4년 연속 보고는 일부). 보고를 멈춘"
          f"\n  {at['n_left']}농장의 마지막 해 PSY 중앙 {at['psy_left']} vs 잔류"
          f" {at['n_stayed']}농장 {at['psy_stayed']} — 이탈 편향은 작지만 0 은 아니다.")


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(prog="farm_panel")
    ap.add_argument("--sows", type=int, default=300)
    ap.add_argument("--json", action="store_true", help="JSON 저장")
    a = ap.parse_args(argv)
    r = summary(a.sows)
    _print(r)
    if a.json:
        os.makedirs(os.path.dirname(OUT_JSON), exist_ok=True)
        json.dump(r, open(OUT_JSON, "w", encoding="utf-8"),
                  ensure_ascii=False, indent=1)
        print(f"\n저장: {os.path.relpath(OUT_JSON, ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
