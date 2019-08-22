#!/bin/sh

# ROSCORE NODE

echo "********************************************************"
echo "Starting roscore"
echo "********************************************************"

# Set environment to execute ROS commands
source /catkin_ws/devel/setup.bash

roscore
echo ">>>>>>>>>>>> roscore has started"


