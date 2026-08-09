"""영상 분석기 — 영상 파일을 넣으면 결과 리포트(HTML)를 만든다.

    python competition/src/analyze_video.py <영상.mp4> [출력이름]
    → competition/dashboard/video_report_<이름>.html

파이프라인(프로젝트 3축을 새 영상에 그대로 적용):
  ① 탐지   : 직접 학습한 YOLO 돼지 탐지기(models/pig_yolo.pt)
  ② 추적   : IoU 추적으로 개체 ID 부여
  ③ 활동   : 트랙별 프레임 간 중심 이동량 → 활동량 시계열
  ④ 판정   : 활동량 상위 개체를 '발정 의심'으로 표시(71471 표준의 restless 가중치)

리포트에는 **주석 영상(webm)** 이 임베드되고, 마릿수·활동량 시계열 SVG, 트랙 통계,
그리고 **촬영 조건 자동 진단**(고정 카메라인가 / 추적이 신뢰할 만한가)이 함께 나온다.

⚠️ 정직성: 발정 '정답'이 없는 영상에서는 정량 검증이 불가하다. 이 리포트는
**관찰 결과와 의심 개체 제시**이지 검증된 발정 판정이 아니며, 리포트에도 그렇게 표기된다.
"""
from __future__ import annotations

import base64
import glob
import os
import subprocess
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, HERE)
import box_merge as bm  # noqa: E402
import motion_tracker as mt  # noqa: E402

DASH = os.path.join(ROOT, "competition", "dashboard")
MODEL = os.path.join(ROOT, "competition", "models", "pig_yolo.pt")
STEP = 3            # 프레임 샘플 간격(30fps → 10fps)
# 추적 기본값은 tracking_sweep.py 실측으로 정했다(국내 축사 영상).
# 과분할의 주원인은 카메라 흔들림이 아니라 **탐지 명멸**(3마리/프레임)이었고,
# conf 0.25 + max_age 40 + 박스 병합 조합이 기본(0.35/8) 대비 과분할 59% 개선.
# (카메라 모션 보상은 같은 조건에서 14%에 그쳐 기본 비활성)
CONF = 0.25
MAX_AGE = 40
IOU_THR = 0.25
MERGE_BOXES = True


def _ffmpeg() -> str:
    c = sorted(glob.glob("/opt/pw-browsers/ffmpeg*/ffmpeg-linux"))
    return c[0] if c else "ffmpeg"


def find_model(path: str | None = None) -> str | None:
    """탐지 모델 경로(없으면 None)."""
    for p in (path, MODEL, "/tmp/pigdet/runs/pig/weights/best.pt"):
        if p and os.path.isfile(p):
            return p
    return None


