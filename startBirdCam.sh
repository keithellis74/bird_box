#!/bin/bash
# Copyright 2016 Keith Ellis
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
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
