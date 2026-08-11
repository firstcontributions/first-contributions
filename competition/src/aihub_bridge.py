"""AI Hub 71471 실데이터 → 운영 모듈 연결.

이 프로젝트의 운영 모듈들은 하나같이 "합성 데이터 시연이다. 실제로는 농장
기록을 그대로 넣으면 같은 화면이 나온다"고 적어 뒀다. 이 모듈은 그 주장을
**실제 데이터로 검증**한다 — AI Hub 71471 [Bbox] 를 읽어 축사 구조와 관측
시계열을 만들고 그대로 모듈에 흘려보낸다.

다만 **AI Hub 가 줄 수 있는 것과 없는 것을 섞지 않는다.** 실측으로 확인된 것:

  ✅ 줄 수 있다
     · 축사 구조   — 농장 1곳 × 채널(돈방) 16개
     · 관측 시계열 — 돈방별 자세 구성(눕기/서기/기좌/섭식), 재실 두수
     · bbox 기하   — 탐지·자세 파이프라인 입력

  ❌ 줄 수 없다
     · **개체 식별** — 프레임 간 추적 ID 가 없다. 같은 돼지를 이어붙일 수
       없으므로 개체카드·개체별 일정은 만들 수 없다(돈방 단위가 한계).
     · **번식 기록** — 교배·분만·이유일이 없다. 캘린더·배치·현황판은 농장
       전산기록(한돈팜스 등)이 따로 있어야 돈다.
     · **발정 정답** — ESTRUS 필드가 있지만 **16/16 채널이 순수**하다
       (ch1~8 전부 Y, ch9~16 전부 N). 개체가 아니라 카메라에 붙은 라벨이고,
       Y/N 의 행동 분포도 사실상 같다(눕기 83.3% vs 83.7%). 이 라벨로 학습하면
       카메라를 외울 뿐이므로 **정답으로 쓰지 않는다**.

그래서 연동의 결론은 이렇다: AI Hub 는 **관측 계층**을 채우고, 번식 계층은
농장 기록이 채운다. 둘을 합쳐야 앱이 완성되며, 이 모듈은 그 경계를 코드로
명시한다.

    python competition/src/aihub_bridge.py            # 연동 + 능력 매트릭스
    AIHUB_71471_DIR=/path python competition/src/aihub_bridge.py
"""
from __future__ import annotations

import glob
import json
import os
import sys
from collections import Counter

import numpy as np
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, HERE)
import aihub_estrus_reference as ref  # noqa: E402
import farm_registry as fr  # noqa: E402

# 실데이터가 놓인 곳(환경변수로 덮어쓸 수 있다)
DEFAULT_DIRS = ["/tmp/a71471b", "/tmp/aihub71471",
                os.path.join(ROOT, "competition", "data", "aihub71471")]

# 71471 ACTION_NAME → 자세 3분류(stall_estrus 어휘와 맞춘다)
ACTION_TO_POSTURE = {
    "lying": "lying", "sitting": "sitting", "standing": "standing",
    "eating": "standing",     # 섭식은 서 있는 자세다
}


def data_dirs() -> list:
    env = os.environ.get("AIHUB_71471_DIR")
    dirs = ([env] if env else []) + DEFAULT_DIRS
    return [d for d in dirs if d and os.path.isdir(d)]


def load_frames(dirs: list | None = None, verbose: bool = False) -> pd.DataFrame:
    """71471 [Bbox] JSON → 정규화된 bbox 테이블.

    파일 하나가 프레임 하나이고 그 안에 개체 bbox 가 여럿이다. 파일명이
    `농장_채널_yyyymmddHH_세션_타임스탬프` 구조라 시간·돈방을 여기서 얻는다.
    """
    dirs = dirs or data_dirs()
    seen, rows, broken = set(), [], 0
    for d in dirs:
        for f in sorted(glob.glob(os.path.join(d, "*.json"))):
            name = os.path.basename(f)[:-5]
            if name in seen:
                continue
            seen.add(name)
            try:
                j = json.load(open(f, encoding="utf-8"))
            except Exception:
                # 다운로드 중 잘린 파일이 섞인다. 조용히 건너뛰지 말고 센다 —
                # 몇 건인지 모르면 결과가 얼마나 부실한지 판단할 수 없다.
                broken += 1
                continue
            im = j.get("IMAGE", {})
            parts = name.split("_")
            if len(parts) < 5:
                continue
            farm, ch, stamp, sess, ts = parts[0], parts[1], parts[2], parts[3], parts[4]
            for a in j.get("ANNOTATION_INFO", []):
                act = a.get("ACTION_NAME")
                rows.append({
                    "frame": name, "farm": farm, "pen": ch,
                    "date": stamp[:8], "hour": int(stamp[8:10]),
                    "session": sess, "ts": int(ts),
                    "w_img": im.get("WIDTH"), "h_img": im.get("HEIGHT"),
                    "x": a.get("BOUNDING_BOX_X_COORDINATE"),
                    "y": a.get("BOUNDING_BOX_Y_COORDINATE"),
                    "w": a.get("BOUNDING_BOX_WIDTH"),
                    "h": a.get("BOUNDING_BOX_HEIGHT"),
                    "action": act,
                    "posture": ACTION_TO_POSTURE.get(act, "other"),
                    "estrus_label": a.get("ESTRUS"),
                })
    df = pd.DataFrame(rows)
    df.attrs["broken_files"] = broken
    df.attrs["n_frames"] = len(seen) - broken
    # 폭·높이가 0 인 박스가 섞여 있다(실측 1건/12,805). 학습에 들어가면 안 되는
    # 값이므로 조용히 통과시키지 말고 세어서 드러낸다. 버리지는 않는다 —
    # 원본을 그대로 두고 소비 측이 valid_boxes() 로 거르게 한다.
    if len(df):
        df.attrs["degenerate_boxes"] = int(((df["w"] <= 0) | (df["h"] <= 0)).sum())
    if verbose:
        print(f"  프레임 {df.attrs['n_frames']:,} · bbox {len(df):,} · "
              f"깨진 파일 {broken} · 폭/높이 0 인 박스 "
              f"{df.attrs.get('degenerate_boxes', 0)}")
    return df


