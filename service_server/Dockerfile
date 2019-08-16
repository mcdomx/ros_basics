# service server image

# This is a will create a basic service server node

FROM rosbasic

# Copy container specific files and run
COPY service_server.py /catkin_ws/src/master_pkg/src/service_server.py

# ADD  run_service_server.sh run_service_server.sh
# CMD ./run_service_server.sh

RUN while ! (rosnode list | grep rosout); do echo "waiting..."; sleep 5 ; done
CMD rosrun master_pkg service_server.py