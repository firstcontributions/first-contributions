"""양돈 스마트팜 합성 데이터 생성기.

실제 공모전 데이터가 확보되기 전, 파이프라인을 end-to-end로 검증하기 위한
현실적인 모사 데이터를 만든다. 변수 간 관계(온도 스트레스 → 증체 저하,
사육밀도 → 폐사 위험 등)를 의도적으로 심어 두어 모델이 학습할 신호가 있다.

실제 데이터가 오면 이 스크립트는 버리고, 동일한 컬럼 스키마의 CSV를
data/train.csv 로 넣으면 이후 단계(eda.py, train.py)가 그대로 동작한다.
"""
from __future__ import annotations

import numpy as np
import pandas as pd

RNG = np.random.default_rng(42)

# 출하 목표 체중(kg). 국내 비육돈 출하 체중 약 110~120kg.
TARGET_MARKET_WEIGHT = 115.0


def generate(n: int = 4000) -> pd.DataFrame:
    """돈군(batch) 단위 n개 레코드를 생성한다.

    한 행 = 한 돈군(같은 시기 같은 돈사에 입식되어 함께 출하되는 돼지 집단).
    """
    farm_id = RNG.integers(1, 41, size=n)          # 40개 농장
    house_id = RNG.integers(1, 9, size=n)          # 농장당 8개 돈사
    sex = RNG.choice(["거세", "암"], size=n, p=[0.5, 0.5])
    breed = RNG.choice(["삼원교잡(LYD)", "이원교잡(LY)"], size=n, p=[0.8, 0.2])

    # 입식 시점 정보
    init_age = RNG.normal(70, 5, n).clip(60, 85)          # 입식 일령(자돈 이유 후)
    init_weight = RNG.normal(25, 3, n).clip(18, 34)       # 입식 체중(kg)

    # 환경 변수 (비육 기간 평균)
    temp = RNG.normal(22, 4, n).clip(10, 33)             # 돈사 평균기온(°C)
    humidity = RNG.normal(65, 10, n).clip(35, 95)        # 상대습도(%)
    nh3 = RNG.normal(15, 6, n).clip(2, 45)               # 암모니아 농도(ppm)
    co2 = RNG.normal(1500, 500, n).clip(500, 4000)       # CO2 농도(ppm)
    stocking_density = RNG.normal(1.3, 0.25, n).clip(0.7, 2.2)  # 두/m2

    # 사양 관리
    feed_intake = RNG.normal(2.3, 0.3, n).clip(1.5, 3.2)   # 두당 일일 사료섭취(kg)
    feed_grade = RNG.choice(["고급", "표준", "저가"], size=n, p=[0.3, 0.5, 0.2])
    vaccinated = RNG.choice([1, 0], size=n, p=[0.85, 0.15])
    antibiotic_days = RNG.poisson(2.5, n).clip(0, 20)      # 항생제 투여일수

    df = pd.DataFrame({
        "farm_id": farm_id,
        "house_id": house_id,
        "sex": sex,
        "breed": breed,
        "init_age_days": init_age.round(1),
        "init_weight_kg": init_weight.round(1),
        "avg_temp_c": temp.round(1),
        "humidity_pct": humidity.round(1),
        "nh3_ppm": nh3.round(1),
        "co2_ppm": co2.round(0),
        "stocking_density": stocking_density.round(2),
        "feed_intake_kg": feed_intake.round(2),
        "feed_grade": feed_grade,
        "vaccinated": vaccinated,
        "antibiotic_days": antibiotic_days,
    })

    # ---- 일당증체량(ADG, kg/day) 을 변수들로부터 생성 (숨은 정답 함수) ----
    # 열 스트레스: 최적 22°C에서 멀어질수록 증체 저하 (특히 고온)
    temp_stress = np.where(temp > 22, (temp - 22) * 0.018, (22 - temp) * 0.006)
    feed_grade_effect = df["feed_grade"].map(
        {"고급": 0.06, "표준": 0.0, "저가": -0.05}).to_numpy()
    sex_effect = np.where(sex == "거세", 0.03, -0.03)

    adg = (
        0.85
        + (feed_intake - 2.3) * 0.22          # 사료 섭취↑ → 증체↑
        - temp_stress
        - (nh3 - 15) * 0.004                   # 암모니아↑ → 증체↓
        - (stocking_density - 1.3) * 0.05      # 밀집↑ → 증체↓
        + feed_grade_effect
        + sex_effect
        + vaccinated * 0.02
        + RNG.normal(0, 0.04, n)               # 잔차
    ).clip(0.55, 1.25)

    # 출하일령 = 입식일령 + (목표체중 - 입식체중)/ADG
    days_to_market = (TARGET_MARKET_WEIGHT - init_weight) / adg
    market_age = (init_age + days_to_market).round(0)

    # 사료요구율(FCR) = 총사료 / 총증체. 대략 feed_intake / adg 로 근사.
    fcr = (feed_intake / adg).round(2)

    # ---- 폐사 발생 확률 (로지스틱) ----
    # 환경/사양 변수가 폐사 위험에 뚜렷이 작용하도록 계수를 설정.
    logit = (
        -2.6
        + (nh3 - 15) * 0.11
        + (stocking_density - 1.3) * 1.8
        + temp_stress * 3.0
        - vaccinated * 1.2
        + (antibiotic_days > 6).astype(float) * 1.1
    )
    mortality_prob = 1 / (1 + np.exp(-logit))
    mortality = (RNG.random(n) < mortality_prob).astype(int)

    df["adg_kg_day"] = adg.round(3)
    df["fcr"] = fcr
    df["market_age_days"] = market_age.astype(int)
    df["mortality"] = mortality

    return df


def main() -> None:
    df = generate()
    out = "yangdon/data/train.csv"
    df.to_csv(out, index=False, encoding="utf-8-sig")
    print(f"생성 완료: {out}  (행 {len(df)}, 열 {df.shape[1]})")
    print(df.head())
    print("\n타깃 요약:")
    print(df[["adg_kg_day", "fcr", "market_age_days", "mortality"]].describe().round(3))
    print("폐사율:", f"{df['mortality'].mean():.1%}")


if __name__ == "__main__":
    main()
