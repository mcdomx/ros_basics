# This script defines the Registration class that is used
# to Subscribe and Unsubscribe to topics

import rospy
import sys
import numpy as np
import time

from std_msgs.msg import Int16MultiArray

# This class will instantiate a new Subscriber instance
# when a new topic is recognized in the network.
class Registration:
    # todo make this local only
    activeSubscriptions = {}

    # called when published
    def callback_receive_data(msg, args):
        rospy.loginfo(str(args[0]))
        try:
            # rospy.loginfo(msg.layout)
            img_array = np.resize(msg.data, (msg.layout.dim[1].size, msg.layout.dim[0].size, msg.layout.dim[2].size))
            rospy.loginfo("Received message with shape: {}".format(img_array.shape))

        except:
            # Failed call - deregister subscriber
            Registration.unRegisterCamera(args[0])


    def __init__(self, new_topic):

        if new_topic in Registration.activeSubscriptions.keys():
            rospy.loginfo("{} is already active.  No action taken.".format(new_topic))
            return None

        # Create a subscriber
        new_subscription = rospy.Subscriber(new_topic, Int16MultiArray, callback=Registration.callback_receive_data, callback_args=(new_topic, "other_arg"))

        Registration.activeSubscriptions[new_topic] = new_subscription
        rospy.loginfo("{} has been subscribed.".format(new_topic))
        return None



    @staticmethod
    def unRegisterCamera(topic_name):
        if topic_name not in Registration.activeSubscriptions:
            rospy.loginfo("{} not an active registration.  No action taken.".format(topic_name))
            return None

        subscription = Registration.activeSubscriptions[topic_name]
        subscription.unregister()
        del Registration.activeSubscriptions[topic_name]
        rospy.loginfo("Deregistered: {}".format(topic_name))
        return topic_name

    @staticmethod
    def get_active_subscriptions():
        return Registration.activeSubscriptions.keys()
