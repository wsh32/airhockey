import rospy

import yaml
import os

import numpy as np

from std_msgs.msg import Header, Float64
from geometry_msgs.msg import Point, PointStamped
from sensor_msgs.msg import Image

from airhockey_vision.msg import State

from airhockey_vision import trajectory
from airhockey_vision.trajectory import TrajectoryCalculator


class Planner:
    def __init__(self, puck_diameter=2.5, striker_diameter=2.5):
        self.puck_diameter = puck_diameter
        self.striker_diameter = striker_diameter

        self.trajectory_calculator = TrajectoryCalculator()

    def compute_optimal_puck_contact_position(self, puck_state, striker_state,
                                              contact_y_pos=6):
        # for now, ignore striker state and return the optimal striker pose for
        # scoring. future work would be to use the striker state to choose the
        # best place to hit the puck.
        time_to_contact = ((contact_y_pos - puck_state[trajectory.Y_POS])
                           / puck_state[trajectory.Y_VEL])

        if puck_state[trajectory.Y_VEL] == 0:
            time_to_contact = 0

        contact_x_pos = (puck_state[trajectory.X_VEL] * time_to_contact
                         + puck_state[trajectory.X_POS])

        return time_to_contact, contact_x_pos, contact_y_pos

    def compute_optimal_striker_contact_state(self, puck_state, striker_state,
                                              target_pos, contact_y_pos=6,
                                              contact_speed=0):
        time, puck_x, puck_y = self.compute_optimal_puck_contact_position(
            puck_state, striker_state, contact_y_pos=contact_y_pos)
        relative_target_position = (np.array(target_pos)
                                    - np.array([puck_x, puck_y]))

        # Correct relative puck velocity to the moving striker
        # Striker is constrained to move in the direction of the target at the
        # speed of contact_speed.
        striker_vel = contact_speed * (relative_target_position /
                                       np.linalg.norm(relative_target_position))
        relative_puck_x_vel = puck_state[trajectory.X_VEL] - striker_vel[0]
        relative_puck_y_vel = puck_state[trajectory.Y_VEL] - striker_vel[1]

        # Calculate angles (rads) clockwise is positive, vertical is zero
        angle_incoming = np.arctan2(-relative_puck_x_vel, -relative_puck_y_vel)
        angle_outgoing = np.arctan2(relative_target_position[0],
                                    relative_target_position[1])

        contact_normal_angle = (angle_incoming + angle_outgoing) / 2

        # Calculate striker position
        ctc_distance = (self.puck_diameter + self.striker_diameter) / 2
        striker_position_relative = ctc_distance * np.array(
            [-np.sin(contact_normal_angle), -np.cos(contact_normal_angle)])
        striker_position = striker_position_relative + np.array([puck_x, puck_y])

        return (time, striker_position[0], striker_position[1],
                striker_vel[0], striker_vel[1])


class PlannerNode:
    def __init__(self, puck_diameter=2.5, striker_diameter=3.875, table_width=36,
                 table_length=78, goal_width=12, default_contact_y_pos=6,
                 default_contact_speed=0):
        self.puck_state_subscriber = rospy.Subscriber(
            "/trajectory/puck_state", State, self.puck_state_callback)
        self.target_command_subscriber = rospy.Subscriber(
            "/game/target", Point, self.target_command_callback)
        self.contact_position_command_subscriber = rospy.Subscriber(
            "/game/contact_y_pos", Float64, self.contact_position_command_callback)
        self.contact_speed_command_subscriber = rospy.Subscriber(
            "/game/contact_speed", Float64, self.contact_speed_command_callback)
        self.striker_state_command_publisher = rospy.Publisher(
            "/planner/striker_state", State, queue_size=3)

        self.target = (table_width / 2, table_length)
        self.planner = Planner(puck_diameter=puck_diameter,
                               striker_diameter=striker_diameter)

        self.contact_y_pos = default_contact_y_pos
        self.contact_speed = default_contact_speed

        self.striker_state = np.zeros(4)

        rospy.spin()

    def puck_state_callback(self, puck_state_msg):
        puck_state = np.array([
            puck_state_msg.x_pos,
            puck_state_msg.y_pos,
            puck_state_msg.x_vel,
            puck_state_msg.y_vel
        ])

        time, x_pos, y_pos, x_vel, y_vel = \
            self.planner.compute_optimal_striker_contact_state(
                puck_state, self.striker_state, self.target,
                contact_y_pos=self.contact_y_pos,
                contact_speed=self.contact_speed)

        header = Header(stamp=rospy.get_rostime() + rospy.Duration(time))
        striker_state = State(header=header, x_pos=x_pos, y_pos=y_pos,
                              x_vel=x_vel, y_vel=y_vel)

        self.striker_state_command_publisher.publish(striker_state)

    def target_command_callback(self, target_msg):
        self.target = (target_msg.x, target_msg.y)

    def contact_position_command_callback(self, position_msg):
        self.contact_y_pos = position_msg.data

    def contact_speed_command_callback(self, speed_msg):
        self.contact_speed = speed_msg.data

    def striker_state_callback(self, striker_state_msg):
        pass


def main():
    rospy.init_node('planner_node', anonymous=True)

    table_width = rospy.get_param("table/width")
    table_length = rospy.get_param("table/length")
    goal_width = rospy.get_param("table/goal_width")
    puck_diameter = rospy.get_param("table/puck_diameter")
    striker_diameter = rospy.get_param("robot/striker_diameter")
    robot_min_y = rospy.get_param("robot/y_min")
    default_contact_speed = rospy.get_param("robot/default_contact_speed")
    PlannerNode(puck_diameter=puck_diameter, striker_diameter=striker_diameter,
                table_width=table_width, table_length=table_length,
                goal_width=goal_width, default_contact_y_pos=robot_min_y,
                default_contact_speed=default_contact_speed)


if __name__=='__main__':
    main()

