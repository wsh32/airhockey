import rospy
from cv_bridge import CvBridge, CvBridgeError
import apriltag

from airhockey_vision.msg import ApriltagDetection, ApriltagDetections
from std_msgs.msg import String
from sensor_msgs.msg import Image
from geometry_msgs.msg import Point32, Polygon, PointStamped

from airhockey_vision.apriltag_node import ApriltagDetector
from airhockey_vision.puck_tracking_node import PuckTracker


class VisualizationNode:
    def __init__(self, tag_families="tag16h5", visualize_color=(255, 0, 255)):
        self.image_subscriber = rospy.Subscriber(
            "/camera/image_raw", Image, self.image_callback)
        self.puck_subscriber = rospy.Subscriber(
            "/vision/puck/puck_position", PointStamped, self.puck_callback)
        self.apriltag_subscriber = rospy.Subscriber(
            "/vision/apriltags/detections", ApriltagDetections,
            self.apriltag_callback)
        self.image_publisher = rospy.Publisher(
            "/vision/visualization/image", Image, queue_size=3)

        self.puck_position = (0, 0)
        self.apriltag_detections = []

        self.apriltag_detector = ApriltagDetector(tag_families)
        self.puck_tracker = PuckTracker((34, 83, 76), (82, 219, 204),
                                        visualize_color)

        self.bridge = CvBridge()
        rospy.spin()

    def puck_callback(self, position_msg):
        self.puck_position = (int(position_msg.point.x),
                              int(position_msg.point.y))

    def apriltag_callback(self, detections_msg):
        self.apriltag_detections = []
        for detection_msg in detections_msg.detections:
            center = [detection_msg.center_position.x,
                      detection_msg.center_position.y]

            # TODO: Add corners
            corners = ([], [], [], [])
            detection = apriltag.Detection(detection_msg.tag_family,
                                           detection_msg.tag_id,
                                           None,
                                           None,
                                           None,
                                           None,
                                           center,
                                           corners)

    def image_callback(self, image_msg):
        frame = self.bridge.imgmsg_to_cv2(image_msg,
                                          desired_encoding='passthrough')
        detections = self.apriltag_detector.detect_tags(frame)
        self.apriltag_detector.annotate_frame(frame, detections)

        puck_position = self.puck_tracker.detect_puck(frame)

        self.puck_tracker.annotate_frame(frame, self.puck_position)

        try:
            self.image_publisher.publish(self.bridge.cv2_to_imgmsg(
                frame, "rgb8"))
        except CvBridgeError as e:
            rospy.logerr(e)


def main():
    rospy.init_node('viz', anonymous=True)
    VisualizationNode()


if __name__=='__main__':
    main()

