#!/usr/bin/env python3

# This script will subscribe to all publihsing picam nodes.
# Data will be stored locally and published via web server.

import rospy
import sys
import collections
import numpy as np

# from std_msgs.msg import UInt8MultiArray
from std_msgs.msg import Int16MultiArray

from rospy.numpy_msg import numpy_msg
from std_msgs.msg import Int8

# This class will instantiate a new Subscriber instance
# when a new topic is recognized in the network.
class RegisterCamera:
    def __init__(new_topic):
        # Create a subscriber
        new_subscription = rospy.Subscriber(new_topic, Int16MultiArray, callback=callback_receive_data, callback_args=(new_topic, "other_arg"))





# called when published
def callback_receive_data(msg, args):
    rospy.loginfo(str(args[0]))
    try:
        rospy.loginfo(msg.layout)
        rospy.loginfo(type(msg.data))
        resized_data = np.resize(msg.data, (msg.layout.dim[1].size, msg.layout.dim[0].size, msg.layout.dim[2].size))
        rospy.loginfo(resized_data.shape)
    except:
        

    # save data somewhere so that the webserver can access it
    # overwrite anything that was already there.



if __name__ == '__main__':

    rospy.init_node('picam_subscriber_node')
    rospy.loginfo("Picam Subscriber has been started")

    # Create a subscriber
    subsciber_pidev1 = rospy.Subscriber("/pidev2_images", Int16MultiArray, callback=callback_receive_data, callback_args=("pidev1", "other_arg"))
    # subsciber_pidev1 = rospy.Subscriber("/pidev2_images", UInt8MultiArray, callback=callback_receive_data, callback_args=("pidev1", "other_arg"))
    # subsciber_pidev1 = rospy.Subscriber("/pidev2_images", numpy_msg(Int8), callback=callback_receive_data, callback_args=("pidev1", "other_arg"))

    # stops and waits here without advancing
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print('Stopping Picam Subscriber.....')
        sys.exit(2)

    sys.exit(0)
