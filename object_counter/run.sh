#!/bin/bash

echo "********************************************************"
echo "OBJECT COUNTING NODE"
echo "HOSTNAME: $(hostname)"
echo "********************************************************"


# Start
python3 /pyfiles/count_server.py

echo ">>>>>>>>>>>> counting server is running as: $(hostname)"
