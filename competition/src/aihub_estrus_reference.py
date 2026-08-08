"""AI Hub 71471(돼지 발정행동) 기준(reference) 모듈.

71471 데이터는 국내 IP 전용이라 원격에서 직접 못 받지만, 그 **행동 분류 체계와
발정 판별 기준**을 표준으로 인코딩해 둔다. 이 표준으로 케글 등 다른 데이터의
행동/활동을 발정 관점에서 분석·점수화한다.

71471 문서 기반 표준:
  - 행동 분류: standing, lying, eating, head shaking, tailing, sitting
  - 발정 판별: 발정체크장비 + 전문가 검수(정답), 멀티모달(영상·keypoint·울음소리·
               외음부·3D). 문서상 멀티모달 발정분류 CRNN F1 0.90.
  - 발정기 행동 특징(수의학): 기립반사(standing)·승가(mounting)·꼬리세움(tailing)·
    서성임(활동↑)·탐색↑, 휴식(lying/sitting)↓.

이 표준은 두 가지로 쓴다:
  (1) 규칙 기준: 아래 가중치로 발정 점수 산출(정답 없이).
  (2) 지도 보정: 71471 실데이터(발정 정답)가 오면 calibrate()로 가중치를 학습.
"""
from __future__ import annotations

import numpy as np

# 71471 표준 행동 분류
REFERENCE_BEHAVIORS = ["standing", "lying", "eating", "head_shaking",
                       "tailing", "sitting", "restless", "mounting"]

# 표준 발정 연관 가중치(+ 발정 시사 / - 휴식). 수의학 근거.
ESTRUS_REFERENCE = {
    "mounting": 1.0,       # 승가 — 최강 신호
    "tailing": 0.9,        # 꼬리세움
    "standing": 0.6,       # 기립반사(모돈 발정 핵심)
    "restless": 0.5,       # 서성임·탐색·활동 증가
    "head_shaking": 0.2,
    "eating": -0.2,
    "sitting": -0.3,
    "lying": -0.6,         # 휴식
}
ACTIVITY_WEIGHT = 0.5      # 활동량(정규화) 기여

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
