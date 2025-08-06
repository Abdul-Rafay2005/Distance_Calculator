import cv2
import numpy as np
import math as m

distance_threshold = 0.06912  # You can adjust this based on your setup

# Try multiple camera indexes (0–4) to find a working one
camera_index = -1
for i in range(5):
    cap = cv2.VideoCapture(i)
    if cap.isOpened():
        camera_index = i
        print(f"[OK] Using camera index {i}")
        break
    cap.release()

if camera_index == -1:
    print("[ERROR] Could not open any webcam.")
    exit()

cap = cv2.VideoCapture(camera_index)

while True:
    ok, img = cap.read()
    if not ok:
        print("[ERROR] Failed to capture frame.")
        break

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    lower_yellow = np.array([20, 100, 100])
    upper_yellow = np.array([30, 255, 255])

    mask = cv2.inRange(src=hsv, lowerb=lower_yellow, upperb=upper_yellow)
    result = cv2.bitwise_and(src1=img, src2=img, mask=mask)

    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    label_char = 65  # ASCII A
    points = []

    for contour in contours:
        if cv2.contourArea(contour) > 500:
            x, y, w, h = cv2.boundingRect(contour)
            cx = x + w // 2
            cy = y + h // 2
            points.append([cx, cy])

            # Draw bounding box and center
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
            cv2.circle(img, (cx, cy), 5, (0, 0, 255), -1)
            cv2.putText(img, chr(label_char), (cx - 30, cy + 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
            label_char += 1

    # Draw distance lines and labels
    for i in range(len(points) - 1):
        x1, y1 = points[i]
        x2, y2 = points[i + 1]
        distance_px = m.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        distance_cm = distance_px * distance_threshold
        tx = (x1 + x2) // 2
        ty = (y1 + y2) // 2

        cv2.line(img, (x1, y1), (x2, y2), (255, 0, 0), 2)
        cv2.putText(img, f"{distance_cm:.2f} cm", (tx, ty), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    # Show all frames
    cv2.imshow("HSV", hsv)
    cv2.imshow("Mask", mask)
    cv2.imshow("Result", result)
    cv2.imshow("Final Output", img)

    if cv2.waitKey(1) == ord("q"):
        break 

cap.release()
cv2.destroyAllWindows()