def valid_boxes(df: pd.DataFrame) -> pd.DataFrame:
    """학습·분석에 쓸 수 있는 박스만. 폭·높이 0 은 뺀다."""
    if not len(df):
        return df
    out = df[(df["w"] > 0) & (df["h"] > 0)].copy()
    out.attrs.update(df.attrs)
    out.attrs["dropped"] = len(df) - len(out)
    return out


def label_audit(df: pd.DataFrame) -> dict:
    """ESTRUS 라벨이 개체 라벨인지 카메라 라벨인지 판정.

    돈방마다 Y 비율이 0 또는 1 이면(순수) 그 라벨은 개체가 아니라 카메라에
    붙은 것이다. 이걸 먼저 확인하지 않고 학습하면 카메라를 외운다.
    """
    if not len(df) or df["estrus_label"].isna().all():
        return {"has_label": False}
    per = df.groupby("pen")["estrus_label"].apply(lambda s: (s == "Y").mean())
    pure = int(((per == 0) | (per == 1)).sum())
    # Y/N 간 행동 분포 차이(총변동거리) — 라벨이 행동을 설명하는가.
    # groupby.apply 체인으로 만들면 인덱스 모양이 판마다 달라져 조용히 None 이
    # 되므로, 두 분포를 따로 뽑아 명시적으로 정렬해 뺀다.
    tvd = None
    if {"Y", "N"} <= set(df["estrus_label"].dropna().unique()):
        py = df[df["estrus_label"] == "Y"]["posture"].value_counts(normalize=True)
        pn = df[df["estrus_label"] == "N"]["posture"].value_counts(normalize=True)
        idx = sorted(set(py.index) | set(pn.index))
        tvd = float(0.5 * sum(abs(py.get(k, 0.0) - pn.get(k, 0.0)) for k in idx))
    return {"has_label": True, "n_pens": int(len(per)), "pure_pens": pure,
            "confounded": pure == len(per),
            "y_rate": round(float((df["estrus_label"] == "Y").mean()), 3),
            "behaviour_tvd": round(tvd, 4) if tvd is not None else None,
            "per_pen": per.round(3).to_dict()}


def build_farm(df: pd.DataFrame, name: str = "AI Hub pigfarmA") -> fr.Farm:
    """관측된 채널 구조 → Farm 객체.

    채널 하나가 돈방 하나다. 71471 은 군사 사육 영상이므로 housing="group",
    수용능력은 그 돈방에서 관측된 최대 두수로 잡는다(실측 상한).
    개체 ID 가 없으므로 **자리 배치는 하지 않는다** — 있지도 않은 개체를
    만들어 넣으면 이후 화면이 전부 거짓이 된다.
    """
    farm = fr.Farm(name)
    farm.add_barn("1동", "임신사", "AI Hub 71471 관측 — 군사 돈방")
    cap = df.groupby(["pen", "frame"]).size().groupby("pen").max()
    for pen in sorted(cap.index, key=lambda p: int(p[2:])):
        farm.add_pen("1동", pen, "group", int(cap[pen]),
                     note=f"관측 최대 {int(cap[pen])}두")
    return farm


