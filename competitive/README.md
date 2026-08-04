# 양돈(養豚) AI 공모전 — 데이터 분석·모델링

스마트팜 양돈 데이터로 **생산성**과 **폐사 위험**을 예측하는 머신러닝 파이프라인.
공모전 실제 데이터가 확보되기 전, 전체 흐름(데이터 → EDA → 모델링 → 해석)을
바로 돌려볼 수 있는 **베이스라인 스캐폴드**다.

> ⚠️ 현재 `data/train.csv` 는 실제 데이터가 아니라 변수 간 관계를 의도적으로
> 심어 만든 **합성 데이터**다. 실제 공모전 데이터가 오면 같은 스키마의 CSV로
> 교체하기만 하면 이후 단계가 그대로 동작한다. (아래 "실제 데이터 연결" 참고)

## 다루는 과제

| 과제 | 타깃 | 유형 | 의미 |
|---|---|---|---|
| 생산성 예측 | `adg_kg_day` (일당증체량) | 회귀 | 사양·환경 조건별 성장 성능 |
| 위험 예측 | `mortality` (폐사 여부) | 분류 | 폐사 고위험 돈군 조기 식별 |

부수 지표로 `fcr`(사료요구율), `market_age_days`(출하일령)도 데이터에 포함.

## 폴더 구조

```
.claude/
  hooks/session-start.sh  # 새 세션마다 의존성 설치·상태 점검(SessionStart 훅)
  settings.json           # 훅 등록
competitive/
  README.md
  requirements.txt
  run_pipeline.sh    # 원커맨드: AI Hub 라벨 다운로드→추출→구조점검
  docs/
    AIHUB.md           # AI Hub 데이터 API 연동 가이드
    SCHEMA.md          # 3종 라벨 스키마 & 파서 설명
  src/
    aihub.py           # AI Hub 데이터 API 클라이언트(검색/트리/다운로드)
    parse_aihub.py     # 라벨(JSON/XML) → 정형 CSV 파서 + 스키마 합성/자체검증
    model_71763.py     # 71763 생체에너지 파싱→회귀(GroupKFold) 데모/실행
    generate_data.py   # 합성 양돈 스마트팜 데이터 생성
    eda.py             # 기초통계·상관·시각화
    train.py           # 베이스라인 모델링(회귀+분류) + 교차검증 + 특성중요도
  tests/
    smoke_test.py      # 의존성·클라이언트·파이프라인 스모크 테스트
  tools/
    aihubshell         # AI Hub 공식 다운로드 스크립트(v0.6)
  data/
    train.csv          # (생성물) 돈군 단위 데이터
  outputs/             # (생성물) EDA 표·그림, 모델 성능·특성중요도
```

## 실데이터 트랙 — Edinburgh Pig Behaviour (Kaggle)

AI Hub 71471은 국내 IP에서만 다운로드 가능(해외 클라우드 차단)이라, 원격에서
바로 실험 가능한 공개 데이터로 검증 트랙을 만들었다
([`docs/EDINBURGH.md`](docs/EDINBURGH.md)).

- Kaggle `jackbyte/edinburgh-pig-behaviour-annotated` — 개체·프레임별 bbox +
  행동 라벨 시계열 (영상 제외, output.json만 사용)
- `parse_edinburgh.py`(→71471 호환 프레임 스키마) + `model_edinburgh_behavior.py`
  (모션 피처 + 개체 분리 GroupKFold 행동 분류)
- **실데이터 베이스라인**: 12녹화·96개체·12,646프레임 → 정확도 0.43 /
  Macro-F1 0.33, 활동량(속도)이 핵심 피처 = 발정 관찰의 기반

```bash
pip install kaggle    # ~/.kaggle/kaggle.json 필요
python competitive/src/parse_edinburgh.py
python competitive/src/model_edinburgh_behavior.py competitive/data/edinburgh_frames.csv
```

## 웹 대시보드

`dashboard/index.html` — 단일 HTML(외부 라이브러리 없음, SVG 차트). 브라우저로 열면 끝.

```bash
python competitive/src/build_dashboard.py                       # 합성 시연 데이터로 생성
python competitive/src/build_dashboard.py <cctv_dir> <mgmt.csv> # 실데이터로 생성
```

