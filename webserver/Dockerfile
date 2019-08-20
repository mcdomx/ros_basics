# web server container
# FROM chunliu/docker-opencv
# FROM openhorizon/mjpg-streamer-pi3
FROM raspbian/jessie

# Install GIT
RUN apt-get update && apt-get -y install git cmake libjpeg8-dev gcc g++	

# Build mjpg_streamer
# Need to run container with the device: docker run -t -i -p 8080:8080/tcp --device=/dev/video0 image:tag
RUN git clone https://github.com/jacksonliam/mjpg-streamer.git 

WORKDIR /mjpg-streamer/mjpg-streamer-experimental

RUN make && make install

EXPOSE 8080/TCP

ENTRYPOINT ["/mjpg-streamer/mjpg-streamer-experimental/docker-start.sh", "output_http.so -w ./www"]

CMD ["input_raspicam.so"]

# ADD  run.sh run.sh
# CMD ./run.sh