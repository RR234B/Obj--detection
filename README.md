
# 🚀 Real-Time Object Detection Using YOLO and OpenCV

## 📌 Project Overview

This project is a real-time object detection application built using **YOLO (You Only Look Once)** and **OpenCV** in Python.

The application uses a live camera feed to detect and identify objects in real time. It draws bounding boxes around detected objects and displays their class labels and confidence scores.

The project uses a pretrained YOLO model that can recognize objects from **80 different classes** in the COCO dataset.

## ✨ Features

- 🎥 Real-time object detection using a webcam
- 🤖 AI-powered object recognition using YOLO
- 👁️ Live video processing with OpenCV
- 📦 Bounding boxes around detected objects
- 🏷️ Object class labels and confidence scores
- ⚡ Fast and efficient detection using a pretrained model

## 🛠️ Technologies Used

- **Python** – Programming language
- **YOLO (Ultralytics)** – Object detection model
- **OpenCV** – Image and video processing
- **PyTorch** – Deep learning framework

## 📋 Requirements

Make sure Python is installed on your system.

Install the required libraries using the following command:

```bash
pip install ultralytics opencv-python
```

PyTorch is installed as a dependency when required, but you can install the appropriate version separately if needed.

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
```

### 2. Open the Project Folder

```bash
cd YOUR-REPOSITORY
```

### 3. Install Dependencies

```bash
pip install ultralytics opencv-python
```

### 4. Download the YOLO Model

The project uses the pretrained `yolo11n.pt` model. Ultralytics can automatically download it when the model is initialized for the first time.

### 5. Run the Project

Run your main Python file. For example, if your file is named `main.py`:

```bash
python main.py
```

**Note:** Replace `main.py` with the actual name of your Python file.

Allow webcam access if prompted. Press `q` to exit the detection window if your script supports this keyboard shortcut.

## 🎯 Supported Object Classes

The pretrained YOLO model can detect 80 classes from the COCO dataset, including:

- Person
- Bicycle
- Car
- Motorcycle
- Airplane
- Bus
- Train
- Truck
- Boat
- Traffic light
- Stop sign
- Cat
- Dog
- Horse
- Bird
- Chair
- Bottle
- Laptop
- Cell phone
- Book
- And many more!

The complete set of 80 classes is defined by the pretrained model.

## 🧠 How It Works

1. The webcam captures a live video stream.
2. OpenCV reads the video frames.
3. YOLO processes each frame and identifies objects.
4. The model predicts object classes and confidence scores.
5. Bounding boxes and labels are displayed on the video.
6. The process continues until the user exits the application.

## 📂 Project Structure

```text
Object-Detection/
│
├── main.py              # Main object detection script
├── yolo11n.pt            # Pretrained YOLO model (if included)
├── requirements.txt      # Project dependencies
├── README.md             # Project documentation
└── runs/                 # Optional training or output files
```

*Update the file names and folders to match your actual repository. The model weights do not need to be committed if they can be downloaded automatically.*

## 🔮 Future Improvements

- Improve detection accuracy and performance.
- Add custom object detection classes.
- Save detected images and video recordings.
- Explore GPU acceleration for faster inference.
- Integrate additional interactive features.

## 👨‍💻 Author

**Your Name**

B.Tech Computer Science and Engineering Student

Interested in Artificial Intelligence, Computer Vision, and Python Development.

## ⭐ Acknowledgements

- [Ultralytics YOLO](https://github.com/ultralytics/ultralytics)
- [OpenCV](https://opencv.org/)
- [COCO Dataset](https://cocodataset.org/)

---

If you find this project interesting, consider giving the repository a ⭐!