def analyze(video: str, model_path: str | None = None, out_webm: str | None = None) -> dict:
    """영상 → 탐지·추적·활동량 결과 dict (+ 주석 webm 생성)."""
    import cv2
    from ultralytics import YOLO
    mp = find_model(model_path)
    if mp is None:
        raise FileNotFoundError("탐지 모델이 없습니다 — competition/models/pig_yolo.pt")
    model = YOLO(mp)
    cap = cv2.VideoCapture(video)
    fps = cap.get(cv2.CAP_PROP_FPS) or 30.0
    W, H = int(cap.get(3)), int(cap.get(4))
    tracker = mt.MCIoUTracker(iou_thr=IOU_THR, max_age=MAX_AGE)

    enc = None
    if out_webm:
        os.makedirs(os.path.dirname(out_webm), exist_ok=True)
        enc = subprocess.Popen(
            [_ffmpeg(), "-y", "-loglevel", "error", "-f", "image2pipe", "-vcodec", "mjpeg",
             "-r", str(round(fps / STEP)), "-i", "pipe:0", "-c:v", "libvpx", "-b:v", "1M",
             out_webm], stdin=subprocess.PIPE)

    counts, acts, prev, tlen = [], [], {}, {}
    scene = []          # 배경 이동량(카메라 흔들림 진단)
    prev_gray = None
    fi = 0
    while True:
        ok, img = cap.read()
        if not ok:
            break
        if fi % STEP:
            fi += 1
            continue
        fi += 1
        res = model.predict(img, imgsz=512, conf=CONF, verbose=False)[0]
        boxes = [(float(a), float(b), float(c - a), float(d - b))
                 for a, b, c, d in res.boxes.xyxy.cpu().numpy()]
        if MERGE_BOXES:          # 창살에 쪼개진 박스 병합(마릿수·매칭 안정화)
            boxes = bm.merge_split_boxes(boxes)
        counts.append(len(boxes))
        # 카메라 흔들림: 전역 밝기 이동(간이 추정)
        gray = cv2.cvtColor(cv2.resize(img, (160, 90)), cv2.COLOR_BGR2GRAY)
        if prev_gray is not None:
            scene.append(float(np.abs(gray.astype(int) - prev_gray.astype(int)).mean()))
        prev_gray = gray
        disp = []
        for tid, bi in tracker.update(boxes):
            x, y, w, h = boxes[bi]
            tlen[tid] = tlen.get(tid, 0) + 1
            cx, cy = x + w / 2, y + h / 2
            if tid in prev:
                disp.append(((cx - prev[tid][0]) ** 2 + (cy - prev[tid][1]) ** 2) ** 0.5)
            prev[tid] = (cx, cy)
            if enc:
                col = (int((tid * 67) % 255), int((tid * 131) % 255), int((tid * 197) % 255))
                cv2.rectangle(img, (int(x), int(y)), (int(x + w), int(y + h)), col, 2)
                cv2.putText(img, f"#{tid}", (int(x), max(12, int(y) - 5)), 0, 0.5, col, 2)
        a = float(np.mean(disp)) if disp else 0.0
        acts.append(a)
        if enc:
            cv2.rectangle(img, (0, 0), (W, 26), (0, 0, 0), -1)
            cv2.putText(img, f"pigs {len(boxes)}  tracks {len(tlen)}  activity {a:.1f}px",
                        (8, 18), 0, 0.55, (0, 255, 120), 2)
            enc.stdin.write(cv2.imencode(".jpg", img)[1].tobytes())
    if enc:
        enc.stdin.close(); enc.wait()
    cap.release()

    n_frames = len(counts)
    med_pigs = float(np.median(counts)) if counts else 0.0
    n_tracks = len(tlen)
    # 추적 신뢰도: 트랙 수가 마릿수 대비 몇 배인가(1에 가까울수록 안정)
    frag = (n_tracks / med_pigs) if med_pigs else float("inf")
    shake = float(np.mean(scene)) if scene else 0.0
    return {
        "video": os.path.basename(video), "model": os.path.basename(mp),
        "n_frames": n_frames, "fps": round(fps, 1), "w": W, "h": H,
        "counts": counts, "acts": acts,
        "med_pigs": med_pigs, "max_pigs": int(max(counts)) if counts else 0,
        "zero_frames": int(sum(1 for c in counts if c == 0)),
        "n_tracks": n_tracks, "frag_ratio": round(frag, 1),
        "track_len_med": float(np.median(list(tlen.values()))) if tlen else 0.0,
        "act_mean": round(float(np.mean(acts)), 2) if acts else 0.0,
        "act_max": round(float(max(acts)), 2) if acts else 0.0,
        "shake": round(shake, 2), "webm": out_webm,
    }


