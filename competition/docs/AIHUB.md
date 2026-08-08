# AI Hub 데이터 API 연동 가이드

[AI Hub](https://www.aihub.or.kr)(NIA 운영) 데이터를 API로 조회·다운로드하는 방법.
프로젝트에 `src/aihub.py`(파이썬 클라이언트)와 `tools/aihubshell`(공식 스크립트 v0.6)을
포함해 두었다.

## API 구조 (공식 aihubshell v0.6 기준)

| 기능 | 엔드포인트 | 인증 |
|---|---|---|
| 데이터셋 목록 | `GET https://api.aihub.or.kr/info/dataset.do` | 불필요 |
| 파일 트리 | `GET https://api.aihub.or.kr/info/{datasetkey}.do` | 불필요 |
| 다운로드 | `GET https://api.aihub.or.kr/down/0.6/{datasetkey}.do?fileSn={filekeys}` | **`apikey` 헤더 필요** |

> 참고: info 엔드포인트는 HTTP 상태코드로 502를 반환하면서도 본문에는 정상
> 데이터를 담아 보낸다. 클라이언트는 이를 정상 처리한다(상태코드 무시, 본문 사용).

## 1. API 키 발급

1. AI Hub 회원가입/로그인
2. 마이페이지 → **API 키 발급/관리**에서 키 발급
3. 다운로드하려는 **각 데이터셋마다 '활용신청' 후 승인**을 받아야 다운로드 가능
   (목록·파일트리 조회는 승인 없이 가능)

## 2. API 키 설정 (보안)

⚠️ **API 키는 비밀값이다. 코드·커밋·채팅에 절대 넣지 말 것.** 환경변수로만 전달한다.

```bash
export AIHUB_APIKEY="발급받은_키"
```

- **Claude Code on the web(원격 환경)** 에서 반복 사용하려면, 환경 설정의
  **환경변수/시크릿**에 `AIHUB_APIKEY` 를 등록하면 세션마다 자동 주입된다.
- 원격 세션은 임시(ephemeral)이므로 셸에서 `export` 한 값은 세션 종료 시 사라진다.

## 3. 사용법

```bash
# 데이터셋 검색 (키 불필요)
python competition/src/aihub.py search 양돈

# 파일 트리 — 파일명 | 크기 | filekey 확인 (키 불필요)
python competition/src/aihub.py tree 71408

# 다운로드 — filekey를 콤마로 지정 (AIHUB_APIKEY 필요)
python competition/src/aihub.py download 71408 509489,509492
```

공식 스크립트를 직접 써도 된다:

```bash
bash competition/tools/aihubshell -mode l                     # 목록
bash competition/tools/aihubshell -mode l 71408               # 파일 트리
bash competition/tools/aihubshell -aihubapikey "$AIHUB_APIKEY" \
     -mode d -datasetkey 71408 -filekey 509489,509492     # 다운로드
```

## 4. 양돈 관련 데이터셋

`search` 로 확인된 주요 데이터셋:

| datasetkey | 이름 | 성격 |
|---|---|---|
| **622** | 지능형 스마트축사 통합 데이터(양돈) | 영상/CV (바운딩박스·폴리곤·키포인트) |
| **71408** | 양돈 생체 에너지 데이터 | 영상 + 생체 라벨 |
| **71763** | 양돈 생체 에너지 데이터 (2023) | 영상 + 생체 라벨 |
| 71471 | 소·돼지 발정행동 데이터 | 행동 영상 |
| 71322 | 축산 기자재(소, 돼지) 3D 데이터 | 3D |
| 145 | 가축 행동 영상 | 행동 영상 |

## 5. ⚠️ 용량 주의 — 정형 분석은 "라벨링데이터"만

원천데이터(영상)는 **파일 하나가 80~100GB**, 데이터셋 전체는 **수 TB**다.
`-filekey all` 로 받으면 안 된다(디스크·시간 폭발).

**데이터 분석/모델링에는 라벨링데이터(주석 JSON)만 받으면 충분하다.** 훨씬 작다.

예) `71408 양돈 생체 에너지 데이터`:

