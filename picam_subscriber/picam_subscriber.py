#!/usr/bin/env python3

# This script will subscribe to all publihsing picam nodes.
# Data will be stored locally and published via web server.

import rospy
import sys
import collections
import numpy as np
import time

# from std_msgs.msg import UInt8MultiArray
from std_msgs.msg import Int16MultiArray

from rospy.numpy_msg import numpy_msg
from std_msgs.msg import Int8

# This class will instantiate a new Subscriber instance
# when a new topic is recognized in the network.
class Registration:
    activeSubscriptions = {}
    deactivatedTopics = []

    # called when published
    def callback_receive_data(msg, args):
        rospy.loginfo(str(args[0]))
        try:
            rospy.loginfo(msg.layout)
            rospy.loginfo(type(msg.data))
            resized_data = np.resize(msg.data, (msg.layout.dim[1].size, msg.layout.dim[0].size, msg.layout.dim[2].size))
            rospy.loginfo(resized_data.shape)
        except:
            # Failed call - deregister subscriber
            Registration.unRegisterCamera(args[0])


    def __init__(new_topic):

        if new_topic in deactivatedTopics:
            rospy.loginfo("{} has already once been deactivated because it was not a camera.  Not registering".format(new_topic))
            return None

        if new_topic in activeSubscriptions.keys():
            rospy.loginfo("{} is already active.  No action taken.".format(new_topic))
            return None

        # Create a subscriber
        new_subscription = rospy.Subscriber(new_topic, Int16MultiArray, callback=callback_receive_data, callback_args=(new_topic, "other_arg"))

        activeSubscriptions[new_topic] = new_subscription
        return new_subscription



    @staticmethod
    def unRegisterCamera(topic_name):
        if topic_name not in activeSubscriptions:
            rospy.loginfo("{} not an active registration.  No action taken.".format(topic_name))
            return None

        subscription = activeSubscriptions[topic_name]
        deactivatedTopics.append(topic_name)
        subscription.unregister()
        return topic_name

    @staticmethod
    def get_active_subscriptions():
        return activeSubscriptions.keys()




# called when published
def callback_receive_data(msg, args):
    rospy.loginfo(str(args[0]))
    try:
        rospy.loginfo(msg.layout)
        rospy.loginfo(type(msg.data))
        resized_data = np.resize(msg.data, (msg.layout.dim[1].size, msg.layout.dim[0].size, msg.layout.dim[2].size))
        rospy.loginfo(resized_data.shape)
    except:
        # Failed call - deregister subscriber
        Registration.unRegisterCamera(args[0])

    # save data somewhere so that the webserver can access it
    # overwrite anything that was already there.

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
        activeSubscriptions = Registration.get_active_subscriptions()
        rospy.loginfo("activeSubscriptions:")
        rospy.loginfo(activeSubscriptions)

        # look for new topics and register new ones
        for topic in cur_topics:
            rospy.loginfo("checking: ", topic, topic[0], topic[1])
            if topic[1] == 'std_msgs/Int16MultiArray':
                rospy.loginfo("found valid topic to subscribe to")
                if topic[0] not in activeSubscriptions:
                    rospy.loginfo("{} is not active".format(topic[0]))
                    rv = Registration(topic[0])
                        rospy.loginfo("Registrtion result: ", rv)
                        if rv is not None:
                            rospy.loginfo("{} has been subscribed.".format(topic[0]))

        rate.sleep() # this will 'pulse' the loop at the rate




# Old main - subsequently made subscribing a class
# if __name__ == '__main__':
#
#     rospy.init_node('picam_subscriber_node')
#     rospy.loginfo("Picam Subscriber has been started")
#
#     # Create a subscriber
#     subsciber_pidev1 = rospy.Subscriber("/pidev2_images", Int16MultiArray, callback=callback_receive_data, callback_args=("pidev1", "other_arg"))
#
#     # stops and waits here without advancing
#     try:
#         rospy.spin()
#     except KeyboardInterrupt:
#         print('Stopping Picam Subscriber.....')
#         sys.exit(2)
#
#     sys.exit(0)
