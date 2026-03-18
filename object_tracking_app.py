import cv2
import time
from ultralytics import YOLO

# ==============================
# CONFIGURATION
# ==============================
MODEL_PATH = "yolov8m.pt"   # Best balance (accuracy + speed)
CONFIDENCE_THRESHOLD = 0.4
VIDEO_INPUT = 0             # 0 = webcam OR "video.mp4"
SAVE_OUTPUT = True
OUTPUT_FILE = "final_output.avi"

# ==============================
# LOAD MODEL
# ==============================
model = YOLO(MODEL_PATH)

# ==============================
# VIDEO CAPTURE
# ==============================
cap = cv2.VideoCapture(VIDEO_INPUT)

width = int(cap.get(3))
height = int(cap.get(4))
fps = int(cap.get(cv2.CAP_PROP_FPS)) or 30

# ==============================
# VIDEO WRITER
# ==============================
if SAVE_OUTPUT:
    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    out = cv2.VideoWriter(OUTPUT_FILE, fourcc, fps, (width, height))

# ==============================
# FPS SETUP
# ==============================
prev_time = 0

# ==============================
# MAIN LOOP
# ==============================
while True:
    ret, frame = cap.read()
    if not ret:
        break

    # ==========================
    # DETECTION + TRACKING
    # ==========================
    results = model.track(
        frame,
        conf=CONFIDENCE_THRESHOLD,
        persist=True,
        tracker="bytetrack.yaml"
    )

    annotated_frame = results[0].plot()

    # ==========================
    # OBJECT COUNT
    # ==========================
    if results[0].boxes.id is not None:
        ids = results[0].boxes.id.cpu().numpy()
        total_objects = len(ids)
    else:
        total_objects = 0

    # ==========================
    # FPS CALCULATION
    # ==========================
    current_time = time.time()
    fps_display = 1 / (current_time - prev_time) if prev_time != 0 else 0
    prev_time = current_time

    # ==========================
    # UI TEXT
    # ==========================
    cv2.putText(annotated_frame, f"FPS: {int(fps_display)}",
                (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.putText(annotated_frame, f"Objects: {total_objects}",
                (20, 80), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

    # ==========================
    # DISPLAY WINDOW
    # ==========================
    cv2.imshow("FINAL PRO Object Detection & Tracking", annotated_frame)

    # ==========================
    # SAVE OUTPUT
    # ==========================
    if SAVE_OUTPUT:
        out.write(annotated_frame)

    # ==========================
    # EXIT KEY
    # ==========================
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# ==============================
# RELEASE
# ==============================
cap.release()
if SAVE_OUTPUT:
    out.release()
cv2.destroyAllWindows()
