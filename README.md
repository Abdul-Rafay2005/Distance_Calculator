

## 📏 Yellow Object Distance Calculator Using OpenCV

This Python project uses **OpenCV** and **NumPy** to detect **yellow-colored objects** in a webcam feed and calculate the **distance between them** in real-time. It's great for beginners learning about computer vision, object tracking, and real-world measurements with cameras.

---

### 🔧 Features

* 🎥 Captures video from webcam
* 🟡 Detects objects with **yellow color**
* 📦 Draws bounding boxes and labels around detected objects
* 📐 Calculates and displays distance between object centers in **centimeters**
* ⚡ Real-time visualization using OpenCV windows

---

### 🧰 Requirements

* Python 3.7+
* OpenCV (`opencv-python`)
* NumPy

Install dependencies with:

```bash
pip install opencv-python numpy
```

---

### 🚀 How to Run

1. **Clone or download** this project.
2. Open the Python file (e.g., `distance_calculator.py`) in your IDE.
3. Run it:

```bash
python distance_calculator.py
```

4. Make sure you have **two or more yellow objects** visible in front of your webcam.
5. Press **`q`** to quit the program.

---

### 🎯 How It Works

1. The program opens your webcam.
2. It converts each frame to **HSV** color space to better detect yellow shades.
3. It isolates yellow regions using a defined HSV threshold.
4. It finds contours and calculates the center points of each detected object.
5. It calculates the **Euclidean distance** between centers and multiplies by a fixed calibration factor to estimate **real-world distance**.

---

### ⚙️ Calibration

The `distance_threshold` value determines how many **centimeters per pixel** are assumed. You can adjust this value:

```python
distance_threshold = 0.06912  # Change this based on your camera and setup
```

To calibrate:

* Place two yellow objects **exactly X cm apart**.
* Measure the pixel distance in the frame using `cv2.line()` or any method.
* Then: `distance_threshold = real_cm / pixel_distance`

---

### 📷 Troubleshooting

* ❌ **Webcam not opening?** Try changing the camera index (e.g., `cv2.VideoCapture(0)` to `cv2.VideoCapture(1)`)
* ❌ **Yellow not detected?** Adjust the HSV range:

```python
lower_yellow = np.array([20, 100, 100])
upper_yellow = np.array([30, 255, 255])
```

Use an HSV color picker tool to fine-tune detection.

---

### 📄 License

This project is open source and available under the [MIT License](https://opensource.org/licenses/MIT).

