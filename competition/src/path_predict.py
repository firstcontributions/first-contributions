"""작업 로그 → **실제 경로** → **다음 사건 예측**.

`work_log` 는 "무엇을 언제 했나" 를 추가만 하며 쌓고, `repro_calendar` 는
"언제 무엇을 해야 하나" 를 표준 간격으로 낸다. 그 둘 사이에 빈 자리가 있다 —
**이 농장에서 실제로 무슨 경로가 밟혔고, 다음엔 무엇이 언제 올 것인가.**

    로그(사건 나열)  →  개체별 경로  →  경로 변형·이탈 지점
                                     →  전이별 실제 간격(이 농장의 값)
                                     →  다음 사건 날짜·종류 예측

## 왜 표준 캘린더로 충분하지 않은가 — 그리고 정말 부족한가

표준은 WEI 5일·임신 115일 같은 **문헌 상수**다. 농장마다 다를 것 같지만,
그건 확인해야 할 주장이지 전제가 아니다. 그래서 예측은 반드시 **표준 캘린더를
기준선으로** 놓고 잰다. 로그로 만든 예측이 문헌 상수를 못 이기면, 그 로그는
예측에 관한 한 값이 없는 것이고 그렇게 보고한다(원칙 3·4).

## 시간을 거슬러 배우지 않는다

경로 예측에서 가장 쉬운 자기기만은 미래 사건으로 과거를 맞히는 것이다.
학습·평가는 **교배일 기준 시간 순**으로 자른다. 같은 개체가 양쪽에 들어가는
것은 막지 않는다 — 현장에서도 그 모돈의 과거는 알고 예측하기 때문이다.
대신 **개체 단위로 자른 결과를 나란히** 낸다. 둘이 크게 다르면 개체를
외운 것이다.

## 지금 로그는 합성이다

실농장 로그가 없으므로 `synth_farm`(실측 계절·재발 구성으로 보정된 생성기)
으로 사건을 만든다. **여기서 나오는 정확도는 농장 성적이 아니라 장치가
도는지의 확인이다.** 다만 하나는 진짜 검증이 된다 — 생성기에 넣은 값을
로그만 보고 되찾는지(`recovery`). 못 되찾으면 경로 복원이 틀린 것이다.

    python competition/src/path_predict.py --sows 300 --years 3
"""
from __future__ import annotations

import argparse
import json
import os
import sys
from datetime import date, timedelta

import numpy as np
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
sys.path.insert(0, ROOT)

import ml_core                                                  # noqa: E402
import repro_calendar as rc                                     # noqa: E402
import synth_farm as sf                                         # noqa: E402

OUT = os.path.join(ROOT, "data", "path_predict.json")

# 사건 어휘. work_log 의 task 이름과 맞춰 둔다 — 앱이 쌓는 로그가 그대로
# 들어오려면 낱말이 같아야 한다.
EVENTS = ("이유", "발정확인", "교배", "분만", "재발정")
STANDARD = ("이유", "발정확인", "교배", "분만")

# 표준 캘린더 상수 = **기준선**. 여기서 새로 적지 않고 repro_calendar 에서 받는다.
B0_DAYS = {
    ("이유", "발정확인"): rc.WEI_BY_PARITY["sow"],
    ("발정확인", "교배"): 1.0,
    ("교배", "분만"): float(rc.GESTATION),
    ("교배", "재발정"): float(rc.RETURN_CHECK),
    ("분만", "이유"): float(rc.LACTATION),
}

MIN_OBS = 30          # 전이별 최소 관측. 이보다 적으면 그 전이는 예측하지 않는다
# 되찾기 허용 오차(일). 생성기가 날짜를 내림해 만들기 때문에 되찾은 평균은
# 주입값보다 반나절쯤 짧게 나온다 — 그 계통 오차를 덮을 만큼만 준다.
TOL_DAYS = 0.7
HIT_DAYS = 2          # 예상일 ±이 일수 안에 들면 맞힌 것으로 본다
CUT_Q = 0.70          # 시간 순 분할 지점(교배일 분위수)