기능:
- KPI: 후보돈 수, **전체 발정률**, CCTV 발정 미탐지 수, 무발정률, 융합 AUC
- 무발정 위험 입력구성별 AUC 비교(CCTV/관리/융합) · 주요 요인
- **농장별 발정률**(낮은 농장 = 관리 점검 필요)
- **이메일 발정/무발정 알람**: 이메일 입력 → 미탐지·고위험 개체 경보 메일 초안(mailto)
  구성 (실시간 자동발송은 SMTP 서버 연동 필요)
- **후보돈 목록**(위험도·농장 필터) → 개체 선택 시:
  - **개체별 발정**: 활동량·발정점수 시계열, **시간 윈도우 발정 시작점** 표시
    (임계 미달 지속 시 무발정 경보)
  - 개선 처방 + 관리요인 현황

## 새 세션에서 이어가기

이 저장소에는 **SessionStart 훅**(`.claude/hooks/session-start.sh`)이 있어,
Claude Code on the web에서 **새 세션이 시작될 때 의존성을 자동 설치**하고
`AIHUB_APIKEY` 등록 여부를 점검한다. 따라서 절차는:

1. AI Hub API 키 발급 + 데이터셋(71763·622·71471) 활용신청 승인
2. 원격 환경 설정의 **환경 시크릿**에 `AIHUB_APIKEY` 등록
3. **새 세션** 시작 → 훅이 자동으로 환경을 준비
4. `bash competitive/run_pipeline.sh` 로 라벨 다운로드→추출→구조점검
   (JSON 스키마 확인 후 파서로 `data/train.csv` 생성 → `eda.py`/`train.py`)

> 환경 시크릿은 **세션 시작 시 주입**되므로, 등록 후에는 반드시 **새 세션**에서
> 진행해야 키가 적용된다.

스모크 테스트: `python competitive/tests/smoke_test.py`

## 실제 데이터: AI Hub 연동

