# web server container
# FROM chunliu/docker-opencv
# FROM openhorizon/mjpg-streamer-pi3
FROM raspbian/jessie

# Install Dependencies and Utilities
RUN apt-get update
RUN dpkg --unpack man-db
RUN apt-get install -y \ 
    wget \
    build-essential \ 
    cmake \ 
    git \
    unzip \ 
    pkg-config \
    python-dev \ 
    python-opencv \ 
    libopencv-dev \ 
    libav-tools  \ 
    libjpeg-dev \ 
    libpng-dev \ 
    libtiff-dev \ 
    libjasper-dev \ 
    libgtk2.0-dev \ 
    python-numpy \ 
    python-pycurl \ 
    libatlas-base-dev \
    gfortran \
    webp \ 
    python-opencv \ 
    qt5-default \
    libvtk6-dev \ 
    zlib1g-dev 

# Install Additional Utilities
RUN apt-get install -y nano iputils-ping

RUN apt-get purge -y wolfram-engine	


# Install OpenCV
RUN wget -O opencv_contrib.zip https://github.com/Itseez/opencv_contrib/archive/3.1.0.zip
RUN unzip opencv_contrib.zip && rm opencv_contrib.zip
RUN cd ~/opencv-3.1.0/
RUN mkdir build
RUN cd build
RUN cmake -D CMAKE_BUILD_TYPE=RELEASE \
    -D CMAKE_INSTALL_PREFIX=/usr/local \
    -D INSTALL_PYTHON_EXAMPLES=ON \
    -D OPENCV_EXTRA_MODULES_PATH=~/opencv_contrib-3.1.0/modules \
    -D BUILD_EXAMPLES=ON ..
RUN make -j4 && make install && ldconfig

RUN mkdir /requirements
COPY requirements.txt /requirements
RUN pip install --no-cache-dir -r /requirements/requirements.txt

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