def to_events(cycles: pd.DataFrame) -> pd.DataFrame:
    """사이클 표 → **사건 로그**(한 행 = 한 사건). 앱이 쌓는 모양과 같다.

    한 사이클이 여러 행으로 펼쳐진다. 분만한 사이클은 이유까지, 실패한
    사이클은 재발정까지다. `cycle` 열을 달아 두면 나중에 사이클 단위로
    되묶을 수 있다 — 로그만 남기고 되묶지 못하면 경로를 못 그린다.
    """
    rows = []
    for i, r in enumerate(cycles.itertuples(index=False)):
        sid, cyc = str(r.sow_id), i
        base = {"animal_id": sid, "cycle": cyc, "parity": int(r.parity)}
        if r.wean_prev is not None:
            rows.append({**base, "event": "이유", "date": r.wean_prev})
        rows.append({**base, "event": "발정확인", "date": r.estrus})
        rows.append({**base, "event": "교배", "date": r.service})
        if r.outcome == "분만":
            rows.append({**base, "event": "분만", "date": r.farrow})
        else:
            # 재발정은 **다음 사이클의 발정확인과 같은 날이 아니다.**
            # 재발을 확인한 날이 따로 있고, 거기서 다음 교배가 준비된다.
            rows.append({**base, "event": "재발정",
                         "date": r.service + timedelta(days=int(rc.RETURN_CHECK)),
                         "note": r.return_type or ""})
    ev = pd.DataFrame(rows)
    ev["date"] = pd.to_datetime(ev["date"]).dt.date
    return ev.sort_values(["animal_id", "date", "cycle"]).reset_index(drop=True)


def journeys(ev: pd.DataFrame) -> pd.DataFrame:
    """개체별 사건 나열. 경로는 여기서부터 나온다."""
    out = []
    for sid, g in ev.groupby("animal_id"):
        g = g.sort_values(["date", "cycle"])
        out.append({"animal_id": sid, "n_events": int(len(g)),
                    "first": g["date"].iloc[0], "last": g["date"].iloc[-1],
                    "seq": " → ".join(g["event"]),
                    "n_cycles": int(g["cycle"].nunique())})
    return pd.DataFrame(out)


def variants(ev: pd.DataFrame, top: int = 8) -> pd.DataFrame:
    """**한 번식 사이클 안의 경로 변형**과 빈도.

    개체 전체 나열을 그대로 세면 길이가 제각각이라 변형이 수백 개로 흩어진다.
    사이클(이유~다음 이유) 단위로 잘라야 "표준 경로가 몇 %, 재발이 낀 경로가
    몇 %" 라는 물음에 답이 된다.
    """
    rows = []
    for (sid, cyc), g in ev.groupby(["animal_id", "cycle"]):
        seq = tuple(g.sort_values("date")["event"])
        span = (g["date"].max() - g["date"].min()).days
        rows.append({"path": " → ".join(seq), "days": span,
                     "standard": seq == STANDARD})
    d = pd.DataFrame(rows)
    agg = (d.groupby("path")
             .agg(n=("path", "size"), median_days=("days", "median"),
                  standard=("standard", "first"))
             .sort_values("n", ascending=False))
    agg["share"] = (agg["n"] / agg["n"].sum()).round(4)
    return agg.head(top).reset_index()


def transitions(ev: pd.DataFrame) -> pd.DataFrame:
    """전이별 **이 농장의 실제 간격** 분포. 표준 상수와 나란히 놓는다."""
    rows = []
    for sid, g in ev.groupby("animal_id"):
        g = g.sort_values(["date", "cycle"]).reset_index(drop=True)
        for a, b in zip(g.itertuples(index=False), g.iloc[1:].itertuples(index=False)):
            rows.append({"from": a.event, "to": b.event,
                         "days": (b.date - a.date).days,
                         "animal_id": sid, "date": b.date})
    d = pd.DataFrame(rows)
    agg = (d.groupby(["from", "to"])["days"]
             .agg(n="size", p10=lambda s: s.quantile(.10),
                  median="median", p90=lambda s: s.quantile(.90))
             .reset_index())
    agg["standard"] = [B0_DAYS.get((f, t)) for f, t in
                       zip(agg["from"], agg["to"])]
    agg["diff"] = agg["median"] - agg["standard"]
    return agg.sort_values("n", ascending=False), d


