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
        # TODO: Add the math here
        if self.x_pos is not None and self.y_pos is not None:
            return self.x_pos, self.y_pos
        return 400, 0


class ControllerNode:
    def __init__(self):
        self.puck_state_subscriber = rospy.Subscriber(
            "/trajectory/puck_state", State, self.puck_state_callback)
        self.striker_state_subscriber = rospy.Subscriber(
            "/planner/striker_state", State, self.striker_state_callback)
        self.arduino_command_publisher = rospy.Publisher(
            "/arduino/command/striker_pos", PointStamped, queue_size=3)

        # TODO: add robot constraints

        self.controller = Controller()
        self.enable = True
        self.center = False

        rospy.Timer(rospy.Duration(0.1), self.publish_state)
        rospy.spin()

    def puck_state_callback(self, puck_state_msg):
        self.enable = abs(puck_state_msg.y_vel) > 0.1
        self.center = puck_state_msg.y_vel > 0.5

        self.controller.update_striker_state(0, puck_state_msg.x_pos, 0, 0, 0)

    def publish_state(self, event=None):
        x, y = self.controller.get_striker_position(rospy.get_rostime())

        if x is None or y is None:
            return

        header = Header(stamp=rospy.get_rostime())
        point = Point(x=round(x - 62.5, 2), y=round(y, 2))

        if self.center:
            point = Point(x=400, y=0)

        if True: #self.enable:
            self.arduino_command_publisher.publish(
                PointStamped(header=header, point=point))

    def striker_state_callback(self, striker_state_msg):
        return
        time = striker_state_msg.header.stamp
        x_pos = striker_state_msg.x_pos
        y_pos = striker_state_msg.y_pos
        x_vel = striker_state_msg.x_vel
        y_vel = striker_state_msg.y_vel

        self.controller.update_striker_state(time, x_pos, y_pos, x_vel, y_vel)


def main():
    rospy.init_node('controller_node', anonymous=True)

    ControllerNode()


if __name__=='__main__':
    main()

