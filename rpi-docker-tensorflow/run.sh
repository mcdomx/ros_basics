#!/bin/bash

echo "********************************************************"
echo "OBJECT COUNTING NODE"
echo "HOSTNAME: $(hostname)"
echo "********************************************************"


# Start main.py
python3 count_server.py

echo ">>>>>>>>>>>> counting server is running as: $(hostname)"