def predict_days(pairs: pd.DataFrame) -> dict:
    """다음 사건까지 며칠인가 — 표준 캘린더 대비.

    B0 표준 캘린더(문헌 상수)   ← **기준선**. 이걸 못 이기면 로그는 값이 없다
    B1 농장 전체 중앙값(학습분)
    B2 그 개체의 과거 중앙값(없으면 B1 로 물러선다)
    """
    d = pairs.dropna(subset=["days"]).copy()
    d = d[[(f, t) in B0_DAYS for f, t in zip(d["from"], d["to"])]]
    if not len(d):
        return {}
    cut = d["date"].quantile(CUT_Q)
    tr, te = d[d["date"] <= cut], d[d["date"] > cut]
    out = {"cut_date": str(cut), "n_train": int(len(tr)), "n_test": int(len(te))}
    if len(te) < MIN_OBS:
        out["skipped"] = f"평가 표본 {len(te)} < {MIN_OBS} — 예측하지 않는다"
        return out

    med = tr.groupby(["from", "to"])["days"].median().to_dict()
    per = tr.groupby(["animal_id", "from", "to"])["days"].median().to_dict()
    n_per = tr.groupby(["animal_id", "from", "to"])["days"].size().to_dict()

    def b0(r):
        return B0_DAYS[(r["from"], r["to"])]

    def b1(r):
        return med.get((r["from"], r["to"]), b0(r))

    def b2(r):
        k = (r["animal_id"], r["from"], r["to"])
        # 그 개체 기록이 1건뿐이면 개체 평균이 아니라 그날의 사고다
        return per[k] if n_per.get(k, 0) >= 2 else b1(r)

    res = {}
    for name, fn in (("B0 표준 캘린더", b0), ("B1 농장 중앙값", b1),
                     ("B2 개체 과거", b2)):
        p = te.apply(fn, axis=1).to_numpy(float)
        e = te["days"].to_numpy(float) - p
        res[name] = {"mae": round(float(np.mean(np.abs(e))), 3),
                     "hit": round(float(np.mean(np.abs(e) <= HIT_DAYS)), 3)}
    base = res["B0 표준 캘린더"]["mae"]
    for k in res:
        res[k]["gain_vs_B0"] = round((base - res[k]["mae"]) / max(1e-9, base), 4)
    out["scores"] = res
    out["by_transition"] = {
        f"{f}→{t}": {"n": int(len(g)),
                     "mae_B0": round(float(np.mean(np.abs(
                         g["days"] - B0_DAYS[(f, t)]))), 2),
                     "mae_B1": round(float(np.mean(np.abs(
                         g["days"] - med.get((f, t), B0_DAYS[(f, t)])))), 2)}
        for (f, t), g in te.groupby(["from", "to"])}
    return out


def _outcome_frame(cycles: pd.DataFrame) -> pd.DataFrame:
    """교배 시점에 **그때까지 알 수 있는 것만** 으로 만든 피처.

    결과(분만/재발)를 알고 만든 피처를 넣으면 그 자리에서 예측이 아니게 된다.
    그래서 이 함수는 `farrow`·`weaned` 같은 사후 열을 쓰지 않는다.
    """
    d = cycles.sort_values(["sow_id", "service"]).reset_index(drop=True)
    d["y"] = (d["outcome"] == "분만").astype(int)
    d["month"] = pd.to_datetime(d["service"]).dt.month
    d["wei"] = [(s - w).days if w is not None else np.nan
                for s, w in zip(d["service"], d["wean_prev"])]
    d["est_gap"] = [(s - e).days for s, e in zip(d["service"], d["estrus"])]
    # 그 개체가 **이번 교배 전까지** 겪은 재발 횟수 — 미래를 안 본다
    d["prior_returns"] = (d.groupby("sow_id")["y"]
                            .apply(lambda s: (1 - s).shift(1).cumsum())
                            .reset_index(level=0, drop=True).fillna(0))
    d["prior_cycles"] = d.groupby("sow_id").cumcount()
    return d


def predict_outcome(cycles: pd.DataFrame) -> dict:
    """이번 교배가 **분만으로 갈까 재발로 갈까**.

    기준선은 다수 클래스(전부 분만이라고 찍기)다. 분만율이 8할이라 정확도만
    보면 그것만으로 0.8 이 나온다 — 그래서 `ml_core` 로 정확도와 Macro-F1 을
    **함께** 본다. 이 프로젝트가 자세 5클래스에서 겪은 함정과 같다.
    """
    from sklearn.ensemble import HistGradientBoostingClassifier

    d = _outcome_frame(cycles)
    feats = ["parity", "month", "wei", "est_gap", "prior_returns", "prior_cycles"]
    d = d.dropna(subset=["wei"])
    if len(d) < MIN_OBS * 4:
        return {"skipped": f"표본 {len(d)} 로는 판정하지 않는다"}

    cut = pd.Series(d["service"]).quantile(CUT_Q)
    out = {"cut_date": str(cut), "n": int(len(d))}

    def run(tr, te, tag):
        if len(te) < MIN_OBS or tr["y"].nunique() < 2:
            return {"skipped": f"평가 {len(te)}건"}
        m = HistGradientBoostingClassifier(max_iter=200, max_depth=3,
                                           learning_rate=0.06, random_state=0)
        m.fit(tr[feats], tr["y"])
        pred = m.predict(te[feats])
        maj = int(tr["y"].mode().iloc[0])
        model = ml_core.score(te["y"], pred)
        base = ml_core.score(te["y"], np.full(len(te), maj))
        v = ml_core.report(tag, model, base, quiet=True)
        return {"n_train": int(len(tr)), "n_test": int(len(te)),
                "model": model, "baseline": base, "verdict": v["verdict"]}

    tr = d[d["service"] <= cut]
    te = d[d["service"] > cut]
    out["time_split"] = run(tr, te, "시간 순 분할")
    out["shared_animals"] = int(len(set(tr["sow_id"]) & set(te["sow_id"])))

    # 개체 단위 분할을 **나란히** 낸다. 시간 분할이 훨씬 좋으면 개체를 외운 것
    ids = sorted(d["sow_id"].unique())
    hold = set(ids[::4])
    out["group_split"] = run(d[~d["sow_id"].isin(hold)],
                             d[d["sow_id"].isin(hold)], "개체 단위 분할")
    return out


