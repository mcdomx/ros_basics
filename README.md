# ros_basics
ROS Learning Environment

Installed Hypriot on pi device.
Install on pi device to get access to mac's hostname from pi:
	sudo apt-get install libnss-mdns

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

docker run -it --rm --name roscore -P -e DISPLAY=$LOCALIP:0 -v /tmp/.X11-unix:/tmp/.X11-unix:ro roscore roscore

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

	docker network create --attachable rosnet

and then start every container using --net rosnet

	docker run -it --name roscore -p 11311:11311 -e DISPLAY=$LOCALIP:0 -v /tmp/.X11-unix:/tmp/.X11-unix:ro roscore roscore

	docker run --name publisher --env ROS_MASTER_URI=http://10.0.1.5:11311/ --env ROS_IP=10.0.1.5 --tty=True publisher
	
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





CREATE DOCKER_MACHINE INSTANCE
docker-machine create --driver virtualbox --engine-env DOCKER_TLS_VERIFY="0" default 
docker-machine create -d virtualbox --engine-env DOCKER_TLS=no default
docker-machine create -d virtualbox --engine-env DOCKER_TLS=no --engine-opt host=tcp://0.0.0.0:2375 default
docker-machine create --driver virtualbox  manager1

stop the machine and forward the virtualbox ports
Open ports:
TCP port 2377 for cluster management communications
TCP and UDP port 7946 for communication among nodes
UDP port 4789 for overlay network traffic

docker-machine stop manager1
VBoxManage modifyvm "manager1" --natpf1 "guestssh,tcp,,2377,,2377"
VBoxManage modifyvm "manager1" --natpf1 "guestssh,tcp,,7946,,7946"
VBoxManage modifyvm "manager1" --natpf1 "guestssh,udp,,7946,,7946"
VBoxManage modifyvm "manager1" --natpf1 "guestssh,udp,,4789,,4789"
(note these may all be setup automatically when you create the swarm in the machine)

open VirtualBox and add a 3rd network adapter bridged to Wifi

docker-machine start manager1

GET THE MACHINE'S IP ADDRESS
docker-machine ip manager1

SSH INTO MACHINE
docker-machine start manager1

GET MACHINE IP and START SWARM
docker swarm init --advertise-addr $(docker-machine ip manager1)

ON WORKER MACHINE
docker-machine create --driver virtualbox  worker1
--open network adapter (see above)


GET THE MACHINE'S IP ADDRESS
docker-machine ip worker1

SSH INTO WORKER MACHINE
docker-machine ssh worker1

JOIN SWARM ON WORKER


GET ENV VARIABLES
docker-machine env default
(use the command to transfer the listed variables to your local shell -- see next step)

CONNECT MACHINE TO SHELL
eval "$(docker-machine env default)"

UNSET TLS MODE
unset DOCKER_TLS_VERIFY

MISC MACHINE COMMANDS
docker-machine ls
docker-machine ip default
docker-machine stop default
docker-machine start default

INITIALIZE SWARM
docker-machine ssh default "docker swarm init --advertise-addr <default ip>"
(note port 2377 is for swarm management. 2376 is docker-daemon, don't use it for swarm actions)

JOIN SWARM
On remote machine:
docker-machine ssh default "docker swarm join --token SWMTKN-1-3mzbb4n9e61ucxzmxv674asuw7538meu1djsx21vwe29ldqxx2-bn4cfyqw6dv04gc7wkiklpalc 192.168.99.106:2377"



CREATE OVERLAY NETWORK
docker network create --driver overlay rosnet




START ROSCORE SERVICE
docker service create --name roscore --env DISPLAY=10.0.1.5:0 --hostname roscore --mount type=bind,source=/tmp/.X11-unix,destination=/tmp/.X11-unix:ro --publish 11311:11311 --network rosnet roscore roscore


START PUBLISHER SERVICE
docker service create --name publisher --env DISPLAY=10.0.1.5:0 --hostname publisher --mount type=bind,source=/tmp/.X11-unix,destination=/tmp/.X11-unix:ro --env ROS_MASTER_URI=http://roscore:11311/ --env ROS_HOSTNAME=publisher --tty=True --network rosnet publisher

START SUBSCRIBER SERVICE
docker service create --name subscriber --env DISPLAY=10.0.1.5:0 --hostname subscriber --mount type=bind,source=/tmp/.X11-unix,destination=/tmp/.X11-unix:ro --env ROS_MASTER_URI=http://roscore:11311/ --env ROS_HOSTNAME=subscriber --tty=True --network rosnet subscriber

	add --replicas 3   to add 3 relicas of the service
