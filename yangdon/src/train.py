"""베이스라인 모델링.

두 가지 대표 과제를 하나의 스크립트로 다룬다.
  - 회귀:  일당증체량(adg_kg_day) 예측 → 생산성 지표
  - 분류:  폐사(mortality) 여부 예측 → 위험 관리 지표

전처리(수치 스케일 + 범주 원-핫)와 모델을 sklearn Pipeline 으로 묶고,
5-fold 교차검증으로 성능을 보고한 뒤 전체 데이터로 재학습하여
특성 중요도를 outputs/ 에 저장한다.

사용:
    python yangdon/src/train.py            # 두 과제 모두
    python yangdon/src/train.py reg        # 회귀만
    python yangdon/src/train.py clf        # 분류만
"""
from __future__ import annotations

import os
import sys

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import (GradientBoostingClassifier,
                              GradientBoostingRegressor)
from sklearn.metrics import (mean_absolute_error, r2_score, roc_auc_score)
from sklearn.model_selection import KFold, StratifiedKFold, cross_val_predict
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

DATA = "yangdon/data/train.csv"
OUT = "yangdon/outputs"

# 타깃/누수(leakage) 변수는 특성에서 제외한다.
# adg 를 예측할 때 fcr/market_age 는 adg 로부터 파생되므로 누수 → 제외.
LEAK_COLS = ["adg_kg_day", "fcr", "market_age_days", "mortality"]


def build_features(df: pd.DataFrame) -> tuple[list[str], list[str]]:
    # 수치형(number)만 num, 나머지(object/string/category)는 cat 으로 분류.
    # 판다스 버전에 따라 문자열이 object 또는 string dtype 일 수 있으므로
    # dtype==object 비교 대신 is_numeric_dtype 로 판별한다.
    feats = [c for c in df.columns if c not in LEAK_COLS]
    num = [c for c in feats if pd.api.types.is_numeric_dtype(df[c])]
    cat = [c for c in feats if c not in num]
    return num, cat


def make_pipeline(num: list[str], cat: list[str], estimator) -> Pipeline:
    pre = ColumnTransformer([
        ("num", StandardScaler(), num),
        ("cat", OneHotEncoder(handle_unknown="ignore"), cat),
    ])
    return Pipeline([("pre", pre), ("model", estimator)])


def save_importances(pipe: Pipeline, num: list[str], cat: list[str],
                     name: str) -> None:
    ohe = pipe.named_steps["pre"].named_transformers_["cat"]
    feat_names = num + list(ohe.get_feature_names_out(cat))
    imp = pipe.named_steps["model"].feature_importances_
    s = pd.Series(imp, index=feat_names).sort_values(ascending=False)
    s.round(4).to_csv(f"{OUT}/importance_{name}.csv",
                      header=["importance"], encoding="utf-8-sig")
    print(f"  특성 중요도 저장: {OUT}/importance_{name}.csv")
    print(s.head(8).round(4).to_string())


def run_regression(df: pd.DataFrame) -> None:
    print("\n=== 회귀: 일당증체량(adg_kg_day) 예측 ===")
    y = df["adg_kg_day"].to_numpy()
    num, cat = build_features(df)
    X = df[num + cat]

    pipe = make_pipeline(num, cat, GradientBoostingRegressor(random_state=42))
    cv = KFold(n_splits=5, shuffle=True, random_state=42)
    pred = cross_val_predict(pipe, X, y, cv=cv)

    print(f"  MAE : {mean_absolute_error(y, pred):.4f} kg/day")
    print(f"  R^2 : {r2_score(y, pred):.4f}")
    # 기준선(평균 예측) 대비 개선
    baseline_mae = mean_absolute_error(y, np.full_like(y, y.mean()))
    print(f"  (평균예측 MAE {baseline_mae:.4f} 대비 "
          f"{(1 - mean_absolute_error(y, pred) / baseline_mae):.1%} 개선)")

    pipe.fit(X, y)
    save_importances(pipe, num, cat, "regression")


def run_classification(df: pd.DataFrame) -> None:
    print("\n=== 분류: 폐사(mortality) 예측 ===")
    y = df["mortality"].to_numpy()
    if y.sum() < 10:
        print("  양성 표본이 너무 적어 건너뜀.")
        return
    num, cat = build_features(df)
    X = df[num + cat]

    pipe = make_pipeline(
        num, cat, GradientBoostingClassifier(random_state=42))
    cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
    proba = cross_val_predict(pipe, X, y, cv=cv, method="predict_proba")[:, 1]

    print(f"  폐사율(양성비율): {y.mean():.1%}")
    print(f"  ROC-AUC : {roc_auc_score(y, proba):.4f}")

    pipe.fit(X, y)
    save_importances(pipe, num, cat, "classification")


def main() -> None:
    os.makedirs(OUT, exist_ok=True)
    df = pd.read_csv(DATA)
    task = sys.argv[1] if len(sys.argv) > 1 else "all"

    if task in ("reg", "all"):
        run_regression(df)
    if task in ("clf", "all"):
        run_classification(df)


if __name__ == "__main__":
    main()
