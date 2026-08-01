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
python yangdon/src/aihub.py search 양돈

# 파일 트리 — 파일명 | 크기 | filekey 확인 (키 불필요)
python yangdon/src/aihub.py tree 71408

# 다운로드 — filekey를 콤마로 지정 (AIHUB_APIKEY 필요)
python yangdon/src/aihub.py download 71408 509489,509492
```

공식 스크립트를 직접 써도 된다:

```bash
bash yangdon/tools/aihubshell -mode l                     # 목록
bash yangdon/tools/aihubshell -mode l 71408               # 파일 트리
bash yangdon/tools/aihubshell -aihubapikey "$AIHUB_APIKEY" \
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
python yangdon/src/aihub.py download 71408 509489,509492
```

압축 해제에는 데이터 크기의 2~3배 여유 공간이 필요하다.
(원격 샌드박스는 디스크 할당이 제한적이므로, 대용량 원천데이터는 로컬/서버에서 받는 것을 권장)

## 6. 다운로드 후

`aihubshell` 이 `download.tar` 를 내려받아 자동으로 압축 해제하고, 분할된
`.partNN` 조각을 병합한 뒤 정리한다. 압축을 풀면 라벨링 JSON이 나오며, 이를
`src/` 파이프라인의 정형 데이터로 가공해 `data/train.csv` 형태로 만들어
`eda.py` / `train.py` 에 연결하면 된다.

## 출처

- [AI 허브 오픈 API 'aihubshell' 이용안내](https://www.aihub.or.kr/devsport/apishell/list.do)
- 스크립트 원본: `https://api.aihub.or.kr/api/aihubshell.do` (v0.6, 25.09.19)