| 파일 | 크기 | filekey |
|---|---|---|
| Training 라벨링 `TL.zip` | 261 MB | 509489 |
| Validation 라벨링 `VL.zip` | 32 MB | 509492 |

```bash
python competition/src/aihub.py download 71408 509489,509492
```

압축 해제에는 데이터 크기의 2~3배 여유 공간이 필요하다.
(원격 샌드박스는 디스크 할당이 제한적이므로, 대용량 원천데이터는 로컬/서버에서 받는 것을 권장)

### 라벨링데이터 다운로드 치트시트 (사용 확정 3종)

키 발급 + 활용신청 승인 후, 아래 명령으로 **라벨링데이터만** 받는다.
원천데이터(영상)는 각 데이터셋이 수 TB이므로 받지 않는다.

#### ① 71763 양돈 생체 에너지 데이터 (2023) — 라벨 총 298MB

| 구분 | 파일 | 크기 | filekey |
|---|---|---|---|
| Training | TL.zip | 265 MB | 528771 |
| Validation | VL.zip | 33 MB | 528774 |

```bash
python competition/src/aihub.py download 71763 528771,528774
```

#### ② 622 지능형 스마트축사 통합 데이터(양돈) — 라벨 총 ~267MB

| 구분 | 유형 | 크기 | filekey |
|---|---|---|---|
| Training | 바운딩박스 | 148 MB | 533707 |
| Training | 폴리곤 | 77 MB | 533708 |
| Training | 키포인트 | 13 MB | 533709 |
| Validation | 바운딩박스 | 19 MB | 533717 |
| Validation | 폴리곤 | 8 MB | 533718 |
| Validation | 키포인트 | 2 MB | 533719 |

```bash
# 전체 라벨
python competition/src/aihub.py download 622 533707,533708,533709,533717,533718,533719
# 바운딩박스만 (탐지/계수 과제)
python competition/src/aihub.py download 622 533707,533717
```

#### ③ 71471 소·돼지 발정행동 데이터 — 양돈만(돼지+흑돼지) 선택 수신

이 데이터셋은 한우/젖소/돼지/흑돼지가 섞여 있다. **양돈 과제이므로 돼지·흑돼지
라벨만** 받는다. (한우·젖소는 제외)

| 구분 | 축종 | 유형 | 크기 | filekey |
|---|---|---|---|---|
| Training | 돼지 | bbox | 231 MB | 511410 |
| Training | 돼지 | keypoints | 28 MB | 511411 |
| Training | 돼지 | polygon | 163 MB | 511412 |
| Training | 흑돼지 | bbox | 92 MB | 511416 |
| Training | 흑돼지 | keypoints | 12 MB | 511417 |
| Training | 흑돼지 | polygon | 63 MB | 511418 |
| Validation | 돼지 | bbox | 29 MB | 511458 |
| Validation | 돼지 | keypoints | 4 MB | 511459 |
| Validation | 돼지 | polygon | 20 MB | 511460 |
| Validation | 흑돼지 | bbox | 12 MB | 511464 |
| Validation | 흑돼지 | keypoints | 1 MB | 511465 |
| Validation | 흑돼지 | polygon | 8 MB | 511466 |

부가 라벨(외음부이미지·3D이미지·울음소리)도 있으나 용량이 작다. 발정행동
분석에는 외음부·울음소리도 신호가 될 수 있어 필요 시 추가:
돼지 511413(외음부)/511414(3D)/511415(울음소리),
흑돼지 511419/511420/511421 (Validation: 511461~511463 / 511467~511469).

```bash
# 돼지+흑돼지 핵심 라벨(bbox+keypoints+polygon)
python competition/src/aihub.py download 71471 \
  511410,511411,511412,511416,511417,511418,\
511458,511459,511460,511464,511465,511466
# keypoints만 (자세/행동 분석)
python competition/src/aihub.py download 71471 511411,511417,511459,511465
```

