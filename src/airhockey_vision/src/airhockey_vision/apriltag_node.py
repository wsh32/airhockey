import rospy
from cv_bridge import CvBridge, CvBridgeError

import cv2
import apriltag

import yaml
import os

from airhockey_vision.msg import ApriltagDetection, ApriltagDetections
from std_msgs.msg import String, Header
from sensor_msgs.msg import Image
from geometry_msgs.msg import Point32, Polygon


class ApriltagDetector:
    def __init__(self, tag_families):
        apriltag_options = apriltag.DetectorOptions(families=tag_families)
        self.detector = apriltag.Detector(apriltag_options)

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


class ApriltagNode:
    def __init__(self, tag_families):
        self.image_subscriber = rospy.Subscriber(
            "/camera/image_raw", Image, self.image_callback)
        self.image_publisher = rospy.Publisher(
            "/vision/apriltags/image", Image, queue_size=3)
        self.detections_publisher = rospy.Publisher(
            "/vision/apriltags/detections", ApriltagDetections, queue_size=3)

        self.bridge = CvBridge()
        self.apriltag_detector = ApriltagDetector(tag_families=tag_families)

        rospy.spin()

    def image_callback(self, image_msg):
        frame = self.bridge.imgmsg_to_cv2(image_msg,
                                          desired_encoding='passthrough')
        detections = self.apriltag_detector.detect_tags(frame)

        detection_msgs = []
        for tag in detections:
            detection_msg = ApriltagDetection()
            detection_msg.tag_family = tag.tag_family.decode("utf-8")
            detection_msg.tag_id = tag.tag_id
            detection_msg.center_position = Point32(x=tag.center[0],
                                                    y=tag.center[1])
            corners = []
            for corner in tag.corners:
                corners.append(Point32(x=corner[0], y=corner[1]))
            detection_msg.corner_positions = Polygon(points=corners)
            detection_msgs.append(detection_msg)

        self.apriltag_detector.annotate_frame(frame, detections)

        try:
            self.image_publisher.publish(self.bridge.cv2_to_imgmsg(
                frame, "rgb8"))
            header = Header(stamp=rospy.Time.now(), frame_id="camera")
            self.detections_publisher.publish(
                ApriltagDetections(header=header, detections=detection_msgs))
        except CvBridgeError as e:
            rospy.logerr(e)


def main():
    rospy.init_node('apriltag_node', anonymous=True)

    tag_families = rospy.get_param("apriltag/tag_family")
    ApriltagNode(tag_families)


if __name__=='__main__':
    config_path = os.path.join(os.path.dirname(__file__), "../..", "config")
    apriltag_config = os.path.join(config_path, "apriltag_16h5.yaml")
    config_data = yaml.load(open(apriltag_config, 'r'), Loader = yaml.Loader)

    rospy.set_param("apriltag/tag_family",
                    config_data['apriltag']['tag_family'])
    main()

