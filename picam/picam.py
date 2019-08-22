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

from std_msgs.msg import UInt8MultiArray


if __name__ == '__main__':

    publish_rate_Hz = 1 # 1/Hz = seconds
    resolution = (320, 240)

    # Assign nodename - if not set, exit
    try:
        nodename = os.getenv('NODENAME')
        rospy.init_node(nodename)
    except:
        rospy.loginfo("PiCamera requires a NODENAME environment variable to be set.")
        rospy.loginfo("Rerun this container with the option:")
        rospy.loginfo("      -e NODENAME=$(hostname)")
        exit(1)

    # Create a publisher topic
    topicname = "/" + nodename + "_images"
    pub = rospy.Publisher(topicname, UInt8MultiArray, queue_size=10)


    rospy.loginfo("PiCamera is publishing on {}".format(topicname))


    # set rate in milliseconds)
    rate = rospy.Rate(publish_rate_Hz)

    camera.resolution = resolution
    camera.framerate = framrate

    camera = picamera.PiCamera()
    output = picamera.array.PiRGBArray(camera)

    i = 1
    while not rospy.is_shutdown():
        try:
            # output = np.empty((480, 640, 3), dtype=np.uint8)
            # camera.capture(output, 'rgb')
            # print('%d - Captured %dx%dx%d image' % (
            #         i, output.shape[0], output.shape[1], output.shape[2]))
            # Here, we want to publish the array value
            with picamera.PiCamera() as camera:
                with picamera.array.PiRGBArray(camera) as output:
                    camera.capture(output, 'rgb')
                    pub.publish(output)
                    print('%d - Published %dx%dx%d image' % (
                            i, output.shape[0], output.shape[1], output.shape[2]))
            i += 1

            rate.sleep() # this will 'pulse' the loop at the rate

        # If SIGINT is received
        except KeyboardInterrupt:
            rospy.loginfo("Stopped publishing: ", nodename, topicname)
            exit(2)
