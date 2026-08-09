"""AI Hub 71471(돼지 발정행동) 기준(reference) 모듈.

71471 데이터는 국내 IP 전용이라 원격에서 직접 못 받지만, 그 **행동 분류 체계와
발정 판별 기준**을 표준으로 인코딩해 둔다. 이 표준으로 케글 등 다른 데이터의
행동/활동을 발정 관점에서 분석·점수화한다.

71471 문서 기반 표준:
  - 행동 분류: standing, lying, eating, head shaking, tailing, sitting
  - 발정 판별: 발정체크장비 + 전문가 검수(정답), 멀티모달(영상·keypoint·울음소리·
               외음부·3D). 문서상 멀티모달 발정분류 CRNN F1 0.90.
  - 발정기 징후(수의학·현장 교육자료): **기립반사(부동자세)**·승가(mounting)·
    꼬리세움(tailing)·**귀 세움(안쪽으로 바짝)**·**외음부 발적·점액 분비**·
    서성임(활동↑)·탐색↑, 휴식(lying/sitting)↓.
    ※ 71471 의 `standing`(서 있는 자세)과 **기립반사**는 다른 개념이다 —
      아래 ESTRUS_REFERENCE 주석 참조.

이 표준은 두 가지로 쓴다:
  (1) 규칙 기준: 아래 가중치로 발정 점수 산출(정답 없이).
  (2) 지도 보정: 71471 실데이터(발정 정답)가 오면 calibrate()로 가중치를 학습.
"""
from __future__ import annotations

import numpy as np

# 71471 표준 행동 분류 + 현장 발정 징후(교육자료·수의 문헌 기반)
REFERENCE_BEHAVIORS = ["standing", "lying", "eating", "head_shaking",
                       "tailing", "sitting", "restless", "mounting",
                       "immobility", "ear_erect", "vulva_sign"]

# 표준 발정 연관 가중치(+ 발정 시사 / - 휴식). 수의학 근거.
#
# ⚠️ 중요 구분: 71471 의 `standing` 은 **단순히 서 있는 자세(posture)** 이지
# **기립반사(standing reflex, 부동자세)가 아니다.** 초기 버전은 이 둘을 혼동해
# standing 에 0.6 을 줬으나, 서 있는 자세 자체는 발정 신호가 약하다(실데이터에서도
# 발정/비발정 간 standing 비율 차이 거의 없음: 3.7% vs 3.3%). 기립반사는 별도
# 카테고리 `immobility` 로 분리한다.
ESTRUS_REFERENCE = {
    "immobility": 1.0,     # 기립반사(부동자세) — 승가압박 시 미동 없음. 현장 확진 기준
    "mounting": 1.0,       # 승가 — 최강 행동 신호
    "tailing": 0.9,        # 꼬리세움
    "vulva_sign": 0.9,     # 외음부 발적·부종·점액 분비 — 직접 생리 지표
    "ear_erect": 0.7,      # 귀 세움(안쪽으로 바짝) — 현장 관찰 지표
    "restless": 0.5,       # 서성임·탐색·활동 증가
    "standing": 0.15,      # 서 있는 자세 — 약한 신호(기립반사와 구분)
    "head_shaking": 0.2,
    "eating": -0.2,
    "sitting": -0.3,
    "lying": -0.6,         # 휴식
}
ACTIVITY_WEIGHT = 0.5      # 활동량(정규화) 기여

# 징후별 관측 가능성(CCTV 기준) — 어떤 카메라·해상도가 필요한지 설계 근거
DETECTABILITY = {
    "restless":   ("high",   "일반 부감 CCTV, 활동량 시계열로 포착"),
    "immobility": ("medium", "활동량 급감 + 자세 유지. 웅돈 접촉·압박 시점 필요"),
    "mounting":   ("medium", "군사 사육에서만 발생. 부감 시점 필요"),
    "tailing":    ("low",    "꼬리 해상도 필요. 근접·고해상 카메라"),
    "ear_erect":  ("low",    "귀 각도 판별에 근접 촬영 또는 고해상 필요"),
    "vulva_sign": ("low",    "후방 근접 카메라 필요(일반 CCTV로는 불가)"),
}

