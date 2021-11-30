import rospy

import yaml
import os

import numpy as np

from std_msgs.msg import Header
from geometry_msgs.msg import Point, PointStamped
from sensor_msgs.msg import Image

import trajectory
from trajectory import TrajectoryCalculator


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
        contact_x_pos = (puck_state[trajectory.X_VEL] * time_to_contact
                         + puck_state[trajectory.X_POS])

        return time_to_contact, contact_x_pos, contact_y_pos

    def compute_optimal_striker_contact_state(self, puck_state, striker_state,
                                              target_pos, contact_y_pos=6,
                                              contact_speed=0):
        time, puck_x, puck_y = self.compute_optimal_puck_contact_position
        relative_target_position = (np.array(target_pos)
                                    - np.array([puck_x, puck_y]))

        # Correct relative puck velocity to the moving striker
        # Striker is constrained to move in the direction of the target at the
        # speed of contact_speed.
        striker_vel = contact_speed * (relative_target_position /
                                       np.linalg.norm(relative_target_position))
        relative_puck_x_vel = puck_state[trajectory.X_VEL] + striker_vel[0]
        relative_puck_y_vel = puck_state[trajectory.Y_VEL] + striker_vel[1]

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

        return (striker_position[0], striker_position[1],
                striker_vel[0], striker_vel[1])


class PlannerNode:
    def __init__(self):
        rospy.spin()


def main():
    rospy.init_node('planner_node', anonymous=True)

    PuckTrackingNode()


if __name__=='__main__':
    main()

