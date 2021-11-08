import rospy
import numpy as np
from cv_bridge import CvBridge, CvBridgeError
from collections import deque
from std_msgs.msg import String
from geometry_msgs.msg import PointStamped


class TrajectoryCalculator:
    def __init__(self):
        self.buffer = deque(np.zeroes((5,5)), maxlen = 5) # [x, y, x_dot, y_dot, time]

    def calc_trajectory(self, x, y, time):
        x_dot = x - self.buffer[-1][1]
        y_dot = y - self.buffer[-1][2]
        puck_pos_v = np.array([x, y, x_dot, y_dot, time])
        self.buffer.append(puck_pos_v)
        return puck_pos_v


class TrajectoryNode:
    def __init__(self):
        self.position_subscriber = rospy.Subscriber(
        "/vision/puck/puck_position", PointStamped,
        )
        self.trajectory_publisher = rospy.Publisher(
            "/vision/apriltags/detections", )

        self.bridge = CvBridge()
        self.trajectory_calculator = TrajectoryCalculator()

        rospy.spin()
    def puck_callback(self, puck_pos):
        pos_v_array = self.trajectory_calculator.calc_trajectory(puck_pos.point.x, puck_pos.point.y, puck_pos.header.stamp)




def main():
    rospy.init_node('trajectory_node', anonymous=True)

    TrajectoryNode()


if __name__=='__main__':
    main()
