#!/usr/bin/env python3

# This script will subscribe to all publihsing picam nodes.
# Data will be stored locally and published via web server.

import rospy
import sys
# import collections
import numpy as np
import time
import Registration as reg

# main will look for new topics and try to subscribe to them
# if the topic is not a camera subscription, it will be deregistered
if __name__ == '__main__':

    # Initialize node
    rospy.init_node('picam_subscriber_node')
    rospy.loginfo("Picam Subscriber has been started")

    pulse = .25 # .25/Hz = 4 seconds
    rate = rospy.Rate(pulse) # set rate

    # query list of topics and see if there is a new one
    while not rospy.is_shutdown():
        # get list of current topics and active subscriptions
        cur_topics = rospy.get_published_topics()
        rospy.loginfo("cur_topics:")
        rospy.loginfo(cur_topics)
        activeSubscriptions = reg.Registration.get_active_subscriptions()
        rospy.loginfo("activeSubscriptions:")
        rospy.loginfo(activeSubscriptions)

        # look for new topics and register new ones
        for topic in cur_topics:
            rospy.loginfo("checking: {} {} {} ".format(str(topic), str(topic[0]), str(topic[1])))
            if topic[1] == 'std_msgs/Int16MultiArray':
                rospy.loginfo("found valid topic to subscribe to")
                if topic[0] not in activeSubscriptions:
                    rospy.loginfo("{} is not active".format(topic[0]))
                    reg.Registration(topic[0])

        # look for topics that are no longer being published
        activeSubscriptions = reg.Registration.get_active_subscriptions()
        cur_topics = [x[0] for x in rospy.get_published_topics()]
        rospy.loginfo("cur_topics:")
        rospy.loginfo(cur_topics)
        rospy.loginfo("activeSubscriptions:")
        rospy.loginfo(activeSubscriptions)
        for activeTopic in activeSubscriptions:
            rospy.loginfo("Checking: {}".format(activeTopic))
            if activeTopic not in cur_topics:
                reg.Registration.unRegisterCamera(activeTopic)

        rate.sleep() # this will 'pulse' the loop at the rate
