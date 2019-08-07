# ros_basics
ROS Learning Environment

Each part of this project is designed to run in a docker container.

roscore must be started so that each node has a central point of communication.  Only one roscore instance can be running on a network and each node will need a unique name.

Build containers from their directories:
docker build -t roscore --rm .
docker build -t picam --rm .

GUI SUPPORT
ON LOCAL MACHINE
Host computer will require XQuartz and socat
> brew cask install xQuartz

https://cntnr.io/running-guis-with-docker-on-mac-os-x-a14df6a76efc
Socat acts as a bridge between docker and the host system
> brew install socat

Setup bridge using socat:
> socat TCP-LISTEN:6000,reuseaddr,fork UNIX-CLIENT:\"$DISPLAY\" &

get ip address of host on the local network
> ifconfig en1 | grep 'inet0 ' | cut -d' ' -f2
or 
> ifconfig en1 | grep 'inet1 ' | cut -d' ' -f2

(can also be done by looking at router)

export DISPLAYIP=<network ip of local machine>

Enable ipaddress with xhost:
> xhost +<ip_address>






Start roscore container
docker run -it --rm --name roscore -p 11311:11311 -e DISPLAY=$LOCALIP:0 -v /tmp/.X11-unix:/tmp/.X11-unix:ro roscore roscore

Get IP of local machine:
ifconfig en1 | grep 'inet0 ' | cut -d' ' -f2
export LOCALIP=<local network ip address of machine running roscore>


Run nodes with that ROS_MASTER_URI env variable set
docker run -it --rm --name picam --env ROS_MASTER_URI=http://$LOCALIP:11311/  -e DISPLAY=$LOCALIP:0 -v /tmp/.X11-unix:/tmp/.X11-unix:ro picam

Turtle sim
docker build -t turtlesim --rm .

container 1:
docker run -it --rm --name turtlesim --env ROS_MASTER_URI=http://$LOCALIP:11311/  -e DISPLAY=$LOCALIP:0 -v /tmp/.X11-unix:/tmp/.X11-unix:ro turtlesim
	rosrun turtlesim turtlesim_node

container 2:
docker run -it --rm --name turtlesim-key --env ROS_MASTER_URI=http://$LOCALIP:11311/  -e DISPLAY=$LOCALIP:0 -v /tmp/.X11-unix:/tmp/.X11-unix:ro turtlesim	
	rosrun turtlesim turtlesim_teleop_key


USING DOCKER-COMPOSE
You can buld and run from the root using:
docker-compose -f docker-compose.yaml up

or force a new build:
docker-compose -f docker-compose.yaml up --build

or just build:
docker-compose -f docker-compose.yaml build


You can clean using:
docker-compose -f docker-compose.yaml rm
