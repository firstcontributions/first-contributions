"""학습·평가 공통 규약 — 이 프로젝트가 **비싸게 배운 것**을 코드로 굳힌다.

새 규약이 아니다. posture_crossview·model_behavior_appearance 가 이미 쓰던
방식을 한군데로 모아, 앞으로 만들 모델이 같은 실수를 되풀이하지 않게 한다.
딥러닝을 얹어도 이 규약은 그대로다 — 오히려 표현력이 커질수록 아래 함정이
깊어진다.

## 굳혀 둔 실수 넷

1. **기준선을 먼저 찍는다.** 기하 전용 모델 5클래스 0.414 인데 다수 클래스만
   찍어도 0.423 이었다. 기준선 없이 보면 개선처럼 읽힌다. 그래서 `report()`
   는 기준선을 **먼저** 출력하고, 모델이 그 아래면 실패로 표시한다.
2. **정확도만 보지 않는다.** 클래스가 치우치면 정확도가 신호를 가린다.
   위 사례에서 판별력은 Macro-F1 에서만 드러났다(0.119 → 0.228).
3. **그룹 누수를 막는다.** train1/train2 가 이미지 3,090장을 공유해 0.642 가
   나왔고, 못 본 카메라로 재면 0.4 대였다. `leakage_check()` 로 분할 전에
   막는다.
4. **폴드가 작으면 보고하지 않는다.** 스톨 24개·시드 5회로 쟀다가 순서가
   뒤집혔다(정확도 낮은 쪽이 AUC 높게 나옴). `MIN_FOLD` 미만 폴드는 뺀다.

## 왜 정확도를 폴드 크기로 가중하나

폴드마다 표본 수가 크게 다르다(자세 뷰별 LOVO 는 폴드 정확도가 0.356~0.770
로 흩어진다). 단순 평균은 작은 폴드에 끌려가므로 n 가중 평균을 쓴다.

    python competition/src/ml_core.py     # 지금 학습 가능한 과제 점검
"""
from __future__ import annotations

import os
from dataclasses import dataclass, field

import numpy as np
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)                       # .../competition

# 이보다 작은 폴드는 분산에 묻혀 순서가 뒤집힌다 — 집계에서 뺀다.
MIN_FOLD = 30
# 모델이 기준선을 이 폭 안쪽으로만 이기면 "이겼다" 고 하지 않는다.
MARGIN = 0.005


# -- 지표 -----------------------------------------------------------------
def score(y_true, y_pred) -> dict:
    """정확도 + Macro-F1. **둘을 항상 같이 낸다.**"""
    from sklearn.metrics import accuracy_score, f1_score
    return {"acc": float(accuracy_score(y_true, y_pred)),
            "mf1": float(f1_score(y_true, y_pred, average="macro",
                                  zero_division=0)),
            "n": int(len(y_true))}


def weighted(rows: list) -> dict:
    """폴드별 결과를 **표본 수로 가중**해 합친다."""
    if not rows:
        return {"acc": float("nan"), "mf1": float("nan"), "n": 0, "folds": 0}
    r = pd.DataFrame(rows)
    w = r["n"] / r["n"].sum()
    return {"acc": round(float((r["acc"] * w).sum()), 3),
            "mf1": round(float((r["mf1"] * w).sum()), 3),
            "n": int(r["n"].sum()), "folds": int(len(r)),
            "acc_min": round(float(r["acc"].min()), 3),
            "acc_max": round(float(r["acc"].max()), 3)}


