#!/bin/sh

# TESTNODE NODE

echo "********************************************************"
echo "TESTNODE NODE"
echo "Waiting for roscore to start on $ROS_MASTER_URI"
echo "ROS_HOSTNAME: $ROS_HOSTNAME"
echo "********************************************************"

# Give time to startup
sleep 2

while ! (rosnode list | grep rosout); do echo "waiting..."; sleep 5 ; done

python /catkin_ws/src/testpackage/src/testnode.py
# rosrun testpackage testnode.py

echo ">>>>>>>>>>>> testnode is running on $ROS_MASTER_URI"

