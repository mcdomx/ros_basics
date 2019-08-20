# web server container
# FROM chunliu/docker-opencv
# FROM openhorizon/mjpg-streamer-pi3
FROM raspbian/jessie

# Install Basics
RUN apt-get update
RUN apt-get install -y build-essential git cmake pkg-config gcc g++ unzip nano iputils-ping
RUN apt-get install man-db

# Install OpenCV
RUN apt-get install -y libgtk2.0-dev pkg-config libavcodec-dev libavformat-dev libswscale-dev
RUN apt-get install -y python-dev python-numpy libtbb2 libtbb-dev libjpeg-dev libpng-dev libtiff-dev libjasper-dev libdc1394-22-dev

# RUN apt-get install -y libjpeg62-turbo-dev libjpeg-dev libpng-dev libtiff-dev libtiff5-dev libjpeg8-dev libpng12-dev
# RUN apt-get install -y libgtk2.0-dev pkg-config
# RUN apt-get install -y python-dev python-numpy libtbb2 libtbb-dev libjasper-dev
# RUN apt-get install -y libavcodec-dev libavformat-dev libswscale-dev libv4l-dev libdc1394-22-devinstal
# RUN apt-get install -y libxvidcore-dev libx264-dev
# RUN apt-get install -y libatlas-base-dev gfortran
# RUN apt-get install -y python3-dev

RUN apt-get purge -y wolfram-engine	

RUN wget -O opencv_contrib.zip https://github.com/Itseez/opencv_contrib/archive/3.1.0.zip
RUN unzip opencv_contrib.zip

RUN wget https://bootstrap.pypa.io/get-pip.py
RUN python get-pip.py

# RUN pip install numpy

RUN cd ~/opencv-3.1.0/
RUN mkdir build
RUN cd build
RUN cmake -D CMAKE_BUILD_TYPE=RELEASE \
    -D CMAKE_INSTALL_PREFIX=/usr/local \
    -D INSTALL_PYTHON_EXAMPLES=ON \
    -D OPENCV_EXTRA_MODULES_PATH=~/opencv_contrib-3.1.0/modules \
    -D BUILD_EXAMPLES=ON ..
RUN make -j4
RUN make install
RUN ldconfig


# Build mjpg_streamer
# Need to run container with the device: docker run -t -i -p 8080:8080/tcp --device=/dev/video0 image:tag
RUN git clone https://github.com/jacksonliam/mjpg-streamer.git 


WORKDIR /mjpg-streamer/mjpg-streamer-experimental

RUN make && make install && chmod +x docker-start.sh

EXPOSE 8080/TCP

ENTRYPOINT ["/mjpg-streamer/mjpg-streamer-experimental/docker-start.sh", "output_http.so -w ./www"]

CMD ["input_raspicam.so"]

# ADD  run.sh run.sh
# CMD ./run.sh