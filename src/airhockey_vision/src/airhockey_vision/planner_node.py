import rospy

import yaml
import os

import numpy as np

from std_msgs.msg import Header
from geometry_msgs.msg import Point, PointStamped
from sensor_msgs.msg import Image


class Planner:
    def __init__(self, prediction_matrix_generator=None):
        if prediction_matrix_generator is not None:
            self.prediction_matrix_generator = prediction_matrix_generator
        else:
            self.prediction_matrix_generator = \
                Planner.default_prediction_matrix_generator

    @staticmethod
    def default_prediction_matrix_generator(t):
        return np.array([
            [1, 0, t, 0],
            [0, 1, 0, t],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
        ])

    def predict_state_time_from_now(self, current_state, time_from_now):
        transform_matrix = self.prediction_matrix_generator(time_from_now)
        return np.dot(transform_matrix, current_state)


class PlannerNode:
    def __init__(self):
        rospy.spin()


def main():
    rospy.init_node('planner_node', anonymous=True)

    PuckTrackingNode()


if __name__=='__main__':
    main()

