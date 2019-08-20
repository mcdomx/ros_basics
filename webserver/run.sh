#!/bin/sh

# START WEB SERVER

set -e

export LD_LIBRARY_PATH="/mjpg-streamer/mjpg-streamer-experimental"


# ./mjpg_streamer -i "input_raspicam.so" -o "output_http.so -w ./www"
./mjpg_streamer -o "$1" -i "$2"

