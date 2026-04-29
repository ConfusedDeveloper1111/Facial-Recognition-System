# 🎯 Facial Recognition System

A real-time face recognition system built with Python and OpenCV. The system implements a complete ML pipeline — from automated face data collection to classifier training and live webcam-based identity recognition.

## 📸 Demo

![Demo](screenshots/demo.png)

## 🚀 How It Works

The project follows a 3-stage ML pipeline:

1. **Data Collection** (`create_dataset.py`) — Opens webcam and automatically captures 100 face images using Haar Cascade face detection
2. **Model Training** (`create_classifier.py`) — Trains an LBPH (Local Binary Pattern Histogram) face recognizer on the captured dataset and saves the classifier
3. **Live Detection** (`Detector.py`) — Loads the trained classifier and performs real-time face recognition via webcam with confidence-based identity verification

## 🛠️ Tech Stack

- Python
- OpenCV (cv2) — face detection and recognition
- LBPH Face Recognizer — similarity-based ML classifier
- Haar Cascade Classifier — face detection
- Pillow — image processing
- NumPy — array operations

## ⚙️ Installation & Usage

**Step 1 — Clone the repo:**
```bash
git clone https://github.com/YOUR_USERNAME/Facial-Recognition-System.git
cd Facial-Recognition-System
```

**Step 2 — Install dependencies:**
```bash
pip install -r requirements.txt
```

**Step 3 — Run the pipeline:**
```bash
python run.py
```

Enter your name when prompted. The system will:
- Capture your face data via webcam (auto-stops at 100 images)
- Train a personal classifier
- Launch live face recognition

## ⚠️ Known Limitations

- LBPH is a similarity-based classifier — it identifies the closest match from trained subjects. A confidence threshold of 50% is implemented to flag unknown faces.
- Performance may vary under poor lighting or extreme angles.
- Screen-displayed photos can occasionally bypass the confidence threshold due to texture differences from live video.

## 📌 Note

Face data folders are excluded from this repository for privacy. Run `python run.py` to generate your own dataset locally.

Press **Q** to exit the webcam window.

## 📂 Project Structure
