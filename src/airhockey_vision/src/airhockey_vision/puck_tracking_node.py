import rospy
from cv_bridge import CvBridge, CvBridgeError

import cv2
import imutils

from geometry_msgs.msg import Point32
from sensor_msgs.msg import Image


class PuckTrackingNode:
    def __init__(self, lower, upper, visualize_color):
        self.lower = lower
        self.upper = upper
        self.visualize_color = visualize_color

        self.image_subscriber = rospy.Subscriber(
            "/camera/image_raw", Image, self.image_callback)
        self.image_publisher = rospy.Publisher(
            "/vision/puck/image", Image, queue_size=3)
        self.detections_publisher = rospy.Publisher(
            "/vision/puck/puck_position", Point32, queue_size=3)

        self.bridge = CvBridge()
        rospy.spin()

    def detect_puck(self, frame):
        blurred = cv2.GaussianBlur(frame, (11, 11), 0)
        hsv = cv2.cvtColor(blurred, cv2.COLOR_RGB2HSV)
        mask = cv2.inRange(hsv, self.lower, self.upper)
        mask = cv2.erode(mask, None, iterations=2)
        mask = cv2.dilate(mask, None, iterations=2)

        contours = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
                                    cv2.CHAIN_APPROX_SIMPLE)
        contours = imutils.grab_contours(contours)
        center = None

        if len(contours) > 0:
            c = max(contours, key=cv2.contourArea)
            ((x, y), radius) = cv2.minEnclosingCircle(c)
            moments = cv2.moments(c)
            center = (int(moments["m10"] / moments["m00"]),
                      int(moments["m01"] / moments["m00"]))

        return center

    def annotate_frame(self, frame, puck_position):
        if puck_position:
            cv2.circle(frame, puck_position, 5, self.visualize_color, -1)

    def image_callback(self, image_msg):
        frame = self.bridge.imgmsg_to_cv2(image_msg,
                                          desired_encoding='passthrough')
        puck_position = self.detect_puck(frame)

        if not puck_position:
            return

        puck_x, puck_y = puck_position
        self.annotate_frame(frame, puck_position)

        try:
            self.image_publisher.publish(self.bridge.cv2_to_imgmsg(
                frame, "rgb8"))
            self.detections_publisher.publish(Point32(x=puck_x, y=puck_y))
        except CvBridgeError as e:
            rospy.logerr(e)


def main():
    rospy.init_node('puck_tracking_node', anonymous=True)
    lower = (rospy.get_param("puck_tracking/h_lower"),
             rospy.get_param("puck_tracking/s_lower"),
             rospy.get_param("puck_tracking/v_lower"))
    upper = (rospy.get_param("puck_tracking/h_upper"),
             rospy.get_param("puck_tracking/s_upper"),
             rospy.get_param("puck_tracking/v_upper"))

    try:
        visualize_color = (rospy.get_param("puck_tracking/visualize_color_r"),
                           rospy.get_param("puck_tracking/visualize_color_g"),
                           rospy.get_param("puck_tracking/visualize_color_b"))
    except KeyError:
        visualize_color = (255, 255, 0)

    PuckTrackingNode(lower=lower, upper=upper, visualize_color=visualize_color)


if __name__=='__main__':
    main()

