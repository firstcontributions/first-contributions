# 딥러닝 작업 지도

무엇이 지금 학습 가능하고, 무엇이 왜 막혔고, 어떤 파일을 쓰는지. 모델을
새로 만들기 전에 이 문서와 `src/ml_core.py` 를 먼저 본다.

```bash
python competition/src/ml_core.py              # 과제별 가용 여부 점검
python competition/src/build_kaggle_notebooks.py   # 캐글 학습 파일 생성
```

## 학습은 캐글 GPU 에서

로컬은 CPU 4스레드라 자세 LOVO 7폴드가 **50분**이다(실측). 캐글 T4 면 몇
분이므로 학습은 캐글에서 한다. `competition/notebooks/` 에 두 벌이 있다.

| 파일 | 쓰는 법 |
|---|---|
| `*.py` | 캐글 New Notebook → **셀 하나에 통째로 붙여넣기** (빠름) |
| `*.ipynb` | 캐글 File → Import Notebook |

| 노트북 | Add Input | Accelerator | Internet |
|---|---|---|---|
| `posture_cnn_kaggle` | Competition `multi-view-pig-posture-recognition` | GPU | **On** (resnet18 가중치) |
| `behavior_seq_kaggle` | Dataset `jackbyte/edinburgh-pig-behaviour-annotated` | GPU | Off 무방 |

노트북은 저장소가 없는 런타임에서 도니 평가 규약을 **인라인**한다. 인라인본과
`ml_core` 가 같은 판정을 내는지 테스트가 대조하므로, 캐글 결과와 로컬 결과를
나란히 놓을 수 있다.

---

## 0. 먼저 — 발정 모델을 만들기 전에

**"발정 판정 딥러닝" 은 지금 데이터로 안 된다.** 모델 문제가 아니다.

| 단계 | 통제 수준 | AUC |
|---|---|---|
| 돈방 라벨 + bbox 기하 | 없음 | ~1.00 ← **가짜** |
| 개체 내 대조 · 행동만 | 카메라 교락 제거 | 0.579 |
| **채널 고정 · 행동만** | **카메라·돈방·개체 전부** | **0.465** |

71471 서브셋의 행동 어휘는 `lying · standing · sitting · eating` 4종뿐이고
**승가(mounting) · 꼬리세움(tailing) · 기립반사가 주석에 없다.** 발정의
지시 변수가 라벨에 없으니 무엇을 얹어도 안 나온다.

여기에 딥러닝을 얹으면 성능이 오르는 게 아니라 **카메라 교락을 더 잘
외운다.** 실제로 기하 피처만으로 AUC 1.0 이 나왔는데, 못 본 카메라에서
0.409 로 무너졌다. 표현력이 커질수록 이 함정은 깊어진다.

### 그럼 무엇이 있으면 되나

`docs/AIHUB.md` §최종검증 결론 그대로:

1. 같은 돈방/카메라에서 **발정·비발정이 함께 관측**된 표본, 또는
2. 같은 개체의 **시간적 전이**(비발정 → 발정) 시계열, 또는
3. 정지 프레임이 아닌 **동영상 기반 활동량 변화**, 또는
4. **외음부이미지 서브셋** — 발정의 직접 생리 지표. Validation `511461`
   **627KB**

**4번이 현실적인 유일한 길이다.** 폴리곤 원천 10GB 와 달리 627KB 라
받을 수 있고, 행동 라벨의 어휘 문제를 생리 지표로 우회한다.

단, 설계에서 반드시 풀어야 할 것: 기존 외음부 라벨은 **전량 `ESTRUS=Y`**
(22,497건 · 175개체 · 7일자)라 **음성 표본이 없다.** 개체별 발정 달력
(`src/estrus_calendar.py`)으로 같은 개체의 비발정 일자를 음성으로 삼는
설계가 필요하고, 그때도 **개체를 통째로 빼고** 검증해야 한다.

> 다운로드는 국내 IP 전용이다. 이 컨테이너에서는 받을 수 없다.

---

## 1. 과제별 현황

| 과제 | 검증 단위 | 현재(고전 ML) | DL 여지 | 상태 |
|---|---|---|---|---|
| 돼지 탐지 | 소스 데이터셋 | mAP50 **0.659** | 크다 — 이미 YOLO 학습 | ✅ |
| 자세 인식(3클래스) | 카메라 뷰 LOVO | acc **0.636** / MF1 0.434 | **가장 확실** (아래) | ✅ |
| 행동 인식 | 개체 GroupKFold | acc **0.516** / MF1 0.386 | 시퀀스 모델이 자연스럽다 | ✅ |
| 발정 판정 | 카메라 채널·개체 | AUC **0.465** = 무작위 | 없음 — 라벨 문제 | ❌ |

### 자세 인식이 DL 로 갈 값이 가장 확실한 이유

좌/우 횡와는 **bbox 로 원리상 구분 불가**다. 둘 다 옆으로 누운 같은
모양의 상자라, 모델은 좌 157 / 우 210 으로 동전을 던진다. 두 클래스가
전체의 27.8% 이므로 **5클래스 상한이 1.0 이 아니라 0.861** 이다.

지금 쓰는 캐시(`data/posture_crops.npz`)는 **60차원 요약 피처**라 여기까지가
끝이다. 원본 크롭을 직접 보는 CNN 만이 좌/우를 가를 수 있다 —
**상한 자체를 올리는 유일한 경로**다.

