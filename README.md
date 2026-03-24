# 🎯 Real-Time Object Detection and Tracking

[![Contributors](https://img.shields.io/github/contributors/khushi-Jag/ApexcifyTechnologys_-Object-Detection-and-Tracking-)](https://github.com/khushi-Jag/ApexcifyTechnologys_-Object-Detection-and-Tracking-/graphs/contributors)
[![Forks](https://img.shields.io/github/forks/khushi-Jag/ApexcifyTechnologys_-Object-Detection-and-Tracking-)](https://github.com/khushi-Jag/ApexcifyTechnologys_-Object-Detection-and-Tracking-/network/members)
[![Stars](https://img.shields.io/github/stars/khushi-Jag/ApexcifyTechnologys_-Object-Detection-and-Tracking-)](https://github.com/khushi-Jag/ApexcifyTechnologys_-Object-Detection-and-Tracking-/stargazers)
[![Issues](https://img.shields.io/github/issues/khushi-Jag/ApexcifyTechnologys_-Object-Detection-and-Tracking-)](https://github.com/khushi-Jag/ApexcifyTechnologys_-Object-Detection-and-Tracking-/issues)
[![License](https://img.shields.io/github/license/khushi-Jag/ApexcifyTechnologys_-Object-Detection-and-Tracking-)](https://github.com/khushi-Jag/ApexcifyTechnologys_-Object-Detection-and-Tracking-/blob/main/LICENSE)

> A **real-time object detection and multi-object tracking** system powered by YOLOv8 and OpenCV — capable of identifying 80 COCO object categories from a live webcam stream while maintaining persistent tracking IDs across frames.

---

## 📌 Table of Contents

* [About The Project](#-about-the-project)
* [Key Features](#-key-features)
* [Built With](#-built-with)
* [Model Details](#-model-details)
* [How It Works](#-how-it-works)
* [Project Structure](#-project-structure)
* [Getting Started](#-getting-started)
* [Usage](#-usage)
* [Contributing](#-contributing)
* [License](#-license)
* [Contact](#-contact)

---

## 💡 About The Project

This project delivers a **real-time object detection and tracking pipeline** built on top of **YOLOv8** (Ultralytics) and **OpenCV**. It reads live video from a webcam or a local video file, runs YOLOv8's integrated ByteTrack tracker on each frame, and overlays bounding boxes, class labels, confidence scores, and unique tracking IDs directly onto the output — all happening in real time.

The system can recognize **80 object categories** drawn from the COCO dataset — including people, vehicles, animals, and common household items — and reliably tracks each object across consecutive frames with stable, consistent IDs, even when they briefly exit the camera's field of view.

---

## ✨ Key Features

* **Live Inference** — Processes frames directly from a webcam feed with minimal latency.
* **Multi-Object Tracking** — Tracks several objects simultaneously, each assigned a unique persistent ID.
* **80 COCO Classes** — Recognizes a wide variety of objects including people, cars, animals, and everyday items.
* **Stable Track IDs** — Tracking identifiers remain consistent even when objects temporarily leave the frame.
* **Flexible Input Sources** — Works seamlessly with both live webcam streams and pre-recorded video files.
* **Lightweight Codebase** — The entire implementation fits in under 50 lines of clean, readable Python.

---

## 🛠 Built With

| Technology | Purpose |
|---|---|
| Python 3.8+ | Core programming language |
| YOLOv8 (Ultralytics) | State-of-the-art real-time object detection |
| OpenCV (`opencv-python`) | Video capture, frame rendering & display |
| ByteTrack | Multi-object tracker integrated within Ultralytics |
| COCO Dataset Weights | Pre-trained on 80 diverse object categories |

---

## 📦 Model Details

| Property | Value |
|---|---|
| **Model** | YOLOv8 Nano (`yolov8n.pt`) |
| **Training Dataset** | COCO (Common Objects in Context) |
| **Number of Classes** | 80 |
| **Model Size** | ~6.5 MB |
| **Tracker** | ByteTrack (Ultralytics default) |
| **Speed** | Optimized for real-time CPU inference |

> The **Nano** variant is selected for its fast CPU inference speed. Larger variants (`yolov8s`, `yolov8m`, `yolov8l`, `yolov8x`) deliver improved accuracy but require more compute.

---

## 🧠 How It Works

```
Webcam / Video File
        │
        ▼
Frame Capture (OpenCV)
        │
        ▼
YOLOv8n Inference
(Object Detection)
        │
        ▼
ByteTrack Tracker
(Assigns & Maintains Track IDs)
        │
        ▼
Frame Annotation
(Boxes + Labels + Confidence + IDs)
        │
        ▼
Live Output Window
(Press 'q' to exit)
```

### Step-by-Step Breakdown

| Step | Description |
|---|---|
| **1. Model Loading** | Loads pre-trained `yolov8n.pt` weights — auto-downloaded on first run if not present locally |
| **2. Video Capture** | Opens the default webcam (`index 0`) via `cv2.VideoCapture()` — a video file path can be substituted |
| **3. Frame Reading** | Reads frames sequentially inside a `while` loop; exits gracefully if the camera disconnects |
| **4. YOLOv8 Tracking** | Calls `model.track(frame, persist=True)` — detection and tracking handled in a single step |
| **5. Annotation** | `results[0].plot()` draws bounding boxes, class labels, confidence scores, and track IDs onto the frame |
| **6. Display** | Renders the annotated frame in an OpenCV window titled **"YOLOv8 Object Tracking"** |
| **7. Exit** | Press **`q`** to cleanly release the camera resource and close all windows |

---

## 📁 Project Structure

```
ApexcifyTechnologys_-Object-Detection-and-Tracking-/
│
├── main.py               # Core application script
├── requirements.txt      # Python package dependencies
├── yolov8n.pt            # Pre-trained YOLOv8 Nano weights (~6.5 MB)
└── README.md
```

---

## 🚀 Getting Started

### Prerequisites

* Python 3.8 or above
* A connected webcam or a local video file for testing
* *(Optional but recommended)* A CUDA-enabled GPU for faster inference

### Installation

**1. Clone the repository**

```bash
git clone https://github.com/khushi-Jag/ApexcifyTechnologys_-Object-Detection-and-Tracking-.git
cd ApexcifyTechnologys_-Object-Detection-and-Tracking-
```

**2. Set up a virtual environment** *(recommended)*

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

**3. Install required packages**

```bash
pip install -r requirements.txt
```

> PyTorch is automatically pulled in as a dependency of `ultralytics` on first install.

---

## 📝 Usage

**Start the application:**

```bash
python main.py
```

* An OpenCV window titled **"YOLOv8 Object Tracking"** will appear.
* Detected objects are highlighted with **color-coded bounding boxes**.
* Every tracked object is assigned a **unique, persistent numeric Track ID**.
* Press **`q`** at any time to quit the application cleanly.

**Switch to a video file instead of webcam:**

Open `main.py` and update line 11:

```python
# Default (webcam):
video_source = 0

# Switch to a video file:
video_source = "path/to/your/video.mp4"
```

### Output Elements

| Element | Description |
|---|---|
| **Bounding Box** | A colored rectangle drawn around each detected object |
| **Label** | The predicted class name (e.g. `person`, `car`, `dog`) |
| **Confidence Score** | The model's certainty level (e.g. `0.91`) |
| **Track ID** | A stable, unique identifier per object (e.g. `#1`, `#2`) |

---

## 🤝 Contributing

Contributions are always welcome!

1. Fork the repository
2. Create a new feature branch:

```bash
git checkout -b feature/YourFeatureName
```

3. Commit your changes:

```bash
git commit -m "Add YourFeatureName"
```

4. Push and open a Pull Request:

```bash
git push origin feature/YourFeatureName
```

---

## 📝 License

Distributed under the **MIT License**. See `LICENSE` for full details.

---

## 📫 Contact

**Khushi Jag**
GitHub: [https://github.com/khushi-Jag/ApexcifyTechnologys_-Object-Detection-and-Tracking-](https://github.com/khushi-Jag/ApexcifyTechnologys_-Object-Detection-and-Tracking-)

---

## 🙏 Acknowledgments

* [Ultralytics YOLOv8 Documentation](https://docs.ultralytics.com/)
* [YOLOv8 Tracking Guide](https://docs.ultralytics.com/modes/track/)
* [OpenCV Documentation](https://docs.opencv.org/)
* [COCO Dataset](https://cocodataset.org/)
* [ByteTrack Paper](https://arxiv.org/abs/2110.06864)
* The Open Source Community ❤️
