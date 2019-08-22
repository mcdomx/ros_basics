# RaspyCam Collector

This project will use one or several Raspberry Pi units with cameras to 
collect detected object data.  Detected object overlays can be displayed
and the objects identfied are logged for statistical analysis.

The network will require a minimum of 2 Raspberry Pi devices.  One will 
act as a ROS Master and web server.  The other will be the iimage collection 
unit which will use ROS to publish image data.  Each Raspberry Pi device will 
use Dokcer images to manage its tasks.  The image collecting Pi device 
will have a single container using ROS to capture image data and publish it.
The ROS master Pi device will have 2 containers; one will act as the ROS Master 
and the other will be a web server the will collect image data from each
Raspberry Pi and stream it.


ROS will be run inside of Dokcer containers on each of the pi devices.  Note that ROS cannot work when 
any of the containers are running on a Mac.  Docker for Mac runs docker containers inside of a 
virutal machine which complicated the comminincation between different hosts on the 
network.

This will require 2 raspberry pi devices connected to the same local network.

## Step 1 - Setup Pi devices
The Pi devices will use Hypriot images.  Hypriot is a Raspian image that is
customized to use Docker from the start.  

### Install Hypriot Flash
See github: https://github.com/hypriot/flash

### Flash SD Card:
Before starting the flash procedure, you will configure 2 files to setup the device
with a specific configuration such as WiFi information, host name, user name and password.
These configuration values are stored in a file called wlan-user-data.yaml for
user data and another file call no-uart-config.txt for basic hardware settings.

Examples of these files can be found at:
https://github.com/hypriot/flash/tree/2.3.0/sample

	<code>flash --userdata ./wlan-user-data.yaml --bootconf ./no-uart-config.txt https://github.com/hypriot/image-builder-rpi/releases/download/v1.11.1/hypriotos-rpi-v1.11.1.img.zip<\code>

### Boot Pi with New Card
Inser the card and power up the Pi.

### Pi Configurations
A few small things need to be setup to make working with the Pi device
more convenient.  Additionally, we will load the project software on to the
device.

#### Add ssh keys
Navigate the the home directory and create a directory called .ssh.

From the host computer that you will use to loginto the pi, navigate the the ~/.ssh
directory:

	cat ./id_rsa.pub | ssh <pi-user-id>@<pi-hostname>.local 'cat >> .ssh/authorized_keys'
	
This will avoid the need for a password at each login.

#### Install a Missing Library
The following library should be installed to make communciation with a mac
host a little easier:

	sudo apt-get update
	sudo apt-get install libnss-mdns
	
#### Clone the Project Repo
Create a directory to keep the project in.  I use ~/projects.
From that directory:

	git clone https://github.com/mcdomx/ros_basics.git
	

### Build containers


### Run containers to test connectivity

On pidev1
	
	docker run -it --rm --name roscore --net=host roscore 

On pidev2
	
	for picam:
	docker run --rm --name picam --env ROS_MASTER_URI=http://10.0.1.4:11311 -e ROS_HOSTNAME=10.0.1.4 -e NODENAME=$(hostname) --tty=True --device /dev/vchiq --net=host --privileged picam

	
	docker run --rm --name publisher --env ROS_MASTER_URI=http://10.0.1.27:11311 -e ROS_HOSTNAME=10.0.1.26  --tty=True --net=host publisher

On pidev1

	docker run --rm --name picam_subscriber --env ROS_MASTER_URI=http://10.0.1.4:11311 -e ROS_HOSTNAME=10.0.1.30  --tty=True --net=host picam_subscriber


### Run Service Server

On pidev1 (if roscore is not already running)

	docker run -it --rm --name roscore --net=host roscore 

On pidev2
	
	docker run --rm --name service_server --env ROS_MASTER_URI=http://10.0.1.27:11311 -e ROS_HOSTNAME=10.0.1.26 --tty=True --net=host service_server
	


## Using the Mac for Graphical Output
To get graphic output on a mac, add the following switches to the docker run statement:

	-e DISPLAY=$LOCALIP:0 -v /tmp/.X11-unix:/tmp/.X11-unix:ro

Additionally, Xquartz will need to be running on the mac



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






SETUP Swarm Mode:
Open ports:
	TCP port 2377 for cluster management communications
	TCP and UDP port 7946 for communication among nodes
	UDP port 4789 for overlay network traffic

On master host:
docker swarm init --advertise-addr=10.0.1.5
	
On worker:
	docker swarm join --token SWMTKN-1-4tf6z2a0rvt2qnkghmomd74t0u74gxmhnq3l2ovn0rs9x2hq92-7mn2l5cq0e3tl7mwtc52ohpl8 --advertise-addr 10.0.1.8 10.0.1.5:2377	







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