# -- 분할 -----------------------------------------------------------------
def leakage_check(df: pd.DataFrame, group: str,
                  id_col: str | None = None) -> dict:
    """같은 이미지·개체가 두 그룹에 걸쳐 있는지. **분할 전에 부른다.**

    train1↔train2 가 이미지 3,090장을 공유하는 걸 못 보고 0.642 를 보고했다.
    그룹으로 나눠도 식별자가 그룹을 넘나들면 누수다.

    **id_col 은 전역 고유 식별자여야 한다.** 파일 경로처럼 행마다 다른 값을
    준다. 그룹마다 0 부터 다시 매겨지는 카운터(`frame_idx` 같은)를 주면
    전부 "누수" 로 나온다 — 실제로 그렇게 불렀다가 600건이 찍혔다. 그래서
    고유성을 먼저 재고, 아니면 세지 않고 경고만 낸다.
    """
    out = {"group": group, "n_groups": int(df[group].nunique()),
           "leaked": 0, "examples": [], "checked": False}
    if not id_col or id_col not in df.columns:
        out["note"] = "id_col 미지정 — 그룹 분할만으로는 누수를 보장 못 한다"
        return out
    spans = df.groupby(id_col)[group].nunique()
    crossing = spans[spans > 1]
    frac = len(crossing) / max(1, len(spans))
    # 진짜 누수는 **일부** 식별자만 그룹을 넘는다. 거의 전부가 넘으면 그건
    # 식별자가 아니라 그룹마다 0 부터 다시 매겨지는 카운터다 —
    # frame_idx 를 넘겼다가 600건이 '누수' 로 찍힌 적이 있다.
    if frac > 0.5:
        out["note"] = (f"'{id_col}' 의 {frac:.0%} 가 그룹을 넘는다 — 식별자가 "
                       f"아니라 그룹별 카운터로 보인다. 전역 고유한 값"
                       f"(파일 경로 등)을 줄 것. 검사 생략")
        return out
    out["checked"] = True
    out["leaked"] = int(len(crossing))
    out["examples"] = [str(x) for x in crossing.index[:5]]
    return out


def leave_one_group_out(df: pd.DataFrame, label: str, group: str,
                        fit_predict, min_fold: int = MIN_FOLD) -> dict:
    """그룹 하나를 통째로 빼고 학습 — 못 본 카메라/돈방/개체로 검증.

    fit_predict(train_df, test_df) -> 예측 배열. 모델 종류를 안 가리므로
    사이킷런이든 토치든 같은 규약으로 잰다.
    """
    vs = df[group].value_counts()
    use = [v for v in sorted(vs.index) if vs[v] >= min_fold]
    rows, skipped = [], [v for v in sorted(vs.index) if vs[v] < min_fold]
    for v in use:
        m = df[group].to_numpy() == v
        tr, te = df.loc[~m], df.loc[m]
        if tr[label].nunique() < 2:
            skipped.append(v)
            continue
        rows.append(score(te[label], fit_predict(tr, te)))
    out = weighted(rows)
    out["skipped"] = [str(s) for s in skipped]
    out["min_fold"] = min_fold
    return out


def group_kfold(df: pd.DataFrame, label: str, group: str, fit_predict,
                k: int = 5, seed: int = 0) -> dict:
    """그룹을 k 덩어리로 나눠 검증 — 그룹이 많아 LOVO 가 과한 경우.

    개체 96마리를 LOVO 로 돌리면 폴드마다 표본이 수십 개라 분산에 묻힌다
    (`MIN_FOLD` 에서 대부분 잘려 나간다). 기존 행동 모델이 쓰던
    GroupKFold(5) 와 같은 규약이다. **그룹은 통째로 한 폴드에만 들어간다.**
    """
    from sklearn.model_selection import GroupKFold
    g = df[group].to_numpy()
    rows = []
    for tr_i, te_i in GroupKFold(n_splits=k).split(df, df[label], g):
        tr, te = df.iloc[tr_i], df.iloc[te_i]
        if tr[label].nunique() < 2:
            continue
        rows.append(score(te[label], fit_predict(tr, te)))
    out = weighted(rows)
    out["skipped"] = []
    out["min_fold"] = 0
    out["scheme"] = f"GroupKFold({k}) · {group}"
    return out


