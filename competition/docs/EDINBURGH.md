# 실데이터 트랙 — Edinburgh Pig Behaviour (Kaggle)

AI Hub 71471은 국내 IP에서만 다운로드 가능(해외 클라우드 차단)해서, 원격
환경에서 바로 실험 가능한 **공개 대체 데이터**로 검증 트랙을 구성했다.

- 출처: Kaggle `jackbyte/edinburgh-pig-behaviour-annotated` (CC BY-NC 4.0)
- 특징: 돈방 CCTV 영상에서 **개체별·프레임별 bbox + 행동 라벨**(시계열)
- 라이선스상 데이터는 저장소에 커밋하지 않고 다운로드로 받는다.

## 받는 법 (영상 제외, 주석 JSON만 — 가볍다)

```bash
pip install kaggle          # + ~/.kaggle/kaggle.json (Kaggle API 토큰)
# 각 녹화 폴더의 output.json 만 선택 다운로드
kaggle datasets files jackbyte/edinburgh-pig-behaviour-annotated   # 경로 확인
kaggle datasets download jackbyte/edinburgh-pig-behaviour-annotated \
  -f <녹화>/output.json -p competition/data/edinburgh/<녹화>
```
(영상 color.mp4 는 녹화당 ~280MB로 크므로 받지 않는다. 행동 분석엔 output.json만 필요.)

## output.json 구조

```
{ videoFileName, stepSize(0.1=10fps), config,
  objects: [ { id, frames: [ {frameNumber, bbox:{x,y,width,height},
                              visible, behaviour}, ... ] } ] }
```

행동 라벨(16종): investigating, walk, standing, eat, fight, lying, sleep,
nose-to-nose, drink, sitting, run, playwithtoy, nose-poke-elsewhere,
**jumpontopof(승가=번식행동)**, other, chase.

## 파이프라인

```bash
python competition/src/parse_edinburgh.py                    # output.json → 프레임 CSV
python competition/src/model_edinburgh_behavior.py competition/data/edinburgh_frames.csv
```

- `parse_edinburgh.py`: 프레임 단위 테이블(개체 시계열). 컬럼을 71471 파서와
  호환되게 맞춰 `build_estrus_features`·`estrus_onset` 재사용 가능.
- `model_edinburgh_behavior.py`: 모션 피처(속도·가속도·면적변화) + bbox →
  행동 분류. **개체 분리 GroupKFold**.

## 실데이터 베이스라인 결과 (12녹화·96개체·12,646프레임)

| 지표 | 값 |
|---|---|
| 정확도 | 0.43 (12개 행동 통합, 희소<100 → other) |
| Macro-F1 | 0.33 |
| 우수 | eat F1 0.84 · walk 0.57 · investigating 0.46 |
| 핵심 피처 | 위치, **속도(활동량)**, 크기 |

bbox+모션만의 정직한 베이스라인. **활동량(속도)이 유효 신호**임을 실데이터로
확인 — 이는 발정 관찰(활동↑·정지↓)의 핵심 기반이다. 향상 여지: keypoint/자세,
시간 윈도우 시퀀스 모델(LSTM/temporal), 외형 특징(영상 프레임) 결합.

## 교차 데이터셋 검증 도구 (posture_eval.py)

독립된 Kaggle 대회 **multi-view-pig-posture-recognition** 데이터로, 행동/자세로
학습한 모델의 **일반화 성능**을 검증한다.

- 공통 자세공간 {standing, sitting, lying} 으로 매핑
  (대회: Standing/Sitting/lateral·sternal-lying, 소스: standing/sitting/lying·sleep)
- 스케일·해상도 불변 피처만 사용(aspect_ratio, area 백분위) → 데이터셋 간 비교 가능

```bash
python competition/src/posture_eval.py                         # 소스=Edinburgh
python competition/src/posture_eval.py <behavior_frames.csv>   # 소스=AI Hub 71471 등
```

결과 예(소스=Edinburgh → 대회 평가):

| 구성 | 정확도 | Macro-F1 |
|---|---|---|
| 교차(Edinburgh→대회) | 0.41 | 0.31 |
| 대회 내부 천장(train1→train2) | 0.75 | 0.64 |

→ 행동 데이터로 학습한 모델이 대회 데이터엔 일반화가 약함(도메인 갭 정량화).
이 갭이 검증 도구의 핵심 산출물이다. 개선: 뷰 정합, bbox 크롭 외형(CNN) 피처
추가. 대회 데이터는 용량·라이선스상 커밋하지 않고 `kagglehub` 로 받는다.

## 멀티뷰 뷰 정합 & 프론트

대회 test 세트는 train에 없는 카메라 뷰로 구성된 **교차-뷰** 과제다.
`view_align.py` 는 라벨 있는 train1+train2에서 test 뷰를 held-out 으로 떼어
**뷰 정합 전/후**를 비교한다(뷰별 aspect z-정규화 + 뷰내 면적 백분위).

| 구성 | 정확도 | Macro-F1 |
|---|---|---|
| 뷰 정합 전 | 0.378 | 0.220 |
| 뷰 정합 후 | 0.362 | 0.228 |

→ 기하 피처만으론 뷰 정규화 효과가 미미(±0.01). **외형(bbox 크롭 CNN) 피처가
필요**함을 수치로 확인. (표본 516행으로 잡음도 큼)

**프론트**: `build_posture_gallery.py` → `dashboard/posture_gallery.html`
- 실제 대회 이미지에 bbox+자세(정답 색/예측 오답 빨강 점선) SVG 오버레이 갤러리
- 한 카메라 연속 프레임에 bbox를 그린 **주석 영상(webm)** 임베드
- 자체완결 HTML(이미지/영상 data URI). 대회 데이터·생성 HTML은 커밋 제외.

```bash
python competition/src/view_align.py            # 뷰 정합 전/후 정확도
python competition/src/build_posture_gallery.py # 사진·영상 프론트 생성
```

## AI Hub 71471 로 옮길 때

동일 개체 시계열 구조라, 71471 라벨을 로컬(국내)에서 받아 `parse_aihub.py`
(또는 파일명/필드에 맞춘 소폭 수정)로 같은 프레임 스키마를 만들면 이 행동/활동
파이프라인과 발정 모델을 그대로 적용할 수 있다.
