#!/usr/bin/env python

import rospy

if __name__ == '__main__':
        rospy.init_node('counting_server')
        rospy.loginfo("Counting server has been started")

        # stops and waits for here until message received
        rospy.spin()

        rospy.loginfo("exiting counting_server.py")
