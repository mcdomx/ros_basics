#!/bin/bash

# ROSCORE NODE

echo "********************************************************"
echo "Starting roscore"
echo "********************************************************"

# Set environment to execute ROS commands
source /catkin_ws/devel/setup.bash

rosparam set /registry_host $(hostname)
echo ">>>>>> /registry_host set to $(hostname)"

roscore
echo ">>>>>> roscore has stopped"


