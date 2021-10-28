import cv2

for i in range(20):
    try:
        cap = cv2.VideoCapture(i)
        if cap.isOpened():
            print(f"Camera open on: {i}")
        cap.release()
    except:
        pass
