#!/bin/sh

echo "********************************************************"
echo "SERVICE SERVER NODE"
echo "Waiting for roscore to start on $ROS_MASTER_URI"
echo "ROS_HOSTNAME: $ROS_HOSTNAME"
echo "ROS_IP: $ROS_IP"
echo "********************************************************"


while ! (rosnode list | grep rosout); do echo "waiting..."; sleep 5 ; done

source ~/.bashrc

python /catkin_ws/src/master_pkg/src/service_server.py
# rosrun master_pkg service_server.py

echo ">>>>>>>>>>>> service server is running on master: $ROS_MASTER_URI"
