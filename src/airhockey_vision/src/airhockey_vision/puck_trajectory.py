import rospy
import numpy as np
from cv_bridge import CvBridge, CvBridgeError
from collections import deque
from std_msgs.msg import String
from geometry_msgs.msg import PointStamped
from std_msgs.msg import Header
from airhockey_vision.msg import PuckState


class TrajectoryCalculator:
    def __init__(self, buffer_len=5, prediction_matrix_generator=None):
        self.buffer = deque(maxlen=buffer_len)  # [x, y, x_vel, y_vel]
        self.first_run = True
        self.prev_time = None

        if prediction_matrix_generator is not None:
            self.prediction_matrix_generator = prediction_matrix_generator
        else:
            self.prediction_matrix_generator = \
                TrajectoryCalculator.default_prediction_matrix_generator

    @staticmethod
    def default_prediction_matrix_generator(t):
        return np.array([
            [1, 0, t, 0],
            [0, 1, 0, t],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
        ])

    def update_state(self, x, y, time):
        if self.first_run:
            x_vel = 0
            y_vel = 0
            self.first_run = False
        else:
            x_vel = (x - self.buffer[-1][0]) / (time - self.prev_time)
            y_vel = (y - self.buffer[-1][1]) / (time - self.prev_time)

        self.prev_time = time
        puck_state = np.array([x, y, x_vel, y_vel])
        self.buffer.append(puck_state)

        return x, y, x_vel, y_vel

    def predict_state_time_from_now(self, time_from_now):
        transform_matrix = self.prediction_matrix_generator(time_from_now)
        return np.dot(transform_matrix, self.buffer[-1])



class TrajectoryNode:
    def __init__(self):
        self.position_subscriber = rospy.Subscriber(
            "/vision/puck/puck_position", PointStamped, self.puck_callback)
        self.trajectory_publisher = rospy.Publisher(
            "/trajectory/puck_state", PuckState, queue_size=3)

        self.trajectory_calculator = TrajectoryCalculator()

        rospy.spin()

    def puck_callback(self, puck_pos):
        time = puck_pos.header.stamp.secs + puck_pos.header.stamp.nsecs * 1e-9
        x, y, x_dot, y_dot = self.trajectory_calculator.update_state(
            puck_pos.point.x, puck_pos.point.y, time)

        header = Header(stamp=rospy.Time.now())
        puck_state = PuckState(
            header=header, x_pos=x, y_pos=y, x_vel=x_dot, y_vel=y_dot)
        self.trajectory_publisher.publish(puck_state)


def main():
    rospy.init_node('trajectory_node', anonymous=True)
    TrajectoryNode()


if __name__=='__main__':
    main()