[AI Hub](https://www.aihub.or.kr) 데이터를 사용한다. **사용 확정 3종:**

| datasetkey | 이름 | 활용 |
|---|---|---|
| **71763** | 양돈 생체 에너지 데이터 (2023) | 생체·에너지 라벨 |
| **622** | 지능형 스마트축사 통합 데이터(양돈) | 탐지·자세(bbox/polygon/keypoint) |
| **71471** | 소·돼지 발정행동 데이터 (양돈만) | 발정행동·자세 |

API로 검색·다운로드하는 방법과 데이터셋별 라벨 filekey는
[`docs/AIHUB.md`](docs/AIHUB.md) 참고.

```bash
python competitive/src/aihub.py search 양돈       # 데이터셋 검색 (API 키 불필요)
python competitive/src/aihub.py tree 71763        # 파일 트리·filekey 확인 (키 불필요)
# 다운로드는 AIHUB_APIKEY 환경변수 + 데이터셋 활용신청 승인 필요
export AIHUB_APIKEY="발급받은_키"
python competitive/src/aihub.py download 71763 528771,528774   # 라벨링데이터만
```

> 원천데이터(영상)는 수 TB이므로 정형 분석/모델링에는 **라벨링데이터(주석 JSON)만**
> 받는다. 자세한 filekey·용량 주의사항은 `docs/AIHUB.md`.

### 라벨 스키마 & 파서 (데이터 도착 전 선작성 완료)

3종 라벨 구조를 AI Hub 문서에서 조사해 파서를 미리 작성해 두었다
([`docs/SCHEMA.md`](docs/SCHEMA.md)). 실데이터가 오면 파서만 통과시키면
바로 모델링에 들어간다.

```bash
python competitive/src/parse_aihub.py --selftest   # 스키마 합성 데이터로 파서 검증
python competitive/src/model_71763.py              # (합성) 파싱→생체에너지 회귀 데모
```

- **71471 발정 탐지 ⭐(중점)**: 프레임을 개체 단위로 집계 → 행동비율 +
  활동량(중심 이동) + 자세 피처로 발정 이진 분류. 재현율 우선(임계값 하향).
  데모 AUC≈0.72. `python competitive/src/model_71471_estrus.py`
- **후보돈 무발정·발정지연 위험 ⭐(예측+처방)**: 초교배 일령 경과 후보돈의
  무발정 위험을 사료·음수·시설·웅돈접촉·질병력·환경으로 예측하고, **개체별
  개선요인을 처방**. 데모 AUC≈0.66, 관리불량군 무발정률 43% vs 양호군 19%.
  `python competitive/src/model_gilt_anestrus.py`
- **통합 파이프라인 ⭐⭐ (CCTV→무발정→처방)**: CCTV 발정관찰(개체 시계열
  활동·행동) + 관리요인을 **융합**해 무발정 위험 예측 + 처방. 데모에서
  융합 AUC 0.71 > CCTV만 0.70 · 관리만 0.69 (두 소스가 상호보완).
  `python competitive/src/pipeline_gilt.py`
- **71763**: 환경센서·개체온도·체중·사양관리 → 호흡수/현열량/잠열량 회귀
  (같은 개체 누수 방지 GroupKFold). 데모 R²≈0.9(합성).
- **622**: CVAT XML 파싱, 개체 탐지·월령/상태 분류.

> **중점 과제 = 발정기 판단.** 발정 적기 포착은 번식효율(수태율)의 핵심이라
> 대회 임팩트가 크다. 자세한 접근은 [`docs/SCHEMA.md`](docs/SCHEMA.md) ②.

## 실행 방법

```bash
pip install -r competitive/requirements.txt

python competitive/src/generate_data.py   # data/train.csv 생성
python competitive/src/eda.py             # outputs/ 에 EDA 결과
python competitive/src/train.py           # 회귀+분류 모두 (reg / clf 인자로 개별 실행)
```

## 데이터 스키마 (돈군 = batch 단위 1행)

| 컬럼 | 설명 |
|---|---|
| `farm_id`, `house_id` | 농장·돈사 식별자 |
| `sex`, `breed` | 성별(거세/암), 교잡종 |
| `init_age_days`, `init_weight_kg` | 입식 일령·체중 |
| `avg_temp_c`, `humidity_pct`, `nh3_ppm`, `co2_ppm` | 비육기 돈사 환경 평균 |
| `stocking_density` | 사육밀도(두/m²) |
| `feed_intake_kg`, `feed_grade` | 두당 일일 사료섭취·사료등급 |
| `vaccinated`, `antibiotic_days` | 백신 접종 여부·항생제 투여일수 |
| `adg_kg_day` | **타깃(회귀)** 일당증체량 |
| `fcr`, `market_age_days` | 파생 지표(사료요구율·출하일령) |
| `mortality` | **타깃(분류)** 폐사 여부 |

## 베이스라인 성능 (합성 데이터, 5-fold CV)

| 과제 | 지표 | 값 |
|---|---|---|
| 회귀 (adg) | MAE / R² | ≈ 0.034 kg/day / ≈ 0.83 |
| 분류 (폐사) | ROC-AUC | ≈ 0.70 |

모델이 짚어낸 상위 요인이 데이터에 심어 둔 실제 인과와 일치한다:
- 증체 ← 사료섭취량(＋), 기온(고온 스트레스 −), 사료등급
- 폐사 ← 암모니아, 사육밀도, 고온 스트레스

즉 파이프라인이 신호를 제대로 학습함을 확인했다. (합성 데이터라 절대 수치보다
"흐름이 옳다"는 검증에 의미가 있다)

## 모델링 설계 메모

- **누수(leakage) 차단**: `adg` 예측 시 이로부터 파생된 `fcr`·`market_age_days`,
  그리고 다른 타깃 `mortality` 는 특성에서 제외.
- **전처리**: 수치형 표준화 + 범주형 원-핫을 `Pipeline` 안에 넣어 CV 각 fold에서
  독립적으로 적합 → 전처리 누수 방지.
- **교차검증**: 회귀 KFold(5), 분류 StratifiedKFold(5).
- **베이스라인 모델**: GradientBoosting. 실데이터 확보 후 XGBoost/LightGBM,
  하이퍼파라미터 탐색, 시계열/공간(농장) 분할 검증으로 확장 예정.

## 실제 데이터 연결

1. 공모전 데이터를 `data/train.csv` 로 저장 (위 스키마에 맞추거나,
   컬럼명이 다르면 `train.py`의 `LEAK_COLS`·타깃명만 수정).
2. `python competitive/src/eda.py` → 분포·결측·상관 점검.
3. `python competitive/src/train.py` → 베이스라인 성능 확인 후 개선.

## 로드맵

- [x] 합성 데이터 + end-to-end 파이프라인 (EDA·회귀·분류·특성중요도)
- [ ] 실제 공모전 데이터 연결 및 스키마 정합
- [ ] 부스팅 계열 모델·하이퍼파라미터 최적화
- [ ] 농장 단위 그룹 분할 검증(일반화 성능 정직하게 측정)
- [ ] 예측 결과 해석(SHAP) 및 현장 활용 시나리오
- [ ] (선택) 결과 대시보드 — 필요 시 단일 HTML로 제작
