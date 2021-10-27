import cv2

cap = cv2.VideoCapture(
    '/dev/v4l/by-id/usb-046d_HD_Pro_Webcam_C920_A4EC6ABF-video-index0')
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

try:
    while True:
        _, frame = cap.read()

        cv2.imshow('frame', frame)
        cv2.waitKey(1)
except KeyboardInterrupt:
    pass

cv2.destroyAllWindows()
cap.release()

