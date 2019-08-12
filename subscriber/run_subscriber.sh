#!/bin/sh

echo "********************************************************"
echo "SUBSCRIBER NODE"
echo "Waiting for roscore to start on $ROS_MASTER_URI"
echo "ROS_HOSTNAME: $ROS_HOSTNAME"
echo "ROS_IP: $ROS_IP"
echo "********************************************************"

# Give time to startup
sleep 2

while ! (rosnode list | grep rosout); do echo "waiting..."; sleep 5 ; done

python /catkin_ws/src/subscriber_pkg/src/subscriber.py
# rosrun subscriber_pkg subscriber.py

echo ">>>>>>>>>>>> subscriber is running on master: $ROS_MASTER_URI"
