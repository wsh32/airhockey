import rospy

from std_msgs.msg import Int16
from geometry_msgs.msg import PointStamped


# Super dirty glue code for sprint 1
class GlueNode:
    def __init__(self, puck_lower=85, puck_upper=420, striker_lower=0,
                 striker_upper=360, lpf_coef=0.125):
        self.puck_position_subscriber = rospy.Subscriber(
            "/vision/puck/puck_position", PointStamped, self.puck_callback)
        self.motor_position_publisher = rospy.Publisher(
            "/arduino/command/striker_pos", Int16, queue_size=3)

        self.puck_lower = puck_lower
        self.puck_upper = puck_upper
        self.striker_lower = striker_lower
        self.striker_upper = striker_upper
        self.striker_range = striker_upper - striker_lower

        self.last_command = self.puck_lower
        self.lpf_coef = lpf_coef

        rospy.spin()

    def puck_callback(self, puck_position_msg):
        position_pcnt = (puck_position_msg.point.y - self.puck_lower) / \
                (self.puck_upper - self.puck_lower)
        striker_position_cmd = position_pcnt * self.striker_range + \
                self.striker_lower

        striker_position_filtered = self.last_command * self.lpf_coef + \
            striker_position_cmd * (1 - self.lpf_coef)
        self.last_command = striker_position_filtered

        self.motor_position_publisher.publish(Int16(
            data=int(striker_position_filtered)))


def main():
    rospy.init_node("glue_node", anonymous=True)
    GlueNode()

if __name__=='__main__':
    main()

