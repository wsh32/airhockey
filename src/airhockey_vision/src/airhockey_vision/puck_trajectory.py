import rospy
import numpy as np
from cv_bridge import CvBridge, CvBridgeError
from collections import deque
from std_msgs.msg import String
from geometry_msgs.msg import PointStamped
from std_msgs.msg import Header
from airhockey_vision.msg import PuckState



class TrajectoryCalculator:
    def __init__(self, buffer_len = 5):
        self.buffer = deque(maxlen = buffer_len) # [x, y, x_dot, y_dot]
        self.first_run = True
        self.prev_time = None
        print(self.buffer)

    def calc_trajectory(self, x, y, time):
        if self.first_run:
            x_dot = 0
            y_dot = 0
            self.first_run = False
        else:
            x_dot = (x - self.buffer[-1][0]) / (time - self.prev_time)
            y_dot = (y - self.buffer[-1][1]) / (time - self.prev_time)
        self.prev_time = time
        puck_pos_v = np.array([x, y, x_dot, y_dot])
        self.buffer.append(puck_pos_v)
        return x, y, x_dot, y_dot

class TrajectoryNode:
    def __init__(self):
        self.position_subscriber = rospy.Subscriber(
            "/vision/puck/puck_position", PointStamped, self.puck_callback)
        self.trajectory_publisher = rospy.Publisher(
            "/vision/puck/puck_state", PuckState, queue_size=3)
        self.trajectory_calculator = TrajectoryCalculator()

        rospy.spin()

    def puck_callback(self, puck_pos):
        x, y, x_dot, y_dot = self.trajectory_calculator.calc_trajectory(puck_pos.point.x,
                                    puck_pos.point.y,
                                    puck_pos.header.stamp.secs +
                                    puck_pos.header.stamp.nsecs / 1000000000)
        header = Header(stamp=rospy.Time.now())
        puck_state = PuckState(header = header,
                                        x_pos = x,
                                        y_pos = y,
                                        x_vel = x_dot,
                                        y_vel = y_dot)
        self.trajectory_publisher.publish(puck_state)


def main():
    rospy.init_node('trajectory_node', anonymous=True)
    TrajectoryNode()


if __name__=='__main__':
    main()