# 타 데이터 행동 어휘 → 71471 표준 카테고리 매핑
VOCAB_MAP = {
    # Edinburgh
    "walk": "restless", "run": "restless", "investigating": "restless",
    "chase": "restless", "playwithtoy": "restless",
    "nose-poke-elsewhere": "restless", "nose-to-nose": "restless",
    "fight": "restless", "jumpontopof": "mounting",
    "standing": "standing", "lying": "lying", "sleep": "lying",
    "sitting": "sitting", "eat": "eating", "drink": "eating",
    # 71471 자체 어휘
    "head shaking": "head_shaking", "head_shaking": "head_shaking",
    "tailing": "tailing", "eating": "eating", "mounting": "mounting",
    "restless": "restless",
    # 현장 발정 징후(교육자료 기반) — 관측 파이프라인이 산출하면 매핑된다
    "immobility": "immobility", "standing_reflex": "immobility",
    "부동자세": "immobility", "기립반사": "immobility",
    "ear_erect": "ear_erect", "ears_up": "ear_erect", "귀세움": "ear_erect",
    "vulva_sign": "vulva_sign", "vulva": "vulva_sign", "외음부": "vulva_sign",
}


def to_reference(behavior: str) -> str | None:
    """임의 데이터의 행동 라벨 → 71471 표준 카테고리."""
    if behavior is None:
        return None
    return VOCAB_MAP.get(str(behavior).strip().lower(),
                         VOCAB_MAP.get(str(behavior).strip()))


class EstrusReference:
    """71471 발정 표준. 규칙 점수 + (정답 있으면) 지도 보정."""

    def __init__(self):
        self.weights = dict(ESTRUS_REFERENCE)
        self.activity_w = ACTIVITY_WEIGHT
        self.calibrated = False
        self._clf = None
        self._cols = None

    def score(self, ref_fractions: dict, activity_norm: float) -> float:
        """표준 카테고리 비율 dict + 활동량(0~1) → 발정 원점수."""
        s = self.activity_w * float(activity_norm)
        for cat, w in self.weights.items():
            s += w * float(ref_fractions.get(cat, 0.0))
        return s

    def calibrate(self, ref_fraction_rows, activity_norm, y) -> float:
        """71471 발정 정답으로 로지스틱 보정. 반환: 교차검증 AUC.

        ref_fraction_rows: [{cat:frac,...}, ...], activity_norm: array, y: 0/1.
        """
        from sklearn.linear_model import LogisticRegression
        from sklearn.metrics import roc_auc_score
        from sklearn.model_selection import cross_val_predict
        cats = REFERENCE_BEHAVIORS
        X = np.array([[r.get(c, 0.0) for c in cats] + [a]
                      for r, a in zip(ref_fraction_rows, activity_norm)])
        y = np.asarray(y).astype(int)
        clf = LogisticRegression(max_iter=1000, class_weight="balanced")
        proba = cross_val_predict(clf, X, y, cv=5, method="predict_proba")[:, 1]
        auc = float(roc_auc_score(y, proba))
        clf.fit(X, y)
        self._clf = clf; self._cols = cats + ["activity"]
        self.calibrated = True
        return auc

    def score_calibrated(self, ref_fractions: dict, activity_norm: float) -> float:
        if not self.calibrated:
            return self.score(ref_fractions, activity_norm)
        x = np.array([[ref_fractions.get(c, 0.0) for c in REFERENCE_BEHAVIORS]
                      + [activity_norm]])
        return float(self._clf.predict_proba(x)[0, 1])


def map_fractions(behavior_fractions: dict) -> dict:
    """원본 행동 비율 dict → 표준 카테고리 비율로 합산."""
    out: dict = {}
    for beh, frac in behavior_fractions.items():
        cat = to_reference(beh)
        if cat:
            out[cat] = out.get(cat, 0.0) + float(frac)
    return out
