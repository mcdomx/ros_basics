#!/bin/sh

# PICAM NODE

echo "********************************************************"
echo "PICAM NODE"
echo "Waiting for roscore to start on $ROS_MASTER_URI"
echo "ROS_HOSTNAME: $ROS_HOSTNAME"
echo "********************************************************"
while ! (rosnode list | grep rosout); do sleep 5 ; done
echo ">>>>>>>>>>>> picam is running on $ROS_MASTER_URI"

"Starting picam...."
python /catkin_ws/src/picam/src/picam.py
# rosrun picam picam.py



