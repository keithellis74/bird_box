#!/usr/bin/env python3

# This Python script sends picamera video output to stout,
# it is intended to be called from a bash script which pipes 
# the output into ffmpeg
#
# Bash script is startPythonStream.sh

import os
import time
import picamera

sys.stdout = os.fdopen(sys.stdout.fileno(), 'wb', 0)

    
#--------------------------------------------------------- 
# Start capturing video

with picamera.PiCamera() as camera: 
	camera.resolution = (640, 480)
	camera.framerate = 30
	camera.start_recording(sys.stdout, format='h264')
	camera.wait_recording(60)
	camera.stop_recording()
