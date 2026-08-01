"""탐색적 데이터 분석(EDA).

data/train.csv 를 읽어 기초 통계, 결측/분포, 타깃과의 상관을 요약하고
outputs/ 에 요약표(csv)와 그림(png)을 저장한다.
"""
from __future__ import annotations

import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

DATA = "yangdon/data/train.csv"
OUT = "yangdon/outputs"

# 한글 폰트가 없을 수 있으므로 그림 라벨은 영문 키를 사용.
NUMERIC_TARGETS = ["adg_kg_day", "fcr", "market_age_days"]


def main() -> None:
    os.makedirs(OUT, exist_ok=True)
    df = pd.read_csv(DATA)

    # 1) 기초 통계
    desc = df.describe(include="all").T
    desc.to_csv(f"{OUT}/eda_summary.csv", encoding="utf-8-sig")
    print("기초 통계 저장:", f"{OUT}/eda_summary.csv")

    # 2) 결측 점검
    na = df.isna().sum()
    if na.sum() == 0:
        print("결측치: 없음")
    else:
        print("결측치:\n", na[na > 0])

    # 3) 수치형 상관 (타깃 adg_kg_day 기준)
    num = df.select_dtypes(include=[np.number])
    corr = num.corr()
    corr.to_csv(f"{OUT}/correlation.csv", encoding="utf-8-sig")

    target = "adg_kg_day"
    corr_t = corr[target].drop(target).sort_values(key=np.abs, ascending=False)
    print(f"\n[{target}] 와의 상관계수 (절댓값 순):")
    print(corr_t.round(3).to_string())

    # 4) 상관 상위 변수 산점도
    top = corr_t.head(4).index.tolist()
    fig, axes = plt.subplots(1, len(top), figsize=(4 * len(top), 3.6))
    for ax, col in zip(np.atleast_1d(axes), top):
        ax.scatter(df[col], df[target], s=6, alpha=0.25)
        ax.set_xlabel(col)
        ax.set_ylabel(target)
        ax.set_title(f"{col} vs {target}")
    fig.tight_layout()
    fig.savefig(f"{OUT}/scatter_top_features.png", dpi=110)
    plt.close(fig)
    print("산점도 저장:", f"{OUT}/scatter_top_features.png")

    # 5) 상관 히트맵
    fig, ax = plt.subplots(figsize=(8, 6.5))
    im = ax.imshow(corr, cmap="RdBu_r", vmin=-1, vmax=1)
    ax.set_xticks(range(len(corr)))
    ax.set_yticks(range(len(corr)))
    ax.set_xticklabels(corr.columns, rotation=90, fontsize=7)
    ax.set_yticklabels(corr.columns, fontsize=7)
    fig.colorbar(im, ax=ax, fraction=0.046, pad=0.04)
    ax.set_title("Numeric feature correlation")
    fig.tight_layout()
    fig.savefig(f"{OUT}/correlation_heatmap.png", dpi=110)
    plt.close(fig)
    print("히트맵 저장:", f"{OUT}/correlation_heatmap.png")

    # 6) 폐사 그룹별 환경 차이
    if "mortality" in df.columns:
        grp = df.groupby("mortality")[["nh3_ppm", "stocking_density",
                                       "avg_temp_c"]].mean().round(2)
        grp.to_csv(f"{OUT}/mortality_group_means.csv", encoding="utf-8-sig")
        print("\n폐사(0/1) 그룹별 환경 평균:\n", grp.to_string())


if __name__ == "__main__":
    main()