다만 캐시엔 피처만 있어 **원본 이미지는 케글에서 다시 받아야 한다.**

---

## 2. 지켜야 할 규약 — `src/ml_core.py`

새 규약이 아니다. 이미 쓰던 방식을 모은 것이라, **공표된 기준선을 그대로
재현하는지 테스트가 확인한다**(자세 5클래스 0.423/0.119 · 3클래스
0.547/0.239).

```python
import ml_core as mc

mc.leakage_check(df, group="view", id_col="path")   # 분할 전에
base  = mc.majority_baseline(df, "cls3", "view")
model = mc.leave_one_group_out(df, "cls3", "view", fit_predict)
mc.report("자세 3클래스", model, base)               # 기준선을 먼저 찍는다
```

`fit_predict(train_df, test_df) -> 예측` 규약만 맞추면 사이킷런이든
토치든 같은 자로 잰다.

### 굳혀 둔 실수 넷

1. **기준선을 먼저 찍는다.** 기하 모델 5클래스 0.414 인데 다수 클래스만
   찍어도 0.423 이었다. 폴리곤 실험에서는 기준선을 계산해 놓고 출력을 안
   해서 0.615 를 개선으로 읽을 뻔했다(기준선 0.636).
2. **정확도만 보지 않는다.** 위 사례에서 판별력은 Macro-F1 에서만
   드러났다(0.119 → 0.228). `report()` 는 정확도가 기준선 아래여도 MF1 이
   위면 `정확도만 미달(불균형에 가림)` 로 구분한다 — 그건 미달이 아니다.
3. **그룹 누수를 막는다.** train1↔train2 가 이미지 3,090장을 공유해 0.642
   가 나왔고, 못 본 카메라로 재면 0.4 대였다. `id_col` 은 **전역 고유**
   값을 준다(파일 경로 등) — 그룹마다 0 부터 매겨지는 `frame_idx` 를
   넘겼다가 100% 가 '누수' 로 찍힌 적이 있다. 지금은 그 경우를 카운터로
   판정해 검사를 건너뛴다.
4. **작은 폴드는 집계에서 뺀다**(`MIN_FOLD=30`). 스톨 24개·시드 5회로
   쟀다가 순서가 뒤집혔다 — 정확도 낮은 쪽이 AUC 가 높게 나왔다.

폴드 집계는 **표본 수 가중**이다. 자세 뷰별 LOVO 는 폴드 정확도가
0.356~0.770 로 흩어져서, 단순 평균이면 작은 폴드에 끌려간다.

---

## 3. 파일 지도

### 학습·모델
| 파일 | 하는 일 |
|---|---|
| `ml_core.py` | **공통 규약** — 분할·기준선·지표·보고 |
| `train_pseudo_label.py` | YOLO 탐지기 학습(→ `models/pig_yolo.pt`) |
| `finetune_polygon.py` | 세그멘테이션 파인튜닝 + CPU 예산 계산 |
| `model_behavior_appearance.py` | 행동 인식(기하+모션+외형) |
| `model_71471_estrus.py` | 발정 이진 분류 — **데이터 없음** |
| `model_gilt_anestrus.py` | 후보돈 무발정 위험(합성) |
| `model_edinburgh_behavior.py` · `model_71763.py` | 초기 베이스라인 |

### 피처·전처리
`posture_features.py` · `posture_crop_feats.py`(60차원 크롭 피처) ·
`temporal_features.py`(롤링 윈도우) · `iou_tracker.py` · `motion_tracker.py` ·
`reid.py` · `box_merge.py` · `view_align.py`

### 평가·검증
| 파일 | 하는 일 |
|---|---|
| `posture_crossview.py` | 뷰별 LOVO · 기준선 · 상한 · 혼동행렬 |
| `estrus_contrast_eval.py` | 개체 내 대조 3단계 — **0.465 를 낸 코드** |
| `validate_estrus_reference.py` | 교락 자동 탐지 — 누수된 AUC 를 보고하지 않는다 |
| `estrus_calendar.py` | 외음부 라벨 → 개체별 발정 달력 |
| `polygon_shape_eval.py` | 폴리곤 vs bbox 상한 측정 |
| `posture_eval.py` · `pose_vs_behavior_eval.py` | 교차-데이터셋 일반화 |

### 데이터 파서
`parse_aihub.py` · `parse_71471_real.py` · `parse_71471_keypoints.py` ·
`parse_pig_polygon.py` · `parse_edinburgh.py` · `aihub_bridge.py` ·
`fetch_622.py`(다운로드 진단 포함)

---

## 4. 지금 있는 데이터

| 자산 | 크기 | 쓸 곳 |
|---|---|---|
| 케글 pig-detection | 3.0GB | 탐지 학습 |
| `data/posture_crops.npz` | 5.1MB | 자세 — 23,450행 × 60차원 |
| `data/edinburgh_frames.csv` | 1.3MB | 행동 — 12,646행 · 96개체 · 16종 |
| `models/pig_yolo.pt` | 24MB | 학습된 탐지기(gitignore) |
| AI Hub 71471 | — | **없음** (국내망 필요) |

> 케글 데이터는 CC BY-NC 라 커밋하지 않는다. 가중치도 gitignore 다.