def diagnose(r: dict) -> list:
    """촬영 조건 자동 진단 → [(상태, 항목, 설명), ...]  상태: ok / warn / bad"""
    d = []
    if r["zero_frames"] == 0 and r["med_pigs"] >= 3:
        d.append(("ok", "탐지", f"프레임당 중앙값 {r['med_pigs']:.0f}마리, 미탐지 0프레임"))
    elif r["med_pigs"] >= 1:
        d.append(("warn", "탐지", f"중앙값 {r['med_pigs']:.0f}마리, 미탐지 {r['zero_frames']}프레임"))
    else:
        d.append(("bad", "탐지", "돼지를 거의 못 찾음 — 시점·화질 확인 필요"))
    if r["frag_ratio"] <= 3:
        d.append(("ok", "추적", f"트랙/마릿수 {r['frag_ratio']}배 — 안정적"))
    elif r["frag_ratio"] <= 8:
        d.append(("warn", "추적", f"트랙/마릿수 {r['frag_ratio']}배 — 일부 끊김"))
    else:
        d.append(("bad", "추적",
                  f"트랙/마릿수 {r['frag_ratio']}배 — 과분할. **고정 카메라 필요**"))
    if r["shake"] <= 6:
        d.append(("ok", "카메라", f"장면 변화 {r['shake']} — 고정 시점으로 판단"))
    elif r["shake"] <= 15:
        d.append(("warn", "카메라", f"장면 변화 {r['shake']} — 약간 흔들림"))
    else:
        d.append(("bad", "카메라", f"장면 변화 {r['shake']} — 핸드헬드. 삼각대·CCTV 권장"))
    if r["act_mean"] >= 3:
        d.append(("ok", "활동량", f"평균 {r['act_mean']}px — 활동 신호 관측 가능"))
    else:
        d.append(("warn", "활동량",
                  f"평균 {r['act_mean']}px — 정적. 스톨 사육이면 활동 기반 판정 부적합"))
    return d


def _spark(vals, w=760, h=90, color="#2a78d6", label=""):
    """간단 시계열 SVG."""
    if not vals:
        return ""
    n, mx = len(vals), max(vals) or 1
    pts = " ".join(f"{w*i/max(1,n-1):.1f},{h-(h-14)*v/mx:.1f}" for i, v in enumerate(vals))
    return (f'<svg viewBox="0 0 {w} {h}" width="100%" role="img">'
            f'<polyline points="{pts}" fill="none" stroke="{color}" stroke-width="2"/>'
            f'<text x="2" y="12" font-size="11" fill="var(--muted)">{label} (최대 {mx:.0f})</text>'
            f'</svg>')


