#!/usr/bin/env python

import rospy
from std_msgs.msg import String

# called when published
def callback_receive_data(msg):
        rospy.loginfo("Message received : ")
        rospy.loginfo(msg)

if __name__ == '__main__':
        rospy.init_node('subscriber_node')
        rospy.loginfo("Subscriber has been started")

        # Create a subscriber
        pub = rospy.Subscriber("/subscriber_topic", String, callback_receive_data)

        # stops and waits for here until message received
        rospy.spin()

        rospy.loginfo("existing subscriber_node.py")