def recovery(ev: pd.DataFrame, cycles: pd.DataFrame, params) -> dict:
    """**넣은 값을 로그만 보고 되찾는가.** 경로 복원이 맞는지의 진짜 검증.

    합성 로그의 정확도는 농장 성적이 아니지만, 주입한 모수를 사건 나열에서
    되찾는 것은 진짜 확인이다. 못 되찾으면 `to_events` 나 `transitions` 가
    틀린 것이고, 그 위에 얹은 예측은 볼 필요도 없다.
    """
    _, pairs = transitions(ev)

    def stat(f, t):
        s = pairs[(pairs["from"] == f) & (pairs["to"] == t)]["days"]
        if not len(s):
            return float("nan"), float("nan"), 0
        return float(s.mean()), float(s.median()), int(len(s))

    def row(inj, f, t):
        m, md, n = stat(f, t)
        return {"injected": round(float(inj), 2), "recovered": round(m, 2),
                "median": round(md, 1), "n": n,
                "ok": abs(m - inj) <= TOL_DAYS}

    got = float((cycles["outcome"] == "분만").mean())
    return {
        # 주입값은 (중앙, p25, p75) 튜플이고 되찾는 건 이유→발정확인 하나다.
        # 발정확인→교배 는 적기 간격이라 WEI 에 더하면 안 된다.
        #
        # **중앙값이 아니라 평균으로 잰다.** 로그는 날짜 단위라 6.9 일 같은
        # 소수 중앙값이 나올 수 없다 — 중앙값으로 재면 6.0 이 찍히고 멀쩡한
        # 복원을 실패로 판정한다. 평균은 남는다.
        "wei": row(params.wean_to_estrus[0], "이유", "발정확인"),
        "gestation": row(params.gestation, "교배", "분만"),
        "lactation": row(params.lactation, "분만", "이유"),
        "farrowing_rate": {"injected": round(float(params.farrowing_rate), 4),
                           "recovered": round(got, 4), "median": None,
                           "n": int(len(cycles)),
                           "ok": abs(got - params.farrowing_rate) <= 0.02},
    }


def run(n_sows: int = 300, years: float = 3.0, seed: int = 0) -> dict:
    P = sf.Params()
    cycles = sf.generate(n_sows=n_sows, years=years, seed=seed, params=P)
    ev = to_events(cycles)
    j = journeys(ev)
    agg, pairs = transitions(ev)
    return {
        "source": "합성(synth_farm) — 실농장 로그 아님",
        "params_source": getattr(P, "source", "?"),
        "n_animals": int(ev["animal_id"].nunique()),
        "n_events": int(len(ev)),
        "n_cycles": int(ev["cycle"].nunique()),
        "events_per_animal": round(float(j["n_events"].mean()), 1),
        "variants": variants(ev).to_dict("records"),
        "transitions": agg.to_dict("records"),
        "recovery": recovery(ev, cycles, P),
        "days": predict_days(pairs),
        "outcome": predict_outcome(cycles),
    }


