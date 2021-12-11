import rospy

import yaml
import os

import numpy as np

from std_msgs.msg import Header, Float64
from geometry_msgs.msg import Point, PointStamped
from sensor_msgs.msg import Image

from airhockey_vision.msg import State


class Controller:
    def __init__(self):
        self.state_time = None
        self.x_pos = None
        self.y_pos = None
        self.x_vel = None
        self.y_vel = None

    def update_striker_state(self, time, x_pos, y_pos, x_vel, y_vel):
        self.state_time = time
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.x_vel = x_vel
        self.y_vel = y_vel

    def get_striker_position(self, time):
        return self.x_pos, self.y_pos


class ControllerNode:
    def __init__(self):
        self.striker_state_subscriber = rospy.Subscriber(
            "/planner/striker_state", State, self.striker_state_callback)
        self.arduino_command_publisher = rospy.Publisher(
            "/arduino/command/striker_pos", PointStamped, queue_size=3)

        # TODO: add robot constraints

        self.controller = Controller()

        rospy.spin()

    def striker_state_callback(self, striker_state_msg):
        x = striker_state_msg.x_pos
        y = striker_state_msg.x_pos
        header = Header(stamp=rospy.get_rostime)


def main():
    rospy.init_node('controller_node', anonymous=True)

    PlannerNode()


if __name__=='__main__':
    main()

