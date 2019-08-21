#!/bin/bash

echo "********************************************************"
echo "SERVICE SERVER NODE"
echo "Waiting for roscore to start on $ROS_MASTER_URI"
echo "ROS_HOSTNAME: $ROS_HOSTNAME"
echo "ROS_IP: $ROS_IP"
echo "********************************************************"

# Give time to startup
# sleep 3

while ! (rosnode list | grep rosout); do echo "waiting..."; sleep 5 ; done

# Set environment to execute ROS commands
source /catkin_ws/devel/setup.bash

# python /catkin_ws/src/master_pkg/src/service_server.py
# bash -c 'rosrun master_pkg service_server.py'
rosrun master_pkg service_server.py

echo ">>>>>>>>>>>> service server is running on master: $ROS_MASTER_URI"