def _print(r: dict) -> None:
    print("=" * 78)
    print(f"  로그 기반 경로·예측 — 개체 {r['n_animals']} · 사건 "
          f"{r['n_events']:,} · 사이클 {r['n_cycles']:,}")
    print("=" * 78)
    print(f"  출처: {r['source']} (모수 {r['params_source']})")

    print(f"\n  [경로 되찾기] 생성기에 넣은 값을 로그만 보고 되찾는가")
    print(f"    {'':<2}{'':<16}{'주입':>8}{'되찾음(평균)':>14}{'중앙':>7}{'n':>7}")
    for k, v in r["recovery"].items():
        ok = "✅" if v["ok"] else "❌"
        md = "—" if v["median"] is None else f"{v['median']:.1f}"
        print(f"    {ok} {k:<16}{v['injected']:>8}{v['recovered']:>14}"
              f"{md:>7}{v['n']:>7}")
    print(f"    날짜가 일 단위라 소수 중앙값은 복원되지 않는다 — 평균으로 잰다"
          f"(허용 {TOL_DAYS}일).")

    print(f"\n  [경로 변형] 한 사이클 안에서 실제로 밟힌 길")
    print(f"    {'':<2}{'경로':<44}{'건수':>7}{'비율':>7}{'중앙일':>7}")
    for v in r["variants"]:
        mark = "표준" if v["standard"] else "  "
        print(f"    {mark:<2}{v['path'][:43]:<44}{v['n']:>7}"
              f"{v['share']:>7.1%}{v['median_days']:>7.0f}")

    print(f"\n  [전이별 실제 간격] 이 농장 값 vs 표준 상수")
    print(f"    {'전이':<22}{'n':>7}{'p10':>6}{'중앙':>6}{'p90':>6}{'표준':>6}{'차이':>7}")
    for t in r["transitions"]:
        # 표준 상수가 없는 전이(재발정→이유 등)는 대조 대상이 아니다.
        # DataFrame 을 거치면 None 이 NaN 이 되므로 그것도 걸러야 한다.
        if t["standard"] is None or t["standard"] != t["standard"]:
            continue
        print(f"    {t['from'] + '→' + t['to']:<22}{t['n']:>7}{t['p10']:>6.0f}"
              f"{t['median']:>6.0f}{t['p90']:>6.0f}{t['standard']:>6.0f}"
              f"{t['diff']:>+7.1f}")

    d = r["days"]
    print(f"\n  [다음 사건 날짜 예측] 시간 순 분할 · 학습 {d.get('n_train', 0):,} "
          f"→ 평가 {d.get('n_test', 0):,}")
    if d.get("skipped"):
        print(f"    건너뜀 — {d['skipped']}")
    else:
        print(f"    {'모델':<18}{'MAE(일)':>9}{'±2일 적중':>10}{'B0 대비':>9}")
        for k, v in d["scores"].items():
            mark = "  ←기준선" if k.startswith("B0") else ""
            print(f"    {k:<18}{v['mae']:>9.2f}{v['hit']:>10.1%}"
                  f"{v['gain_vs_B0']:>+9.1%}{mark}")
        print(f"\n    전이별 (B0 표준 → B1 농장값)")
        for k, v in d["by_transition"].items():
            print(f"      {k:<20}n {v['n']:>5}   {v['mae_B0']:>6.2f} → "
                  f"{v['mae_B1']:>6.2f}")

    o = r["outcome"]
    print(f"\n  [분만 vs 재발 예측]")
    if o.get("skipped"):
        print(f"    건너뜀 — {o['skipped']}")
    else:
        for key, title in (("time_split", "시간 순 분할"),
                           ("group_split", "개체 단위 분할")):
            s = o.get(key) or {}
            if s.get("skipped"):
                print(f"    {title}: 건너뜀 — {s['skipped']}")
                continue
            m, b = s["model"], s["baseline"]
            print(f"    {title:<12} acc {m['acc']:.3f} / MF1 {m['mf1']:.3f}"
                  f"   기준선 {b['acc']:.3f} / {b['mf1']:.3f}   → {s['verdict']}")
        print(f"    (시간 분할에서 양쪽에 겹친 개체 {o['shared_animals']}두 — "
              f"현장에서도 그 모돈의 과거는 알고 예측한다)")


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(prog="path_predict")
    ap.add_argument("--sows", type=int, default=300)
    ap.add_argument("--years", type=float, default=3.0)
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--out", default=None)
    a = ap.parse_args(argv)
    r = run(a.sows, a.years, a.seed)
    _print(r)
    if a.out:
        json.dump(r, open(a.out, "w", encoding="utf-8"),
                  ensure_ascii=False, indent=1, default=str)
        print(f"\n저장: {a.out}")
    print("\n※ 로그가 합성이라 위 정확도는 농장 성적이 아니라 **장치 확인**이다.")
    print("  실농장 로그가 들어오면 같은 함수가 그 농장 간격·재발률로 다시 돈다.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
