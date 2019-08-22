#!/usr/bin/env python3

# This script will subscribe to all publihsing picam nodes.
# Data will be stored locally and published via web server.

import rospy
import sys

from std_msgs.msg import UInt8MultiArray


# called when published
def callback_receive_data(msg, host):
    rospy.loginfo("Message received from: ", host)
    rospy.loginfo(msg.layout)
    rospy.loginfo(msg.data)

    # save data somewhere so that the webserver can access it
    # overwrite anything that was already there.



if __name__ == '__main__':

    rospy.init_node('picam_subscriber_node')
    rospy.loginfo("Picam Subscriber has been started")

    # Create a subscriber
    subsciber_pidev1 = rospy.Subscriber("/pidev2_images", UInt8MultiArray, callback=callback_receive_data, callback_args=("pidev1"))

    # stops and waits here without advancing
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print('Stopping Picam Subscriber.....')
        sys.exit(2)

    sys.exit(0)
