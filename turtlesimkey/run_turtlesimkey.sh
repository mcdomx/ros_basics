#!/bin/sh

# TURTLESIM KEYBOARD NODE

echo "********************************************************"
echo "Waiting for turtlesim to start on $ROS_MASTER_URI"
echo "ROS_HOSTNAME: $ROS_HOSTNAME"
echo "********************************************************"

while ! (rosnode list | grep turtlesim) ; do sleep 5 ; done
echo ">>>>>>>>>>>> turtlesim is running on $ROS_MASTER_URI"

rosrun turtlesim turtle_teleop_key
