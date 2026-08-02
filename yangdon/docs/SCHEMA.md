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

## ② 71471 소·돼지 발정행동 데이터 — JSON

BBox / Keypoints / Polygon + 울음소리 + 외음부 + 3D. 파일명에 농장정보·발정시간·
채널·프레임수 인코딩. 발정여부 = 발정체크장비 + 전문가 검수.

행동분류(영문명): standing, lying, eating, head shaking, tailing, sitting …

| 과제 | 타깃 | 유형 |
|---|---|---|
| 발정 탐지 | estrus(0/1) | 이진 분류 |
| 행동 분류 | behavior | 다중 분류 |

**피처**: keypoint 기반 자세(폭·높이·비율), bbox, 종(pig/blackpig)
※ 양돈 과제이므로 **돼지·흑돼지만** 사용.

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
