# 라벨 스키마 & 파서 (사용 확정 3종)

AI Hub 각 데이터셋 view 페이지의 **'어노테이션 포맷 및 데이터 구조'** 에서
확인한 스키마. 파서는 `src/parse_aihub.py`, 검증은 `python
yangdon/src/parse_aihub.py --selftest` (스키마대로 만든 합성 샘플로 라운드트립).

> ⚠️ 실제 필드명이 문서와 미세하게 다를 수 있다. 파서는 방어적으로 접근하며,
> 실데이터 확보 시 이 문서와 대조해 필요한 부분만 수정한다.

## ① 71763 양돈 생체 에너지 데이터 (2023) — JSON

정형 회귀에 최적. `annotations` 객체 구조:

| 그룹 | 필드 | 의미 |
|---|---|---|
| keypoint-top[] | pointcount, distance | 키포인트 개수·길이 |
| TextInfo | chamber-number, pig-number, weight, pig-classification, measure-date, measure-time | 챔버·개체·체중·분류(weaningpig/piglet/growing-pig/porker) |
| SensorData | T, RH, CO2, NH3, **breath-rate** | 환경센서 + 호흡수 |
| TemperatureData | rectal-, back-, neck-, head-temperature | 개체 부위별 온도 |
| FeedingAndManagementData | ventilation-rate, feedstuff-volume, watersupply, pig-manure, **sensibleHeat(현열량)**, **IatentHeat(잠열량)** | 사양관리 + 생체에너지 |

**타깃**: `breath_rate`(호흡수), `sensible_heat`(현열량), `latent_heat`(잠열량)
**피처**: 환경센서·개체온도·체중·사양관리·keypoint 길이
**검증**: 같은 개체(pig_id) 누수 방지 → `GroupKFold`
**모델 데모**: `python yangdon/src/model_71763.py [라벨디렉터리]`

## ② 71471 소·돼지 발정행동 데이터 — JSON ⭐ (중점 과제: 발정 탐지)

BBox / Keypoints / Polygon + 울음소리 + 외음부 + 3D. 파일명에 농장정보·발정시간·
채널·프레임수 인코딩. 발정여부 = 발정체크장비 + 전문가 검수.

행동분류(영문명): standing, lying, eating, head shaking, tailing, sitting …

### 발정 탐지 접근 (핵심)

발정은 **한 프레임이 아니라 시간에 걸친 행동·활동 변화**로 나타난다:
활동량↑, 기립(standing)·꼬리세움(tailing)↑, 눕는 시간(lying)↓.
따라서 **프레임 라벨을 개체(individual_id) 단위로 집계**해 분류한다.

| 단계 | 내용 |
|---|---|
| 파싱 | 프레임 단위 행 (individual_id, frame_idx, behavior, bbox, keypoint 중심/산포) |
| 피처 | 행동 비율 + **활동량**(프레임 간 중심 이동 평균/표준편차/최대) + 자세(종횡비·면적·산포) |
| 모델 | 개체당 1행 → GradientBoosting, StratifiedKFold |
| 지표 | ROC-AUC, F1, 정밀도, **재현율**(발정 놓치면 21일 손실 → 재현율 우선, 임계값 하향) |

**실행**: `python yangdon/src/model_71471_estrus.py [라벨디렉터리]`
합성 스키마 기준 데모: AUC≈0.72, 임계값 0.3에서 재현율≈0.78.

※ 양돈 과제이므로 **돼지·흑돼지만** 사용. 부가 모달(울음소리·외음부·3D)은
   확보 시 멀티모달로 확장(문서상 CRNN 멀티모달 발정분류 F1 0.90).

## ③ 622 지능형 스마트축사(양돈) — XML (CVAT)

라벨 형식이 **XML**(`annotations.xml`, CVAT 스타일). 공식 파이프라인도
`data_parsing.py`로 XML→JSON 변환 후 학습. 평가는 Pascal-VOC AP50.

```
<image name width height>
  <box    label xtl ytl xbr ybr/>
  <polygon label points="x,y;x,y;..."/>
  <points  label points="x,y;..."/>
```

라벨 = 농장·월령/상태: 이유자돈 전기/후기, 육성돈 전기/후기, 비육돈 전기/후기,
분만돈, 임신돈, 환돈. 농장: 야곱/삼성/대우/한돈혁신/바다.

| 과제 | 타깃 | 유형 |
|---|---|---|
| 개체 탐지·계수 | box | Object Detection (mAP/AP50) |
| 자세·형상 | polygon/points | Segmentation / Keypoint |
| 월령·상태 분류 | label | 분류 |

**피처**: bbox 크기, polygon 점 개수, 이미지 크기, 라벨(월령/상태)

---

## 파서 사용

```bash
python yangdon/src/parse_aihub.py --selftest              # 스키마 검증
python yangdon/src/parse_aihub.py 71763 <라벨디렉터리>     # JSON → CSV
python yangdon/src/parse_aihub.py 622   <라벨디렉터리>     # XML  → CSV
```