def pen_sessions(df: pd.DataFrame) -> pd.DataFrame:
    """돈방 × 날짜 × 시간 단위 관측 요약 — 자세 구성과 재실 두수."""
    if not len(df):
        return pd.DataFrame()
    g = df.groupby(["pen", "date", "hour"])
    rows = []
    for (pen, date, hour), sub in g:
        n_frames = sub["frame"].nunique()
        comp = sub["posture"].value_counts(normalize=True)
        rows.append({
            "pen": pen, "date": date, "hour": hour,
            "n_frames": n_frames, "n_bbox": len(sub),
            "headcount": round(len(sub) / max(1, n_frames), 1),
            "standing": round(float(comp.get("standing", 0.0)), 3),
            "sitting": round(float(comp.get("sitting", 0.0)), 3),
            "lying": round(float(comp.get("lying", 0.0)), 3),
            "eating": round(float((sub["action"] == "eating").mean()), 3),
        })
    return pd.DataFrame(rows).sort_values(["pen", "date", "hour"])


def pen_estrus_scores(sessions: pd.DataFrame) -> pd.DataFrame:
    """돈방별 발정 지표 — 71471 표준 가중치를 실측 자세 구성에 적용.

    **개체 점수가 아니라 돈방 점수다.** 추적 ID 가 없어 개체를 이어붙일 수
    없기 때문이며, 이 한계를 숨기면 개체카드가 거짓이 된다. 그리고 이 점수는
    정답과 대조할 수 없다 — ESTRUS 라벨이 카메라 교락이라 검증에 못 쓴다.
    """
    R = ref.EstrusReference()
    if not len(sessions):
        return pd.DataFrame()
    rows = []
    for pen, sub in sessions.groupby("pen"):
        frac = {"standing": float(sub["standing"].mean()),
                "sitting": float(sub["sitting"].mean()),
                "lying": float(sub["lying"].mean()),
                "eating": float(sub["eating"].mean())}
        # 활동량 대체값: 기립 비율의 시간대별 변동(추적이 없어 이동거리는 불가).
        # 세션이 1개뿐인 돈방은 표본표준편차가 NaN 이 되고, 그러면 점수까지
        # NaN 이 되어 **순위에서 조용히 빠진다**(실측 ch2~ch5 가 그랬다).
        # ddof=0 으로 계산하고 NaN 은 0 으로 둔다 — 변동을 관측하지 못한 것이지
        # 활동이 없다는 뜻은 아니므로, n_sessions 를 함께 내어 추정이 얇음을 알린다.
        sd = sub["standing"].std(ddof=0)
        act = 0.0 if sd != sd else float(np.clip(sd * 4.0, 0, 1))
        rows.append({"pen": pen, "n_sessions": int(len(sub)),
                     "headcount": round(float(sub["headcount"].mean()), 1),
                     **{k: round(v, 3) for k, v in frac.items()},
                     "activity_proxy": round(act, 3),
                     "estrus_score": round(R.score(frac, act), 3)})
    d = pd.DataFrame(rows)
    return d.sort_values("estrus_score", ascending=False).reset_index(drop=True)


CAPABILITY = [
    ("축사 구조(동·돈방)", "farm_registry", True,
     "채널 16개 → 돈방 16개. 수용능력은 관측 최대 두수"),
    ("재실 두수", "barn_map · herd_board", True, "프레임당 bbox 수"),
    ("자세 구성 시계열", "stall_estrus · 활동 분석", True,
     "눕기/서기/기좌/섭식 비율(돈방·시간 단위)"),
    ("bbox 기하", "탐지·자세 파이프라인", True, None),   # 실제 수는 런타임에
    ("개체 식별", "모돈카드 · 개체 일정", False,
     "추적 ID 없음 — 프레임 간 같은 돼지를 이어붙일 수 없다"),
    ("번식 기록(교배·분만·이유)", "repro_calendar · batch_flow · herd_board",
     False, "데이터에 없음 — 농장 전산기록 필요"),
    ("발정 정답", "모델 학습·검증", False,
     "ESTRUS 가 카메라 교락(16/16 순수) — 정답으로 쓸 수 없다"),
]


