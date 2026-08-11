"""pigflow — 돈군흐름(배치 단위) 모델링 패키지.

설계 원칙(명세 §0):
  1. 개체가 아니라 **배치가 1급 객체**다. 모든 이동·계산은 배치 단위다.
  2. 돈방 1개 = 배치 1개. 서로 다른 배치를 섞지 않는다(AIAO).
  3. **역류 금지.** 뒤처진 돼지를 어린 배치로 되돌리는 이동은 위반이다.
  4. 공백기(세척·소독·건조)는 스테이지 점유일에 포함한다.
  5. 모든 기본값은 config 로 분리해 농장별로 덮어쓴다.

사용:
    cd competition   (또는 PYTHONPATH=competition, 저장소 루트에서 실행할 때)
    python -m pigflow                                    # 기본 설계·시뮬레이션
    python -m pigflow --config pigflow/example_farm.yaml # 농장 설정
    python pigflow/tests/test_pigflow.py                 # 검산 고정 테스트

한계(읽고 쓸 것):
  - **배치 1개 = 돈방 1개**로 모델링한다. 실제로는 한 배치를 여러 펜에 나누는
    농장이 많다(Config.allow_split 은 자리만 잡아 뒀고 아직 동작하지 않는다).
    그래서 "돈방"은 물리적 펜이 아니라 **한 배치를 통째로 받는 단위 공간**으로
    읽어야 한다.
  - 시뮬레이터는 분만율을 배치 생성 단계에서 이미 반영된 것으로 본다. 재발정·
    유산으로 분만틀이 비는 변동은 재현하지 않으므로 PSY/MSY 는 설계 상한이다.
  - duration_days·폐사율 기본값은 국내 관행 초기값이다. 농장 전산기록으로
    바꾸지 않으면 그 농장의 계산이 아니다(명세 §11).
"""
from .config import Config, load_config  # noqa: F401
from .models import Batch, MoveEvent, Room, RoomState, Stage  # noqa: F401

__all__ = ["Config", "load_config", "Batch", "MoveEvent", "Room",
           "RoomState", "Stage"]
