#!/usr/bin/env python

import rospy
from std_msgs.msg import String

if __name__ == '__main__':
        rospy.init_node('publisher_node')
        rospy.loginfo("Publisher has been started")

        # Create a publisher
        pub = rospy.Publisher("/publisher_topic", String, queue_size=10)

        rate = rospy.Rate(2)

        print("Created /publisher_topic.  Starting to publish messages...")
        # while the node is running (not shutdown)
        i = 1
        while not rospy.is_shutdown():
            msg = String()
            msg.data = "News radio info .. {}".format(i)
            pub.publish(msg)
            print ("..published message .. {}".format(i))
            i = i + 1
            rate.sleep() # this will 'pulse' the loop at the rate

        rospy.loginfo("exiting publisher.py")
