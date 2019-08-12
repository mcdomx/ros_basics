#!/usr/bin/env python

import rospy

if __name__ == '__main__':
        rospy.init_node('first_node')
        rospy.loginfo("Testnode has been started")

        # set rate at 100 hrz (100 milliseconds)
        rate=rospy.Rate(10) # in milliseconds

        # while the node is running (not shutdown)
        i = 0
        while not rospy.is_shutdown():
            i = i+1
            rospy.loginfo("Hi {:f}".format(i))
            rate.sleep() # this will 'pulse' the loop at the rate

        rospy.loginfo("existing testnode.py")