def majority_baseline_kfold(df: pd.DataFrame, label: str, group: str,
                            k: int = 5) -> dict:
    """group_kfold 와 같은 분할에서의 다수 클래스 기준선."""
    def _maj(tr, te):
        return np.full(len(te), tr[label].value_counts().idxmax())
    return group_kfold(df, label, group, _maj, k)


def majority_baseline(df: pd.DataFrame, label: str, group: str,
                      min_fold: int = MIN_FOLD) -> dict:
    """학습 폴드의 다수 클래스를 그대로 찍는다 — **넘어야 할 선**."""
    def _maj(tr, te):
        return np.full(len(te), tr[label].value_counts().idxmax())
    return leave_one_group_out(df, label, group, _maj, min_fold)


# -- 보고 -----------------------------------------------------------------
def report(name: str, model: dict, base: dict, quiet: bool = False) -> dict:
    """**기준선을 먼저** 찍고, 모델이 그 아래면 실패로 표시한다.

    폴리곤 실험에서 기준선을 계산해 놓고 출력을 안 해서, 정확도 0.615 를
    개선으로 읽을 뻔했다(기준선 0.636). 순서를 코드로 고정한다.
    """
    d_acc = model["acc"] - base["acc"]
    d_mf1 = model["mf1"] - base["mf1"]
    # **정확도와 Macro-F1 이 갈릴 때가 중요하다.** 자세 실측에서 기하 모델은
    # 정확도 0.414 로 기준선 0.423 에 못 미쳤지만 MF1 은 0.119 → 0.228 이었다.
    # 클래스가 치우쳐 정확도가 신호를 가린 것이고, 그건 '미달' 이 아니다.
    # 반대로 둘 다 못 미치면(폴리곤 실험) 진짜 미달이다.
    if d_mf1 > MARGIN and d_acc < -MARGIN:
        verdict = "정확도만 미달(불균형에 가림)"
    elif d_acc < -MARGIN or d_mf1 < -MARGIN:
        verdict = "기준선 미달"
    elif abs(d_acc) <= MARGIN and abs(d_mf1) <= MARGIN:
        verdict = "기준선과 같음"
    else:
        verdict = "개선"
    out = {"task": name, "baseline": base, "model": model,
           "d_acc": round(d_acc, 3), "d_mf1": round(d_mf1, 3),
           "verdict": verdict}
    if quiet:
        return out
    print(f"\n=== {name} ===")
    print(f"  기준선(다수 클래스)  acc {base['acc']:.3f} · MF1 {base['mf1']:.3f}"
          f"   ← 먼저 본다")
    print(f"  모델                acc {model['acc']:.3f} · MF1 {model['mf1']:.3f}"
          f"   ({d_acc:+.3f} / {d_mf1:+.3f})")
    print(f"  폴드 {model.get('folds', 0)}개 · 표본 {model.get('n', 0):,} · "
          f"폴드별 정확도 {model.get('acc_min', 0):.3f}~{model.get('acc_max', 0):.3f}")
    if verdict == "기준선 미달":
        print("  ❌ 기준선보다 못하다. 개선이 아니다.")
    elif verdict == "기준선과 같음":
        print("  ⚠️ 기준선과 사실상 같다 — 신호가 없다고 봐야 한다.")
    elif verdict.startswith("정확도만"):
        print("  ⚠️ 정확도는 기준선 아래인데 Macro-F1 은 위다. 클래스가 치우쳐")
        print("     정확도가 신호를 가리는 경우다 — **정확도로 결론내지 말 것.**")
    if model.get("skipped"):
        print(f"  ※ 표본 부족으로 뺀 폴드 {len(model['skipped'])}개"
              f"(각 {model['min_fold']}개 미만)")
    return out


