#!/usr/bin/env python3

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
from time import sleep, time
from datetime import datetime

sys.stdout = os.fdopen(sys.stdout.fileno(), 'wb', 0)

snapshot_frequency = 60 * 60  #frequency of snapshops in seconds

max_images = 24 		# Maximum number of images to keep


def start_stream():
	start= time()
	last = start
	snap_shot_count = 0

	
#	print("Create camera object")
	camera = picamera.PiCamera()
	camera.roatation = 90
	camera.resolution = (960, 540)
	camera.framerate = 25
	camera.vflip = True
	camera.hflip = True
	camera.annotate_background = picamera.Color('black')

	
#	print("About to start recording")
	camera.start_recording(sys.stdout, bitrate = 500000, format='h264')
	
	while True:
		i = datetime.now()
		now = i.strftime('%d %b %Y - %H:%M:%S')
		camera.annotate_text = ' Bird Cam - ' + now + ' '
		
		try:
			camera.wait_recording(0.2)
		
		except picamera.exc.PiCameraError:
			camera.close()
			break			
			
		except BrokenPipeError:
			camera.close()
			break
			
		if time() - last > snapshot_frequency:  # Take snap shot
#			print("taking snap shot No.",snap_shot_count)
			snap_shot('image'+str(snap_shot_count), camera)
			last = time()
			if snap_shot_count >= max_images:
				snap_shot_count = 0
			else:
				snap_shot_count += 1
	
				
	
#Function to take a snapshop image	
def snap_shot(name, camera):
#	global camera
	camera.capture('images/'+ name +'.jpg', use_video_port=True)  	


start_stream()
