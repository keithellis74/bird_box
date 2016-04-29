#!/usr/bin/env python3
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

# This Python script sends picamera video output to stout,
# it is intended to be called from a bash script which pipes
# the output into ffmpeg
#
# Bash script is startPythonStream.sh

import os
import time
import picamera
import sys
from signal import pause

sys.stdout = os.fdopen(sys.stdout.fileno(), 'wb', 0)


#---------------------------------------------------------
# Start capturing video

with picamera.PiCamera() as camera:
	camera.resolution = (960, 540)
	camera.framerate = 25
	camera.vflip = True
	camera.hflip = True
	camera.start_recording(sys.stdout, bitrate = 500000, format='h264')
	pause()
