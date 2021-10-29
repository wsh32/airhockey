import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

import cv2
import apriltag


class VisionNode:
    def __init__(self):
        self.image_subscriber = rospy.Subscriber("/camera/image_raw", Image,
                                                 self.image_callback)
        self.image_publisher = rospy.Publisher("/vision/apriltags/image", Image,
                                              queue_size=3)
        self.image_publisher = rospy.Publisher("/vision/apriltags/locations", Image,
                                              queue_size=3)

        self.bridge = CvBridge()

        apriltag_options = apriltag.DetectorOptions(families="tag16h5")
        self.detector = apriltag.Detector(apriltag_options)

        rospy.spin()

    def image_callback(self, image_msg):
        frame = self.bridge.imgmsg_to_cv2(image_msg,
                                          desired_encoding='passthrough')

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        results = self.detector.detect(gray)
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

            tag_id = r.tag_id
            cv2.putText(frame, str(tag_id), (ptA[0], ptA[1] - 15),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        try:
            self.image_publisher.publish(self.bridge.cv2_to_imgmsg(
                frame, "rgb8"))
        except CvBridgeError as e:
            rospy.logerr(e)


def main():
    rospy.init_node('vision_node', anonymous=True)
    VisionNode()


if __name__=='__main__':
    main()

