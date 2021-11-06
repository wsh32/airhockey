import rosbag
from std_msgs.msg import Int16

import matplotlib.pyplot as plt

bag = rosbag.Bag('/home/wsh32/airhockey/bags/2021-11-04-00-46-51.bag')

data = []
for topic, msg, t in bag.read_messages(topics=['/arduino/command/striker_pos']):
    data.append(msg.data)


plt.plot(data)
plt.show()

