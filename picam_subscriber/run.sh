#!/bin/bash

echo "********************************************************"
echo "SUBSCRIBER NODE"
echo "Waiting for roscore to start on $ROS_MASTER_URI"
echo "ROS_HOSTNAME: $ROS_HOSTNAME"
echo "ROS_IP: $ROS_IP"
echo "********************************************************"

# Set environment to execute ROS commands
source /catkin_ws/devel/setup.bash

while ! (rosnode list | grep rosout); do echo "waiting..."; sleep 5 ; done

# Start picam_subscriber.py
# python /catkin_ws/src/master_pkg/src/subscriber.py
rosrun master_pkg picam_subscriber.py

echo ">>>>>>>>>>>> picam_subscriber is running on master: $ROS_MASTER_URI"