def main() -> int:
    dirs = data_dirs()
    print("=== AI Hub 71471 [Bbox] 연동 ===")
    if not dirs:
        print("  데이터를 찾지 못했다. AIHUB_71471_DIR 로 경로를 지정하거나")
        print(f"  {DEFAULT_DIRS[-1]} 에 JSON 을 두면 된다.")
        print("  (국내 IP 전용 다운로드 — 이 환경에서는 내려받을 수 없다)")
        return 0
    print(f"  경로: {', '.join(dirs)}")
    df = load_frames(dirs, verbose=True)
    if not len(df):
        print("  파싱된 bbox 가 없다.")
        return 0
    print(f"  농장 {df['farm'].nunique()} · 돈방 {df['pen'].nunique()} · "
          f"날짜 {df['date'].nunique()} · 시간대 {df['hour'].nunique()}")

    print("\n=== 먼저 라벨 감사 — 쓸 수 있는 정답인가 ===")
    aud = label_audit(df)
    print(f"  ESTRUS Y 비율 {aud['y_rate']:.1%} · "
          f"순수 돈방 {aud['pure_pens']}/{aud['n_pens']}")
    if aud["confounded"]:
        print("  ⚠ **모든 돈방이 순수하다** — ESTRUS 는 개체가 아니라 카메라에")
        print("    붙은 라벨이다. 이걸로 학습하면 카메라를 외울 뿐이다.")
    print(f"  Y/N 간 자세 분포 차이(TVD) {aud['behaviour_tvd']:.4f} "
          f"— 0 에 가까울수록 행동으로 구분 불가")
    print("  → 정답으로 쓰지 않는다. 관측 계층만 가져다 쓴다.")

    farm = build_farm(df)
    occ = farm.occupancy()
    print(f"\n=== 축사 구조 생성 (farm_registry) ===")
    print(f"  {farm.name} · 동 {len(farm.barns)} · 돈방 {len(farm.pens)}")
    print(f"  {'돈방':>6} {'수용(관측 최대)':>14}")
    for r in occ.head(6).itertuples(index=False):
        print(f"  {r.pen:>6} {r.capacity:>10}두")
    print(f"  … 외 {max(0, len(occ) - 6)}개 돈방")
    print("  ※ 개체 ID 가 없어 **자리 배치는 하지 않았다**. 없는 개체를 만들어"
          "\n    넣으면 이후 화면이 전부 거짓이 된다.")

    ses = pen_sessions(df)
    print(f"\n=== 관측 시계열 (돈방 × 날짜 × 시간) {len(ses):,}건 ===")
    print(f"  {'돈방':>6} {'세션':>4} {'재실':>5} {'눕기':>6} {'서기':>6} "
          f"{'기좌':>6} {'섭식':>6}")
    for r in ses.groupby("pen").agg(
            n=("n_frames", "size"), hc=("headcount", "mean"),
            ly=("lying", "mean"), st=("standing", "mean"),
            si=("sitting", "mean"), ea=("eating", "mean")
    ).head(6).reset_index().itertuples(index=False):
        print(f"  {r.pen:>6} {r.n:>4} {r.hc:>5.1f} {r.ly:>6.1%} "
              f"{r.st:>6.1%} {r.si:>6.1%} {r.ea:>6.1%}")

    sc = pen_estrus_scores(ses)
    print(f"\n=== 돈방별 발정 지표 (71471 표준 가중치 적용) ===")
    print(f"  {'돈방':>6} {'세션':>4} {'재실':>5} {'눕기':>6} {'서기':>6} {'점수':>7}")
    for r in sc.head(6).itertuples(index=False):
        thin = " (세션 1개 — 추정 얇음)" if r.n_sessions <= 1 else ""
        print(f"  {r.pen:>6} {r.n_sessions:>4} {r.headcount:>5.1f} "
              f"{r.lying:>6.1%} {r.standing:>6.1%} {r.estrus_score:>7.3f}{thin}")
    thin_n = int((sc["n_sessions"] <= 1).sum())
    if thin_n:
        print(f"  ※ 세션이 1개뿐인 돈방 {thin_n}개는 시간 변동을 관측할 수 없어")
        print("    활동 지표가 0 이다. 활동이 없다는 뜻이 아니라 못 쟀다는 뜻이다.")
    print("  ※ **돈방 점수이지 개체 점수가 아니다**(추적 ID 없음).")
    print("  ※ 정답과 대조할 수 없다 — 위 라벨 감사대로 ESTRUS 가 교락이다.")

    print("\n=== 연동 능력 매트릭스 ===")
    print(f"  {'항목':<22} {'연결 대상':<34} 가능")
    for item, target, ok, note in CAPABILITY:
        # bbox 수는 하드코딩하면 안 된다. 두 디렉터리에 같은 파일이 겹쳐 있어
        # 중복을 세면 13,916 이 나오지만 실제 고유 bbox 는 그보다 적다.
        txt = note if note else f"{len(df):,} bbox · 프레임 {df.attrs['n_frames']:,}"
        print(f"  {item:<22} {target:<34} {'✅' if ok else '❌'}  {txt}")
    n_ok = sum(1 for _i, _t, ok, _n in CAPABILITY if ok)
    print(f"\n  → {n_ok}/{len(CAPABILITY)} 항목 연결. AI Hub 는 **관측 계층**을"
          "\n    채우고, 번식 계층(교배·분만·이유)은 농장 전산기록이 채운다."
          "\n    둘을 합쳐야 앱이 완성되며 어느 한쪽만으로는 안 된다.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
