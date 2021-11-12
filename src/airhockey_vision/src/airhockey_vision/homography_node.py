import rospy
import numpy as np
import cv2

from std_msgs.msg import Header
from geometry_msgs.msg import PointStamped, Point
from airhockey_vision.msg import ApriltagDetections


class Tag:
    def __init__(self, tag_id, table_position):
        self.id = tag_id
        self.table_position = table_position
        self.camera_position = np.zeros(table_position.shape)


class TableLocalizer:
    def __init__(self, tag_locations):
        self.tag_locations = tag_locations
        self.homography_matrix = None
        self.homography_matrix_inv = None

    def update_tag_camera_positions(self, camera_positions):
        tags_found = []
        for tag in self.tag_locations:
            try:
                self.tag_locations[tag].camera_position = camera_positions[tag]
                tags_found.append(tag)
            except KeyError:
                self.tag_locations[tag].camera_position = None

        rospy.loginfo(f"Tags found: {tags_found}")

        if len(tags_found) < 4:
            rospy.logwarn("Not enough apriltags found")
        else:
            self.update_homography_matrix()

    def update_homography_matrix(self):
        points_camera = []
        points_table = []
        for tag in self.tag_locations.values():
            if tag.camera_position is None:
                continue

            points_camera.append(np.array(tag.camera_position))
            points_table.append(np.array(tag.table_position))

        self.homography_matrix, status = cv2.findHomography(
            np.array(points_camera), np.array(points_table))
        self.homography_matrix_inv, status = cv2.findHomography(
            np.array(points_table), np.array(points_camera))

    def get_table_position_from_camera(self, camera_x, camera_y):
        if self.homography_matrix is None:
            rospy.logerr("Homography matrix not calculated yet")
            return None

        return np.dot(self.homography_matrix, np.array([camera_x, camera_y, 1]))

    def get_camera_position_from_table(self, table_x, table_y):
        if self.homography_matrix is None:
            rospy.logerr("Homography matrix not calculated yet")
            return None

        return np.dot(self.homography_matrix_inv, np.array([table_x, table_y, 1]))


class HomographyNode:
    def __init__(self):
        self.puck_subscriber = rospy.Subscriber(
            "/vision/puck/puck_position", PointStamped, self.puck_callback)
        self.puck_publisher = rospy.Publisher(
            "/vision/puck/puck_position_table", PointStamped, queue_size=3)
        self.apriltag_subscriber = rospy.Subscriber(
            "/vision/apriltags/detections", ApriltagDetections,
            self.apriltag_callback)

        tags = {}
        tag_locations = rospy.get_param("tag_locations")
        for tag_name in tag_locations:
            tag = tag_locations[tag_name]
            tag_key = f"{tag['tag_family']}_{tag['tag_id']}"
            table_position = np.array([tag['table_x'], tag['table_y']])
            tags[tag_key] = Tag(tag['tag_id'], table_position)

        self.localizer = TableLocalizer(tags)

        rospy.spin()

    def apriltag_callback(self, apriltag_msg):
        locations = {}
        for det in apriltag_msg.detections:
            position = (det.center_position.x, det.center_position.y)
            locations[f"{det.tag_family}_{det.tag_id}"] = position
        self.localizer.update_tag_camera_positions(locations)

    def puck_callback(self, puck_msg):
        camera_x = puck_msg.point.x
        camera_y = puck_msg.point.y
        rospy.logwarn(f"X: {camera_x}, Y: {camera_y}")
        table_pos = self.localizer.get_table_position_from_camera(
            camera_x, camera_y)

        if table_pos is None:
            return

        point = Point(x=table_pos[0], y=table_pos[1])
        header = Header(stamp=rospy.Time.now(), frame_id="table")
        self.puck_publisher.publish(PointStamped(header=header, point=point))


def main():
    rospy.init_node('homography_node', anonymous=True, log_level=rospy.INFO)

#    tag_families = rospy.get_param("apriltag/tag_family")
    HomographyNode()


if __name__=='__main__':
    main()

