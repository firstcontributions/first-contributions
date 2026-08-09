"""자동 라벨링(pseudo-label) 재학습 — 국내 축사 영상으로 탐지기 도메인 적응.

문제: 탐지기는 공개 데이터(pig-detection, 대부분 해외 연구용 우리·부감 시점)로
학습됐다. 국내 상용 돈방(측면 시점·창살·스톨)은 도메인이 다르다. 그런데 국내
영상에는 **bbox 정답이 없다**.

해법(self-training): 현재 탐지기로 국내 영상을 **자동 라벨링**하고, 고신뢰
검출만 남겨 학습 데이터로 삼아 **파인튜닝**한다. 라벨 작업 없이 도메인 적응이 된다.

⚠️ 한계(정직하게): 자동 라벨은 **기존 오류를 강화**한다. 창살에 가려 한 마리가
두 박스로 쪼개진 것을 정답으로 배우면 더 쪼갠다. 이를 줄이려고
  · 높은 신뢰 임계(기본 0.6)만 채택
  · 프레임을 듬성듬성 샘플(중복 억제)
  · 원본 공개 데이터를 함께 섞어 학습(catastrophic forgetting 방지)
그래도 소량이라도 **사람이 검수한 라벨**이 있으면 그쪽이 항상 낫다.

    # 1) 영상에서 자동 라벨 데이터셋 만들기
    python competition/src/train_pseudo_label.py build <영상들...> --out /tmp/kr_pig
    # 2) 파인튜닝
    python competition/src/train_pseudo_label.py train /tmp/kr_pig --epochs 8
"""
from __future__ import annotations

import glob
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, HERE)
import analyze_video as av  # noqa: E402

BASE_DATA = ("/root/.cache/kagglehub/datasets/rbbbjp/"
             "pig-detection-yolo-dataset-mixed-sources/versions/1")
CONF_MIN = 0.6      # 자동 라벨 채택 임계(보수적으로)
FRAME_STEP = 10     # 프레임 샘플 간격(중복 억제)
VAL_RATIO = 0.2


def build_dataset(videos: list, out_dir: str, conf: float = CONF_MIN,
                  step: int = FRAME_STEP, model_path: str | None = None) -> dict:
    """영상들 → 자동 라벨 YOLO 데이터셋(images/labels, train/val 분할)."""
    import cv2
    from ultralytics import YOLO
    mp = av.find_model(model_path)
    if mp is None:
        raise FileNotFoundError("탐지 모델 없음 — competition/models/pig_yolo.pt")
    model = YOLO(mp)
    for split in ("train", "val"):
        os.makedirs(os.path.join(out_dir, split, "images"), exist_ok=True)
        os.makedirs(os.path.join(out_dir, split, "labels"), exist_ok=True)
    n_img = n_box = n_drop = 0
    for vi, video in enumerate(videos):
        cap = cv2.VideoCapture(video)
        stem = os.path.splitext(os.path.basename(video))[0].replace(" ", "_")
        fi = kept = 0
        while True:
            ok, img = cap.read()
            if not ok:
                break
            if fi % step:
                fi += 1
                continue
            fi += 1
            res = model.predict(img, imgsz=512, conf=0.25, verbose=False)[0]
            H, W = img.shape[:2]
            lines = []
            for (x1, y1, x2, y2), c in zip(res.boxes.xyxy.cpu().numpy(),
                                           res.boxes.conf.cpu().numpy()):
                if float(c) < conf:
                    n_drop += 1
                    continue
                cx, cy = (x1 + x2) / 2 / W, (y1 + y2) / 2 / H
                bw, bh = (x2 - x1) / W, (y2 - y1) / H
                if bw <= 0 or bh <= 0:
                    continue
                lines.append(f"0 {cx:.6f} {cy:.6f} {bw:.6f} {bh:.6f}")
            if not lines:          # 빈 프레임은 제외(배경만 학습시키지 않음)
                continue
            split = "val" if (kept % int(1 / VAL_RATIO) == 0) else "train"
            base = f"{stem}_{fi:06d}"
            cv2.imwrite(os.path.join(out_dir, split, "images", base + ".jpg"), img)
            open(os.path.join(out_dir, split, "labels", base + ".txt"),
                 "w").write("\n".join(lines) + "\n")
            kept += 1; n_img += 1; n_box += len(lines)
        cap.release()
        print(f"  [{vi+1}/{len(videos)}] {os.path.basename(video)} → {kept}장")
    # data.yaml (원본 공개 데이터를 함께 섞어 망각 방지)
    srcs = [s for s in ("bama2d", "compag2020", "compag2021", "faroseg", "hogs",
                        "multiview", "pigdata", "rgb")
            if os.path.isdir(os.path.join(BASE_DATA, s, "train", "images"))]
    yaml = [f"path: {out_dir}", "train:", "  - train/images"]
    yaml += [f"  - {BASE_DATA}/{s}/train/images" for s in srcs]
    yaml += ["val:", "  - val/images", "names:", "  0: pig"]
    open(os.path.join(out_dir, "data.yaml"), "w").write("\n".join(yaml) + "\n")
    return {"images": n_img, "boxes": n_box, "dropped_low_conf": n_drop,
            "yaml": os.path.join(out_dir, "data.yaml"), "mixed_sources": len(srcs)}


def finetune(data_yaml: str, epochs: int = 8, imgsz: int = 512,
             model_path: str | None = None, name: str = "pig_kr") -> str:
    """자동 라벨 데이터로 파인튜닝. 반환: best.pt 경로."""
    from ultralytics import YOLO
    mp = av.find_model(model_path)
    model = YOLO(mp)
    model.train(data=data_yaml, epochs=epochs, imgsz=imgsz, batch=16, workers=2,
                device="cpu", project="/tmp/pigdet/runs", name=name, exist_ok=True,
                val=True, plots=False, lr0=0.002)     # 낮은 lr = 미세 조정
    return f"/tmp/pigdet/runs/{name}/weights/best.pt"


def main() -> int:
    if len(sys.argv) < 3:
        print(__doc__)
        return 1
    cmd = sys.argv[1]
    if cmd == "build":
        args = sys.argv[2:]
        out = "/tmp/kr_pig"
        if "--out" in args:
            i = args.index("--out"); out = args[i + 1]; args = args[:i] + args[i + 2:]
        vids = [v for a in args for v in sorted(glob.glob(a))]
        if not vids:
            print("영상을 찾지 못했습니다."); return 1
        print(f"자동 라벨링: 영상 {len(vids)}개 → {out}")
        r = build_dataset(vids, out)
        print(f"완료: 이미지 {r['images']}장 · 박스 {r['boxes']}개 "
              f"(저신뢰 제외 {r['dropped_low_conf']}) · 공개 데이터 {r['mixed_sources']}소스 혼합")
        print(f"data.yaml: {r['yaml']}")
        return 0
    if cmd == "train":
        data = sys.argv[2]
        if os.path.isdir(data):
            data = os.path.join(data, "data.yaml")
        ep = 8
        if "--epochs" in sys.argv:
            ep = int(sys.argv[sys.argv.index("--epochs") + 1])
        print(f"파인튜닝: {data} ({ep} epochs)")
        print("완료 →", finetune(data, epochs=ep))
        return 0
    print(__doc__)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
