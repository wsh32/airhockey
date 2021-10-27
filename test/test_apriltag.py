import cv2
import apriltag

cap = cv2.VideoCapture(2)
#cap.set(cv2.CAP_PROP_FOCUS, 255)

apriltag_options = apriltag.DetectorOptions(families="tag16h5")
detector = apriltag.Detector(apriltag_options)

try:
    while True:
        _, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        results = detector.detect(gray)

        for r in results:
            (ptA, ptB, ptC, ptD) = r.corners
            ptB = (int(ptB[0]), int(ptB[1]))
            ptC = (int(ptC[0]), int(ptC[1]))
            ptD = (int(ptD[0]), int(ptD[1]))
            ptA = (int(ptA[0]), int(ptA[1]))
            (cX, cY) = (int(r.center[0]), int(r.center[1]))
            cv2.circle(frame, (cX, cY), 5, (0, 0, 255), -1)

            cv2.line(frame, ptA, ptB, (0, 255, 0), 2)
            cv2.line(frame, ptB, ptC, (0, 255, 0), 2)
            cv2.line(frame, ptC, ptD, (0, 255, 0), 2)
            cv2.line(frame, ptD, ptA, (0, 255, 0), 2)

            #print(dir(r))
            tag_id = r.tag_id
            cv2.putText(frame, str(tag_id), (ptA[0], ptA[1] - 15),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        cv2.imshow('frame', frame)
        cv2.waitKey(1)
except KeyboardInterrupt:
    pass

cv2.destroyAllWindows()
cap.release()

