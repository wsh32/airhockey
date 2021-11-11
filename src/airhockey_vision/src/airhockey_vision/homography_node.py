import rospy
import numpy as np
import cv2

from geometry_msgs.msg import PointStamped
from airhockey_vision.msg import ApriltagDetections


class Tag:
    def __init__(self, tag_id, table_position):
        self.id = tag_id
        self.table_position = table_position
        self.camera_position = np.zeros(table_position.shape)


class TableLocalizer:
    def __init__(self, tags):
        self.tag_locations = tag_locations

    def update_tag_camera_locations(self, camera_locations):
        for tag in camera_locations:
            try:
                self.tag_locations[tag].camera_position = camera_locations[tag]
            except KeyError:
                rospy.warning(f"Tag {tag} not registered")

    def get_table_position_from_camera(self, camera_x, camera_y):
        pass

    def get_camera_position_from_table(self, table_x, table_y):
        pass


class HomographyNode:
    def __init__(self):
        self.puck_subscriber = rospy.Subscriber(
            "/vision/puck/puck_position", PointStamped, self.puck_callback)
        self.puck_publisher = rospy.Publisher(
            "/vision/puck/puck_position_table", PointStamped, queue_size=3)
        self.apriltag_subscriber = rospy.Susbscriber(
            "/vision/apriltag/detections", ApriltagDetections,
            self.apriltag_callback)

        tags = None  # TODO: Get tags from rosparams
        self.localizer = TableLocalizer(tags)

        rospy.spin()

    def apriltag_callback(self, apriltag_msg):
        locations = {}
        for det in apriltag_msg.detections:
            position = (det.center_position.x, det.center_position.y)
            locations[f"{det.tag_family}_{det.tag_id}"] = position

    def puck_callback(self, puck_msg):
        camera_x = puck_msg.point.x
        camera_y = puck_msg.point.y
        rospy.loginfo(f"X: {camera_x}, Y: {camera_y}")


def main():
    rospy.init_node('localization_node', anonymous=True, log_level=rospy.INFO)

#    tag_families = rospy.get_param("apriltag/tag_family")
    HomographyNode()


if __name__=='__main__':
    main()

