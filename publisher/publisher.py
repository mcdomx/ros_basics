#!/usr/bin/env python

import rospy
from std_msgs.msg import String
# import signal
import sys

# handle kill command
# def signal_handler(sig, frame):
#     print('Stopping .....')
#     sys.exit(0)

if __name__ == '__main__':
        rospy.init_node('publisher_node')
        rospy.loginfo("Publisher has been started")

        # Create a publisher
        pub = rospy.Publisher("/publisher_topic", String, queue_size=10)

        rate = rospy.Rate(2)

        print("Created /publisher_topic.  Starting to publish messages...")
        # while the node is running (not shutdown)
        i = 1
        try:
            while not rospy.is_shutdown():
                msg = String()
                msg.data = "News radio info .. {}".format(i)
                pub.publish(msg)
                print ("..published message .. {}".format(i))
                i = i + 1
                rate.sleep() # this will 'pulse' the loop at the rate
        except KeyboardInterrupt:
            print("Stopping ....")
            sys.exit(0)

        sys.exit(0)
