"""71763 양돈 생체 에너지 — 파싱→모델링 데모/실행 스크립트.

환경센서(온도·습도·CO2·NH3) + 개체온도 + 체중 + 사양관리로부터
생체에너지 지표(호흡수·현열량·잠열량)를 예측하는 회귀 베이스라인.

실데이터:
    python competition/src/model_71763.py competition/data/aihub/71763   # 라벨 디렉터리
없이 실행하면 문서 스키마대로 합성 라벨을 만들어 전체 흐름을 시연한다.
"""
from __future__ import annotations

import os
import sys
import tempfile

import numpy as np
import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.model_selection import GroupKFold, KFold, cross_val_predict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import parse_aihub  # noqa: E402
import train as train_mod  # noqa: E402  (make_pipeline 재사용)

TARGETS = ["breath_rate", "sensible_heat", "latent_heat"]
ID_COLS = ["chamber", "pig_id", "measure_date", "measure_time"]


def load(label_dir: str | None) -> pd.DataFrame:
    if label_dir and os.path.isdir(label_dir):
        df = parse_aihub.parse_71763(label_dir)
        print(f"실데이터 파싱: {label_dir} → {len(df)}행")
    else:
        tmp = tempfile.mkdtemp()
        parse_aihub.generate_synthetic_71763(tmp, n=1500)
        df = parse_aihub.parse_71763(tmp)
        print(f"(합성 데이터 시연) {len(df)}행 — 실행: model_71763.py <라벨디렉터리>")
    return df


def run(df: pd.DataFrame) -> None:
    df = df.dropna(subset=[t for t in TARGETS if t in df.columns], how="all")
    for target in TARGETS:
        if target not in df.columns or df[target].notna().sum() < 30:
            print(f"\n[{target}] 데이터 부족 — 건너뜀")
            continue
        sub = df[df[target].notna()].copy()
        y = sub[target].to_numpy(dtype=float)

        drop = set(TARGETS) | set(ID_COLS)
        feats = [c for c in sub.columns if c not in drop]
        num = [c for c in feats if pd.api.types.is_numeric_dtype(sub[c])]
        cat = [c for c in feats if c not in num]
        X = sub[num + cat]

        pipe = train_mod.make_pipeline(
            num, cat, GradientBoostingRegressor(random_state=42))

        # 같은 개체(pig_id)가 train/test에 섞이는 누수 방지 → GroupKFold
        if "pig_id" in sub.columns and sub["pig_id"].nunique() >= 5:
            groups = sub["pig_id"].to_numpy()
            cv = GroupKFold(n_splits=5)
            pred = cross_val_predict(pipe, X, y, cv=cv, groups=groups)
            cvname = "GroupKFold(pig_id)"
        else:
            cv = KFold(n_splits=5, shuffle=True, random_state=42)
            pred = cross_val_predict(pipe, X, y, cv=cv)
            cvname = "KFold"

        mae = mean_absolute_error(y, pred)
        base = mean_absolute_error(y, np.full_like(y, y.mean()))
        print(f"\n=== [{target}] 회귀 ({cvname}) ===")
        print(f"  MAE {mae:.3f}  R² {r2_score(y, pred):.3f}  "
              f"(평균예측 대비 {(1 - mae / base):.1%} 개선)")

        pipe.fit(X, y)
        train_mod.save_importances(pipe, num, cat, f"71763_{target}")


def main() -> int:
    label_dir = sys.argv[1] if len(sys.argv) > 1 else None
    os.makedirs("competition/outputs", exist_ok=True)
    run(load(label_dir))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
