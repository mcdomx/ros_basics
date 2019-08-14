#!/usr/bin/env python

import rospy
from std_msgs.msg import String
# import signal
import sys

# handle kill command
# def signal_handler(sig, frame):
#     print('Stopping .....')
#     sys.exit(0)

# called when published
def callback_receive_data(msg):
    rospy.loginfo("Message received : ")
    rospy.loginfo(msg)

if __name__ == '__main__':
    # signal.signal(signal.SIGINT, signal_handler)
    rospy.init_node('subscriber_node')
    rospy.loginfo("Subscriber has been started")

    # Create a subscriber
    pub = rospy.Subscriber("/publisher_topic", String, callback_receive_data)

    # stops and waits here without advancing
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print('Stopping .....')
        sys.exit(0)

    sys.exit(0)
