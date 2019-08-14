#!/bin/sh

echo "********************************************************"
echo "SERVICE SERVER NODE"
echo "Waiting for roscore to start on $ROS_MASTER_URI"
echo "ROS_HOSTNAME: $ROS_HOSTNAME"
echo "ROS_IP: $ROS_IP"
echo "********************************************************"

# Give time to startup
sleep 2

while ! (rosnode list | grep rosout); do echo "waiting..."; sleep 5 ; done

python /catkin_ws/src/service_server_pkg/src/service_server.py
# rosrun service_server_pkg service_server.py

echo ">>>>>>>>>>>> service server is running on master: $ROS_MASTER_URI"
