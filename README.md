# 🔍 Autonomous Visual Inspection System

An AI-based PCB inspection system that uses **YOLOv8** and **Streamlit** to detect defects in PCB images automatically.

## 🚀 About the Project

Checking PCBs manually can take a lot of time, especially when there are many boards to inspect. Small defects can also be difficult to notice during manual inspection.

This project uses a trained **YOLOv8 object detection model** to analyze PCB images and identify defects. Users can simply upload a PCB image, and the system displays the detected defects along with their locations and confidence scores.

## ✨ Features

- 📷 Upload a PCB image
- 🤖 Detect PCB defects using YOLOv8
- 🔍 Automatically inspect the uploaded image
- 📊 Display confidence scores for detected defects
- 🖼️ Show detected defects with bounding boxes
- ⚡ Simple and interactive Streamlit interface
- 🏭 Useful for AI-based quality inspection

## 🛠️ Technologies Used

- **Python** – Application development
- **YOLOv8** – Object detection
- **Ultralytics** – YOLOv8 implementation
- **Streamlit** – Web interface
- **OpenCV** – Image processing
- **Pillow** – Image handling
- **NumPy** – Numerical operations

## 🧠 How It Works

```text
PCB Image
    ↓
Upload Image
    ↓
Streamlit Interface
    ↓
YOLOv8 Model
    ↓
Detect PCB Defects
    ↓
Draw Bounding Boxes
    ↓
Display Defects & Confidence Scores