> filekey는 데이터셋 갱신 시 바뀔 수 있으니, 받기 전에
> `python competition/src/aihub.py tree <datasetkey>` 로 최신값을 확인할 것.
> (참고: 71408 '양돈 생체 에너지 데이터'(2023 이전판) 라벨은 509489/509492)

## 6. 다운로드 후

`aihubshell` 이 `download.tar` 를 내려받아 자동으로 압축 해제하고, 분할된
`.partNN` 조각을 병합한 뒤 정리한다. 압축을 풀면 라벨링 JSON이 나오며, 이를
`src/` 파이프라인의 정형 데이터로 가공해 `data/train.csv` 형태로 만들어
`eda.py` / `train.py` 에 연결하면 된다.

## 7. ⚠️ 해외 다운로드 제한(지역 차단)과 해결법

AI Hub는 **데이터 다운로드를 국내 IP에서만** 허용한다. 조회는 되지만 다운로드는 막힌다.

| 단계 | 해외 IP(원격 샌드박스) |
|---|---|
| 데이터셋 검색 / 파일 트리 | ✅ 정상 |
| API 키 인증 | ✅ 통과 |
| **데이터 다운로드** | ❌ `HTTP 502` — `AI 허브는 해외에서의 데이터 다운로드를 제한하고 있습니다.` |

즉 이 원격 환경(프록시=해외 IP)에서는 키가 유효해도 71471을 못 받는다. 키·권한이
아니라 **접속 위치** 문제다.

### 해결 절차 (국내망 1회 다운로드 → 자동 실측 검증)

1. **국내망**(한국 내 PC/서버, 또는 국내 리전 클라우드 VM)에서 키를 설정하고
   위 §5-③의 **돼지 라벨만** 받는다. 발정 검증에는 keypoints/bbox면 충분(수십 MB):

   ```bash
   export AIHUB_APIKEY="발급받은_키"
   # 돼지 Validation 라벨(가장 가벼움): bbox+keypoints
   python competition/src/aihub.py download 71471 511458,511459
   ```

2. 받은 라벨 JSON을 프로젝트의 아래 경로에 둔다(디렉터리째 복사):

   ```
   competition/data/aihub/71471/
   ```

   (또는 임의 위치에 두고 `export AIHUB_71471_DIR=/받은/경로` 로 지정)

3. 그러면 **파이프라인이 자동으로 실측 발정 AUC를 채운다.** 별도 코드 수정 불필요:

   ```bash
   python competition/src/validate_estrus_reference.py   # 보정 AUC vs 규칙 baseline
   python competition/src/build_eval_report.py           # 리포트 D 섹션이 실측으로 교체
   ```

   - 파일이 **없으면**: 리포트 D 섹션은 "합성 시연"으로 표시되고 국내망 안내 배너가 뜬다.
   - 파일이 **있으면**: 같은 자리에 실측 AUC + ROC/PR/보정곡선이 자동 렌더된다.

> 요약: 코드(로더·보정·리포트 슬롯)는 이미 완성되어 대기 중이다. 국내망에서 라벨
> 파일만 한 번 떨어뜨리면 발정 실측 검증이 그대로 돌아간다.

### 실제 라벨 스키마 (확인 완료, 2022 labelon 배포본)

실데이터를 받아 확인한 결과 스키마는 **대문자 키 + 프레임(이미지) 1개당 JSON 1개**다.
`src/parse_71471_real.py` 가 이 스키마를 파싱한다.

