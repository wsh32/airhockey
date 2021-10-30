import rospy
from cv_bridge import CvBridge, CvBridgeError

import cv2
import apriltag

from airhockey_vision.msg import ApriltagDetection, ApriltagDetections
from sensor_msgs.msg import Image
from geometry_msgs.msg import Point32, Polygon


class ApriltagNode:
    def __init__(self):
        self.image_subscriber = rospy.Subscriber(
            "/camera/image_raw", Image, self.image_callback)
        self.image_publisher = rospy.Publisher(
            "/vision/apriltags/image", Image, queue_size=3)
        self.detections_publisher = rospy.Publisher(
            "/vision/apriltags/detections", ApriltagDetections, queue_size=3)

        self.bridge = CvBridge()

        apriltag_options = apriltag.DetectorOptions(families="tag16h5")
        self.detector = apriltag.Detector(apriltag_options)

        rospy.spin()

    def detect_tags(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        results = self.detector.detect(gray)

        return results

    def annotate_frame(self, frame, detections):
        for tag in detections:
            (ptA, ptB, ptC, ptD) = tag.corners
            ptB = (int(ptB[0]), int(ptB[1]))
            ptC = (int(ptC[0]), int(ptC[1]))
            ptD = (int(ptD[0]), int(ptD[1]))
            ptA = (int(ptA[0]), int(ptA[1]))
            (cX, cY) = (int(tag.center[0]), int(tag.center[1]))
            cv2.circle(frame, (cX, cY), 5, (0, 0, 255), -1)

            cv2.line(frame, ptA, ptB, (0, 255, 0), 2)
            cv2.line(frame, ptB, ptC, (0, 255, 0), 2)
            cv2.line(frame, ptC, ptD, (0, 255, 0), 2)
            cv2.line(frame, ptD, ptA, (0, 255, 0), 2)

            tag_id = tag.tag_id
            cv2.putText(frame, str(tag_id), (ptA[0], ptA[1] - 15),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    def image_callback(self, image_msg):
        frame = self.bridge.imgmsg_to_cv2(image_msg,
                                          desired_encoding='passthrough')
        detections = self.detect_tags(frame)

        detection_msgs = []

        for tag in detections:
            detection_msg = ApriltagDetection()
            detection_msg.tag_family = tag.tag_family
            detection_msg.tag_id = tag.tag_id
            detection_msg.center_position = Point32(tag.center[0],
                                                    tag.center[1], 0)
            detection_msg.corner_positions = Polygon([Point32(tag.center[0],
                                                     tag.center[1], 0) for i
                                                     in range(4)])
            detection_msgs.append(detection_msg)

        print(detection_msgs)
        self.annotate_frame(frame, detections)

        try:
            self.image_publisher.publish(self.bridge.cv2_to_imgmsg(
                frame, "rgb8"))
            self.detections_publisher.publish(ApriltagDetections(detections=detection_msgs))
        except CvBridgeError as e:
            rospy.logerr(e)


def main():
    rospy.init_node('apriltag_node', anonymous=True)
    ApriltagNode()


if __name__=='__main__':
    main()