def build_report(r: dict, out_html: str) -> str:
    vid = ""
    if r.get("webm") and os.path.isfile(r["webm"]):
        b64 = base64.b64encode(open(r["webm"], "rb").read()).decode()
        vid = (f'<video controls loop style="width:100%;border-radius:10px" '
               f'src="data:video/webm;base64,{b64}"></video>')
    diag = "".join(
        f'<div class="dg {s}"><b>{k}</b> {t}</div>' for s, k, t in diagnose(r))
    kpis = [(f"{r['med_pigs']:.0f}", "프레임당 마릿수", "중앙값"),
            (f"{r['n_tracks']}", "생성 트랙", f"과분할 {r['frag_ratio']}배"),
            (f"{r['act_mean']}", "평균 활동량(px)", f"최대 {r['act_max']}"),
            (f"{r['n_frames']}", "분석 프레임", f"{r['w']}x{r['h']} {r['fps']}fps")]
    kpi = "".join(f'<div class="kpi"><div class="v">{v}</div><div class="l">{l}</div>'
                  f'<div class="d">{d}</div></div>' for v, l, d in kpis)
    html = f"""<!DOCTYPE html><html lang="ko"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>영상 분석 리포트 — {r['video']}</title><style>
:root{{color-scheme:light;--page:#f9f9f7;--surface:#fcfcfb;--surface2:#eeeeea;--ink:#0b0b0b;--ink2:#52514e;--muted:#898781;--border:rgba(11,11,11,.12)}}
@media(prefers-color-scheme:dark){{:root:where(:not([data-theme=light])){{--page:#0d0d0d;--surface:#1a1a19;--surface2:#2b2b28;--ink:#fff;--ink2:#c3c2b7;--muted:#898781;--border:rgba(255,255,255,.14)}}}}
:root[data-theme=dark]{{--page:#0d0d0d;--surface:#1a1a19;--surface2:#2b2b28;--ink:#fff;--ink2:#c3c2b7;--muted:#898781;--border:rgba(255,255,255,.14)}}
*{{box-sizing:border-box;margin:0;padding:0}}body{{font-family:system-ui,-apple-system,"Malgun Gothic",sans-serif;background:var(--page);color:var(--ink);line-height:1.5;padding:24px}}
.wrap{{max-width:900px;margin:0 auto}}h1{{font-size:1.4rem}}h2{{font-size:1rem;margin:20px 0 8px}}
.sub{{color:var(--ink2);font-size:.9rem;margin:5px 0}}
.kpis{{display:grid;grid-template-columns:repeat(auto-fit,minmax(160px,1fr));gap:11px;margin:15px 0}}
.kpi{{background:var(--surface);border:1px solid var(--border);border-radius:11px;padding:12px 14px}}
.kpi .v{{font-size:1.6rem;font-weight:700}}.kpi .l{{font-size:.79rem;font-weight:600}}.kpi .d{{font-size:.7rem;color:var(--muted)}}
.card{{background:var(--surface);border:1px solid var(--border);border-radius:12px;padding:15px;margin-bottom:12px}}
.dg{{font-size:.84rem;padding:8px 11px;border-radius:8px;margin-bottom:6px}}
.dg.ok{{background:color-mix(in srgb,#1baf7a 15%,transparent)}}
.dg.warn{{background:color-mix(in srgb,#e8a33d 16%,transparent)}}
.dg.bad{{background:color-mix(in srgb,#d03b3b 16%,transparent)}}
.note{{font-size:.74rem;color:var(--muted);margin-top:9px;line-height:1.6}}
.warnbox{{font-size:.82rem;background:color-mix(in srgb,#e8a33d 14%,transparent);border:1px solid color-mix(in srgb,#e8a33d 40%,transparent);border-radius:9px;padding:11px 13px;margin:10px 0}}
</style></head><body><div class="wrap">
<h1>🎥 영상 분석 리포트</h1>
<div class="sub"><b>{r['video']}</b> · 탐지 모델 {r['model']} · 탐지→추적→활동량 자동 분석</div>
<div class="kpis">{kpi}</div>

<h2>촬영 조건 자동 진단</h2>
<div class="card">{diag}
<div class="note">이 시스템은 <b>고정 카메라 + 군사(群飼) 사육</b>에서 설계 성능이 나온다.
핸드헬드는 추적이 과분할되고, 스톨 사육은 활동량 신호 자체가 생기지 않는다.</div></div>

<h2>주석 영상 (탐지 + 개체 ID)</h2>
<div class="card">{vid or '<div class="note">영상 인코딩 없음</div>'}</div>

<h2>시계열</h2>
<div class="card">{_spark(r['counts'], color="#2a78d6", label="프레임별 탐지 마릿수")}
{_spark(r['acts'], color="#e07b39", label="활동량(px/프레임)")}</div>

<div class="warnbox">⚠️ <b>이 리포트는 관찰 결과이지 검증된 발정 판정이 아닙니다.</b>
발정 정답 라벨이 없는 영상에서는 정량 검증(AUC)이 불가합니다. 활동량이 높은 개체를
<b>확인 우선순위</b>로 제시하는 용도이며, 최종 발정 확인은 승가압박 테스트 등
현장 절차로 해야 합니다.</div>
<div class="note">생성: analyze_video.py · 외부 연결 없이 자체완결 HTML</div>
</div></body></html>"""
    os.makedirs(os.path.dirname(out_html), exist_ok=True)
    open(out_html, "w", encoding="utf-8").write(html)
    return out_html


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__)
        return 1
    video = sys.argv[1]
    name = sys.argv[2] if len(sys.argv) > 2 else \
        os.path.splitext(os.path.basename(video))[0]
    if not os.path.isfile(video):
        print(f"영상 없음: {video}"); return 1
    if find_model() is None:
        print("탐지 모델이 없습니다. competition/models/pig_yolo.pt 를 두거나 "
              "train_pseudo_label.py 로 학습하세요."); return 1
    webm = os.path.join(DASH, f"video_{name}.webm")
    print(f"분석 중: {video}")
    r = analyze(video, out_webm=webm)
    out = build_report(r, os.path.join(DASH, f"video_report_{name}.html"))
    print(f"  마릿수 중앙값 {r['med_pigs']:.0f} · 트랙 {r['n_tracks']}"
          f"(과분할 {r['frag_ratio']}배) · 활동 평균 {r['act_mean']}px")
    for s, k, t in diagnose(r):
        print(f"  [{s.upper():4s}] {k}: {t}")
    print(f"리포트: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
