#!/bin/sh

echo "********************************************************"
echo "PUBLISHER NODE"
echo "Waiting for roscore to start on $ROS_MASTER_URI"
echo "ROS_HOSTNAME: $ROS_HOSTNAME"
echo "ROS_IP: $ROS_IP"
echo "********************************************************"

# Give time to startup
sleep 2

while ! (rosnode list | grep rosout); do echo "waiting..."; sleep 5 ; done

echo ">>>>>>>>>>>> publisher is running on master: $ROS_MASTER_URI"

python /catkin_ws/src/master_pkg/src/publisher.py
# rosrun master_pkg publisher.py
