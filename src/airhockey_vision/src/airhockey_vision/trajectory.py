import rospy
import numpy as np
from cv_bridge import CvBridge, CvBridgeError
from collections import deque
from std_msgs.msg import String
from geometry_msgs.msg import PointStamped
from std_msgs.msg import Header
from airhockey_vision.msg import State


X_POS = 0
Y_POS = 1
X_VEL = 2
Y_VEL = 3


class TrajectoryCalculator:
    def __init__(self, table_dimensions=(36, 78), buffer_len=5,
                 filter_coef=0.125, prediction_matrix_generator=None):
        self.table_x, self.table_y = table_dimensions

        self.buffer = deque([[0, 0, 0, 0]], maxlen=buffer_len)  # [x, y, x_vel, y_vel]
        self.first_run = True
        self.prev_time = None
        self.filter_coef = filter_coef

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
            x_filtered = ((x * self.filter_coef)
                          + (self.buffer[-1][X_POS] * (1 - self.filter_coef)))
            y_filtered = ((y * self.filter_coef)
                          + (self.buffer[-1][Y_POS] * (1 - self.filter_coef)))
            x_vel = (x_filtered - self.buffer[-1][0]) / (time - self.prev_time)
            y_vel = (y_filtered - self.buffer[-1][1]) / (time - self.prev_time)

        self.prev_time = time
        puck_state = np.array([x_filtered, y_filtered, x_vel, y_vel])
        self.buffer.append(puck_state)

        return x, y, x_vel, y_vel

    def predict_state_time_from_now(self, time_from_now):
        transform_matrix = self.prediction_matrix_generator(time_from_now)
        return np.dot(transform_matrix, self.buffer[-1])

    def compute_table_reflection(self, puck_x, puck_y):
        if 0 < puck_x < self.table_x and 0 < puck_y < self.table_y:
            return puck_x, puck_y
        else:
            # Do reflections
            puck_x_reflected = puck_x
            puck_y_reflected = puck_y

            if puck_x < 0:
                puck_x_reflected *= -1
            if puck_x > self.table_x:
                # reflect across self.table_x
                puck_x_reflected = -1 * (puck_x_reflected - self.table_x) \
                        + self.table_x

            if puck_y < 0:
                puck_y_reflected *= -1
            if puck_y > self.table_y:
                # reflect across self.table_y
                puck_y_reflected = -1 * (puck_y_reflected - self.table_y) \
                        + self.table_y

            return self.compute_table_reflection(puck_x_reflected,
                                                 puck_y_reflected)


class TrajectoryNode:
    def __init__(self, table_dimensions):
        self.position_subscriber = rospy.Subscriber(
            "/vision/homography/puck_position", PointStamped, self.puck_callback)
        self.trajectory_publisher = rospy.Publisher(
            "/trajectory/puck_state", State, queue_size=3)

        self.trajectory_calculator = TrajectoryCalculator(
            table_dimensions=table_dimensions)

        rospy.spin()

    def puck_callback(self, puck_pos):
        time = puck_pos.header.stamp.secs + puck_pos.header.stamp.nsecs * 1e-9
        x, y, x_dot, y_dot = self.trajectory_calculator.update_state(
            puck_pos.point.x, puck_pos.point.y, time)

        header = Header(stamp=rospy.Time.now())
        puck_state = State(
            header=header, x_pos=x, y_pos=y, x_vel=x_dot, y_vel=y_dot)
        self.trajectory_publisher.publish(puck_state)


def main():
    rospy.init_node('trajectory_node', anonymous=True)

    table_x = rospy.get_param("table/width")
    table_y = rospy.get_param("table/length")
    TrajectoryNode((table_x, table_y))


if __name__=='__main__':
    config_path = os.path.join(os.path.dirname(__file__), "../..", "config")
    config = os.path.join(config_path, "default_table.yaml")
    config_data = yaml.load(open(config, 'r'), Loader = yaml.Loader)

    rospy.set_param("table", config_data['table'])

    main()

