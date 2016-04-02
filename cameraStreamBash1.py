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
import thingspeak

sys.stdout = os.fdopen(sys.stdout.fileno(), 'wb', 0)

snapshot_frequency = 60 * 60  #frequency of snapshops in seconds
temp_frequency = 5 * 60  #frequency of temperature updates
max_images = 24 		# Maximum number of images to keep

#ThingSpeak keys
channel_id = "88282"
write_key  = "LE6B6L2ZRZ592AA8"
channel = thingspeak.Channel(id=channel_id,write_key=write_key)


def get_temp(sensor):
	if sensor == 'internal':
		field_id = 2
	else:
		field_id = 1
	return channel.get_field_last_text(field=field_id)


def start_stream():
	start= time()
	last = start
	snap_shot_count = 0
	ext_temp = get_temp('external')

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
		
		if time()- last > temp_frequency:
			ext_temp = get_temp('external')

		i = datetime.now()
		now = i.strftime('%d %b %Y - %H:%M:%S')
		camera.annotate_text = ' Bird Cam - ' + now + ' ' + ' Ext temp = ' + ext_temp
		
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
