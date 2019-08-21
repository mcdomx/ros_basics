#!/bin/bash

# PICAM NODE

echo "********************************************************"
echo "PICAM NODE"
echo "Waiting for roscore to start on $ROS_MASTER_URI"
echo "ROS_HOSTNAME: $ROS_HOSTNAME"
echo "ROS_IP: $ROS_IP"
echo "********************************************************"

# Set environment to execute ROS commands
source /catkin_ws/devel/setup.bash

while ! (rosnode list | grep rosout); do echo "waiting..."; sleep 5 ; done

# Start picam
# python /catkin_ws/src/master_pkg/src/picam.py
rosrun master_pkg picam.py

echo ">>>>>>>>>>>> picam is running on $ROS_MASTER_URI"


