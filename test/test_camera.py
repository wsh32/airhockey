import cv2
import camera

cap = camera.Camera(width=1280, height=960)

try:
    while True:
        _, frame = cap.read()

        cv2.imshow('frame', frame)
        cv2.waitKey(1)
except KeyboardInterrupt:
    pass

cv2.destroyAllWindows()
cap.release()

