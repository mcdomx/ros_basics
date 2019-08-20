#!/bin/sh

# START WEB SERVER

set -e

export LD_LIBRARY_PATH="/mjpg-streamer/mjpg-streamer-experimental"

./mjpg_streamer -o output_http.so -w ./www -i input_raspicam.so


