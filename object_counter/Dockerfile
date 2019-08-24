# object counter

# 

FROM rpi-docker-tensorflow

#### Add ImageAI

RUN pip install --upgrade pip
RUN pip install -U tensorflow keras opencv-python-headless
RUN pip3 install imageai --upgrade

##### END ImageAI

RUN mkdir /pyfiles

COPY pyfiles/ /pyfiles/

ADD  run.sh run.sh
CMD ./run.sh