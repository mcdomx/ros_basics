# ros_basics
ROS Learning Environment

Installed Hypriot on pi device.

Each part of this project is designed to run in a docker container.

roscore must be started so that each node has a central point of communication.  Only one roscore instance can be running on a network and each node will need a unique name.

Build containers from their directories:
docker build -t rosbasic  .
docker build -t rosnode  .
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
docker build -t turtlesimkey --rm .

container 1:
docker run -it --rm --name turtlesim --env ROS_MASTER_URI=http://$LOCALIP:11311/  -e DISPLAY=$LOCALIP:0 -v /tmp/.X11-unix:/tmp/.X11-unix:ro turtlesim
	rosrun turtlesim turtlesim_node

container 2:
docker run -it --rm --net=host --name turtlesim-key --env ROS_MASTER_URI=http://$LOCALIP:11311/  -e DISPLAY=$LOCALIP:0 -v /tmp/.X11-unix:/tmp/.X11-unix:ro turtlesim	
	rosrun turtlesim turtlesim_teleop_key

https://docs.docker.com/network/network-tutorial-overlay/
On host1, initialize the node as a swarm (manager).
On host2, join the node to the swarm (worker).
On host1, create an attachable overlay network (test-net).
On host1, run an interactive alpine container (alpine1) on test-net.
On host2, run an interactive, and detached, alpine container (alpine2) on test-net.
On host1, from within a session of alpine1, ping alpine2.

SETUP Swarm Mode:
Open ports:
	TCP port 2377 for cluster management communications
	TCP and UDP port 7946 for communication among nodes
	UDP port 4789 for overlay network traffic

On master host:
docker swarm init --advertise-addr=10.0.1.5
	
On worker:
	docker swarm join --token SWMTKN-1-4tf6z2a0rvt2qnkghmomd74t0u74gxmhnq3l2ovn0rs9x2hq92-7mn2l5cq0e3tl7mwtc52ohpl8 --advertise-addr 10.0.1.8 10.0.1.5:2377	




To communicate between containers, you need to create a network:

	docker network create rosnet

and then start every container using --net rosnet

	docker run -it --rm --net rosnet --name roscore -p 11311:11311 -e DISPLAY=$LOCALIP:0 -v /tmp/.X11-unix:/tmp/.X11-unix:ro roscore roscore

	docker run --name publisher --env ROS_MASTER_URI=http://10.0.1.5:11311/ --env ROS_IP=10.0.1.8 --tty=True publisher
	
	docker run --name subscriber  --tty=True  --rm --env ROS_MASTER_URI --env ROS_IP  subscriber


PORTAINER
docker run -d -p 9000:9000 -v /var/run/docker.sock:/var/run/docker.sock portainer/portainer





USING DOCKER-COMPOSE
You can buld and run from the root using:
docker-compose -f docker-compose.yaml up

or force a new build:
docker-compose -f docker-compose.yaml up --build

or just build:
docker-compose -f docker-compose.yaml build


You can clean using:
docker-compose -f docker-compose.yaml rm
