#!/bin/bash

# This bash script calls all required scripts and programmes
# to start birdcam at boot using systemD
# So far the following items are called/
#
# 1) Python bash script
# 2) Logging python script
# 3) Turn on IR LED


cd /home/kellis/repo/birdcam/
echo "Starting live stream"
screen -S birdbox -dms birdbox ./startPythonStream.sh
echo "Starting temperature logging"
python3 log_temp.py &
echo "All done"
sudo python3 irLED.py &
echo "turning on IR LED"
