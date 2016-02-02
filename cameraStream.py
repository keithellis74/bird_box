#!/usr/bin/env python3

# ---------------------------------------------------------------------
# Basic implimentation of fully python implimentation of streaming
# Raspberry Pi camera to uStream using picamera piped to ffmpeg
# internally within this python script using subprocess.Popen
# ---------------------------------------------------------------------

import subprocess
import picamera
import time


# uStream server info
# uStream keys
RTMP_URL="rtmp://1.21705518.fme.ustream.tv/ustreamVideo/21705518"
STREAM_KEY="fKb9NJUycD2unefr9JhukXybZBRSB3Wq"


# ffmpeg command line
cmdline =['ffmpeg', '-i' , '-', '-vcodec', 'copy', '-an', '-framerate', '25','-metadata', 'title=\"Ipswich IP1 bird box camera\"', '-f', 'flv', RTMP_URL +'/' + STREAM_KEY]

# Setup up pipe to ffmpeg
stream = subprocess.Popen(cmdline, stdin=subprocess.PIPE)

#Set up picamera
camera = picamera.PiCamera()

count = 0

# Function to determine if camera is recording
# If recording return False, is not recording return True
def not_recording():
	if camera.recording:
		return False
	else:
		print("re-starting recording")
		return True
		
#Function to start streaming for 30 minutes and then stop
def stream_now():
	print("About to start recording")
	camera.start_recording(stream.stdin, format='h264', bitrate = 500000)
	print("Record for 30 minutes")
	camera.wait_recording(1800)
	print("30 minutes expired, about to stop")
	camera.stop_recording()

#Main code
try:
	camera.resolution = (960, 540)
	camera.framerate = 25
	camera.vflip = True
	camera.hflip = True
#Main loop
# if not recording, start recording for 15 seconds
	while True:
		if not_recording():
			count += 1
			stream_now()

except KeyboardInterrupt:
		camera.stop_recording()

finally:
	camera.close()
	stream.stdin.close()
	stream.wait()
	print("Camera safely shut down")
	print("Good bye")
	print("Count = ",count)