```json
{"INFO": {"DATASET_NAME": "[Bbox]돼지(백돼지) 발정행동 데이터", "VERSION": "1.0"},
 "IMAGE": {"IMAGE_FILE_NAME": "pigfarmA_ch9_2022092109_20-85_160700.jpg",
           "WIDTH": 1920, "HEIGHT": 1080, "TIMESTAMP": 160700,
           "FARMID": "pigfarmA", "HEADCOUNT": 500, "RECORD_TIME": 23},
 "ANNOTATION_INFO": [
   {"ID": 122946126,
    "BOUNDING_BOX_X_COORDINATE": 142, "BOUNDING_BOX_Y_COORDINATE": 455,
    "BOUNDING_BOX_WIDTH": 363, "BOUNDING_BOX_HEIGHT": 260,
    "CATEGORY_NAME": "pig", "ACTION_NAME": "lying", "ESTRUS": "N"}]}
```

핵심 포인트:
- **`ESTRUS`("Y"/"N")가 bbox(개체 인스턴스)별 정답 라벨** → 발정 지도학습의 근거.
- `ACTION_NAME` = 행동 라벨(lying/standing/eating/head shaking/tailing/sitting).
- **개체 추적 ID 는 없다**(`ID`는 주석 고유번호). 개체 단위 집계가 필요하면
  `iou_tracker` 로 프레임 간 ID 를 부여한다. 발정 검증은 인스턴스 단위로 바로 가능.
- 파일명 규칙: `{farm}_{channel}_{yyyymmddHH}_{pen}_{timestamp}.json`
  → 세션(농장+채널+일시)을 **누수 방지 GroupKFold 그룹 키**로 사용한다.

```bash
python competition/src/parse_71471_real.py <라벨디렉터리>     # 파싱·요약
python competition/src/validate_estrus_reference.py <라벨디렉터리>  # 실측 발정 AUC
```

### ⚠️ 중요 — ESTRUS 는 **개체 라벨이 아니라 돈방/카메라 라벨**이다

실데이터(800파일·6,158 bbox·13세션) 검증에서 확인한 구조적 함정:

| 채널 | 세션 수 | 발정 비율 |
|---|---|---|
| `ch1` | 5 | **100%** (전부 Y) |
| `ch10` | 8 | **0%** (전부 N) |

**발정 라벨이 카메라 채널과 1:1로 교락**되어 있다. 즉 71471은 "발정 모돈이 있는
돈방"과 "없는 돈방"을 각각 다른 카메라로 촬영한 구성이며, `ESTRUS` 는 그 프레임이
어느 돈방인지를 나타낸다(개별 돼지의 발정 여부가 아니다).

결과적으로:
- bbox 기하(위치·크기)를 피처로 쓰면 **AUC ≈ 1.0** 이 나오지만, 이는 발정 인식이
  아니라 **카메라 화각 식별**이다 → **누수**.
- 채널을 그룹으로 분리하면 학습 폴드에 한 클래스만 남아 **지도검증 자체가 불가능**.
- 행동 라벨(`ACTION_NAME`)만으로 본 정직한 분리력은 **AUC 0.523 — 사실상 무작위**.
  (행동별 발정률: eating 0.51 · sitting 0.45 · lying 0.37 · standing 0.37)

`validate_estrus_reference.py` 는 이 교락을 **자동 탐지**해 AUC 1.0 을 보고하지 않고
경고와 함께 규칙 baseline 만 제시한다.

**유효한 발정 검증에 필요한 것**
1. 같은 돈방/카메라에서 **발정·비발정이 함께 관측**된 표본, 또는
2. 같은 개체의 **시간적 전이**(비발정 → 발정)를 담은 시계열, 또는
3. 프레임 정지영상이 아닌 **동영상 기반 행동 변화**(활동량 급증 등)

> 교훈: 라벨이 있다고 바로 지도학습에 넣으면 안 된다. 라벨이 어느 수준(개체/돈방/
> 촬영세션)에 붙어 있는지 먼저 확인해야 한다.

## 출처

- [AI 허브 오픈 API 'aihubshell' 이용안내](https://www.aihub.or.kr/devsport/apishell/list.do)
- 스크립트 원본: `https://api.aihub.or.kr/api/aihubshell.do` (v0.6, 25.09.19)
