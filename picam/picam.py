#!/usr/bin/env python3

# This script will allow a RaspberryPi to publish its camera image data
# as an array to a local ROS network.
#
# The data will be published as a topic with a name in the form of
# "/devicename_images", so if the device name is pidev1 then the topic will
# be "/pidev1_images".
#
# The node will have the same name as the device.




# import cv2
# import matplotlib.pyplot as plt
import time
import os
import picamera
import picamera.array
import rospy
import numpy as np
from array import array

# from std_msgs.msg import UInt8MultiArray
from std_msgs.msg import Int16MultiArray
from std_msgs.msg import MultiArrayLayout
from std_msgs.msg import MultiArrayDimension

from rospy.numpy_msg import numpy_msg
from std_msgs.msg import Int8

if __name__ == '__main__':

    # Assign nodename - if not set, exit
    try:
        nodename = os.getenv('NODENAME')
        rospy.init_node(nodename)
    except:
        rospy.loginfo("PiCamera requires a NODENAME environment variable to be set.")
        rospy.loginfo("Rerun this container with the option:")
        rospy.loginfo("      -e NODENAME=$(hostname)")
        exit(1)

    publish_rate_Hz = 1 # 1/Hz = seconds
    rate = rospy.Rate(publish_rate_Hz) # set rate
    resolution = (320, 240)
    channels = 3

    camera = picamera.PiCamera()
    img_array = picamera.array.PiRGBArray(camera)
    camera.resolution = resolution
    # camera.framerate = framerate

    # Create a publisher topic
    topicname = "/" + nodename + "_images"
    pub = rospy.Publisher(topicname, Int16MultiArray, queue_size=10)
    # pub = rospy.Publisher(topicname, UInt8MultiArray, queue_size=10)
    # pub = rospy.Publisher(topicname, numpy_msg(Int8), queue_size=10)

    rospy.loginfo("PiCamera is publishing on {}".format(topicname))

    # Published data is a dictionary with 'layout' and 'data' as elements
    # 'layout' is an array of dimension properties (shape[0], shape[1], shape[2])
    # where each element in a dictionay consisting of 'label', 'size' and 'stride'
    # 'data' is the array in the layout dimensions

    height_dim = MultiArrayDimension('height',  resolution[1], resolution[1]*resolution[0]*channels)
    width_dim = MultiArrayDimension('width',  resolution[0], resolution[0]*channels)
    channel_dim = MultiArrayDimension('channel',  channels, channels)

    dim = (height_dim, width_dim, channel_dim)
    data_offset = 0

    layout = MultiArrayLayout(dim=dim, data_offset=data_offset)

    img_array = np.empty((320, 240, 3), dtype=np.uint8)
    i = 0

    while not rospy.is_shutdown():

        try:
            camera.capture(img_array, 'rgb')

            # pub.publish(img_array)
            # pub.publish(UInt8MultiArray(layout=layout, data=list(img_array.flatten())))
            pub.publish(Int16MultiArray(layout=layout, data=list(img_array.flatten())))
            print('%d - Published %dx%dx%d image' % (
                    i, img_array.shape[0], img_array.shape[1], img_array.shape[2]))
            # Here, we want to publish the array value
            # with picamera.PiCamera() as camera:
            #     with picamera.array.PiRGBArray(camera) as output:
            #         camera.capture(output, 'rgb')
            #         pub.publish(output)
            #         print('%d - Published %dx%dx%d image' % (
            #                 i, output.shape[0], output.shape[1], output.shape[2]))
            i += 1

            rate.sleep() # this will 'pulse' the loop at the rate

        # If SIGINT is received
        except KeyboardInterrupt:
            rospy.loginfo("Stopped publishing: ", nodename, topicname)
            pub.unregister()
            exit(2)

    rospy.loginfo("Stopped publishing: ", nodename, topicname)
    pub.unregister()
    exit(2)
