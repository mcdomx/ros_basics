#!/bin/sh

# TURTLESIM NODE

echo "********************************************************"
echo "Waiting for roscore to start on $ROS_MASTER_URI"
echo "ROS_HOSTNAME: $ROS_HOSTNAME"
echo "********************************************************"
while ! (rosnode list | grep rosout); do sleep 5 ; done
echo ">>>>>>>>>>>> roscore is running on $ROS_MASTER_URI"

rosrun turtlesim turtlesim_node