# -- 과제 등록부 -----------------------------------------------------------
@dataclass
class Task:
    """딥러닝으로 갈 수 있는 과제 하나. **데이터가 있는지부터 적는다.**"""
    key: str
    name: str
    group: str                    # 무엇을 통째로 빼고 검증하나
    data: str                     # 필요한 파일·디렉터리
    current: str                  # 지금 성적(고전 ML)
    status: str                   # ready / blocked
    note: str = ""
    paths: list = field(default_factory=list)

    def available(self) -> bool:
        return all(os.path.exists(os.path.join(ROOT, p)) for p in self.paths)


TASKS = [
    Task("detect", "돼지 탐지", "소스 데이터셋",
         "케글 pig-detection 45,611 bbox",
         "mAP50 0.659 (YOLOv8n 직접 학습)", "ready",
         "이미 학습됨. DL 로 더 올릴 여지가 가장 확실한 과제.",
         ["models/pig_yolo.pt"]),
    Task("posture", "자세 인식 (발정 3클래스)", "카메라 뷰(LOVO)",
         "크롭 피처 캐시 23,450행 × 60차원 (원본 없이도 돈다)",
         "acc 0.636 / MF1 0.434 · 상한 0.861", "ready",
         "좌/우 횡와는 bbox 로 원리상 구분 불가라 5클래스 상한이 0.861.\n"
         "**DL 이 이 상한을 넘을 수 있는 유일한 과제다** — 캐시는 60차원 "
         "요약이라 여기까지가 끝이고, 원본 크롭을 직접 봐야 좌/우가 갈린다.\n"
         "다만 원본 이미지는 케글에서 다시 받아야 한다(캐시엔 피처만 있다).",
         ["data/posture_crops.npz"]),
    Task("behavior", "행동 인식", "개체 ID(GroupKFold)",
         "Edinburgh 프레임 CSV",
         "acc 0.516 / MF1 0.386", "ready",
         "시간 윈도우가 효과를 냈다(+0.042). DL 은 시퀀스 모델이 자연스럽다.",
         ["data/edinburgh_frames.csv"]),
    Task("estrus", "발정 판정", "카메라 채널·개체",
         "AI Hub 71471 원자료 (미보유)",
         "AUC 0.465 — 무작위", "blocked",
         "**모델 문제가 아니라 라벨 어휘 문제다.** 이 서브셋 행동은 "
         "lying·standing·sitting·eating 4종뿐이고 승가·꼬리세움·기립반사가 "
         "주석에 없다. 여기에 DL 을 얹으면 성능이 아니라 카메라 교락을 "
         "더 잘 외운다 — 기하 피처로 AUC 1.0 이 나왔다가 못 본 카메라에서 "
         "0.409 로 무너진 적이 있다.",
         ["data/aihub/71471"]),
]


def available() -> list:
    return [t for t in TASKS if t.status == "ready" and t.available()]


def main() -> int:
    print("=" * 74)
    print("  딥러닝 과제 점검 — 무엇이 지금 돌아가나")
    print("=" * 74)
    for t in TASKS:
        have = t.available()
        mark = ("✅ 학습 가능" if t.status == "ready" and have else
                "⬜ 데이터 없음" if t.status == "ready" else "❌ 막힘")
        print(f"\n  {mark}  {t.name}")
        print(f"     검증 단위  {t.group} 를 통째로 빼고 학습")
        print(f"     데이터     {t.data}")
        print(f"     현재       {t.current}")
        if t.note:
            for line in t.note.split("\n"):
                print(f"     ※ {line}")
    n = len(available())
    print(f"\n  → 지금 바로 학습 가능한 과제 {n}개")
    print("\n  어떤 모델을 쓰든 규약은 같다:")
    print("    1) 기준선(다수 클래스)을 **먼저** 찍는다")
    print("    2) 정확도와 Macro-F1 을 **같이** 낸다")
    print("    3) 그룹을 통째로 빼고 검증한다(누수 검사 후)")
    print(f"    4) 표본 {MIN_FOLD}개 미만 폴드는 집계에서 뺀다")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
