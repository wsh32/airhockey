import cv2

cap = cv2.VideoCapture(2)
# cap.set(cv2.CAP_PROP_FOCUS, 255)

try:
    while True:
        _, frame = cap.read()

        cv2.imshow('frame', frame)
        cv2.waitKey(1)
except KeyboardInterrupt:
    cv2.imwrite('img.jpg', frame)
    pass

cv2.destroyAllWindows()
cap.release()

