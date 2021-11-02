import rospy
import cv2

from cv_bridge import CvBridge
from sensor_msgs.msg import Image


image_filename = "test_img.jpg"
bridge = CvBridge()

def image_callback(image_msg):
    frame = bridge.imgmsg_to_cv2(image_msg, desired_encoding='passthrough')
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    cv2.imwrite(image_filename, frame)


if __name__ == '__main__':
    rospy.init_node("take_picture_node")
    image_subscriber = rospy.Subscriber("/camera/image_raw", Image, image_callback)

    rospy.spin()

