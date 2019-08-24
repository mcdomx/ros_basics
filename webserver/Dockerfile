
# webserver
# https://github.com/jacksonliam/mjpg-streamer



# Need to run container with the device: docker run -t -i -p 8080:8080/tcp --device=/dev/vchiq webserver
# The stream can be viewed: http://pidev2.local:8080/?action=stream
# http://pidev2.local:8080 shows various html options

ARG RASPBIAN_VERSION=jessie
FROM raspbian/$RASPBIAN_VERSION

ARG RASPBIAN_VERSION
ARG DEBIAN_FRONTEND=noninteractive

# Install Dependencies and Utilities
RUN apt-get update
RUN apt-get install -y git nano unzip iputils-ping make cmake libjpeg8-dev gcc g++
RUN apt-get install -y libraspberrypi-dev

# Build mjpg_streamer
RUN git clone https://github.com/jacksonliam/mjpg-streamer.git 
WORKDIR /mjpg-streamer/mjpg-streamer-experimental
RUN make && make install && chmod +x docker-start.sh


# EXPOSE 8080/TCP

ENTRYPOINT ["/mjpg-streamer/mjpg-streamer-experimental/docker-start.sh", "output_http.so -w ./www"]
CMD ["input_raspicam.so"]
