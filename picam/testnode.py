#!/usr/bin/python

import rospy

if __name__ == '__main__':
        rospy.init_node('first_node')
        rospy.loginfo("Node has been started")

        # set rate at 1000 hrz (1000 milliseconds)
        rate=rospy.Rate(1000) # in milliseconds

        # while the node is running (not shutdown)
        while not rospy.is_shutdown():
            rospy.loginfo("Hi")
            rate.sleep() # this will 'pulse' the loop at the rate
