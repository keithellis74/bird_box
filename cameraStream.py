#!/usr/bin/env python3

# ---------------------------------------------------------------------
# Basic implimentation of fully python implimentation of streaming
# Raspberry Pi camera to uStream using picamera piped to ffmpeg
# internally within this python script using subprocess.Popen
# ---------------------------------------------------------------------
# Added snap_shot()
# this takes a snapshot every 10 seconds


import subprocess
import picamera
import time


# uStream server info
# uStream keys
RTMP_URL="rtmp://1.21705518.fme.ustream.tv/ustreamVideo/21705518"
STREAM_KEY="fKb9NJUycD2unefr9JhukXybZBRSB3Wq"

count = 0  #counts how many stream loops have been completed
snapshot_frequency = 10  #frequency of snapshops in seconds

# ffmpeg command line
cmdline =['ffmpeg', '-i' , '-', '-vcodec', 'copy', '-an','-metadata', 'title=\"Ipswich IP1 bird box camera\"', '-f', 'flv', RTMP_URL +'/' + STREAM_KEY]

# Setup up pipe to ffmpeg
stream = subprocess.Popen(cmdline, stdin=subprocess.PIPE)

#Set up picamera
camera = picamera.PiCamera()

# Function to determine if camera is recording
# If recording return False, is not recording return True
def not_recording():
	if camera.recording:
		return False
	else:
		return True
		
#Function to start streaming for 30 minutes and then stop
def stream_now():
	print("About to start recording")
	camera.start_recording(stream.stdin, format='h264', bitrate = 500000)

#Function to take a snapshop image	
def snap_shot(name):
	camera.capture('images/'+ name +'.jpg', use_video_port=True)    


#Main code
try:
	camera.resolution = (960, 540)
	camera.framerate = 25
	camera.vflip = True
	camera.hflip = True
	
# Main loop if not streaming, start take snapstop and stream again
	start=time.time()
	last = start
	snap_shot_count = 0
	while True:
		if not_recording():
			count += 1 # Count number of times Stream has been restarted
			stream_now() # Start the stream
		if time.time() - last > snapshot_frequency:  # Take snap shot
			print("taking snap shot No.",snap_shot_count)
			snap_shot('image'+str(snap_shot_count))
			last = time.time()
			snap_shot_count += 1
			
except KeyboardInterrupt:
	camera.stop_recording()

finally:
	camera.close()
	stream.stdin.close()
	stream.wait()
	print("Camera safely shut down")
	print("Good bye")
	print("Stream Count =",count)
	print("Snap shot count =", snap_shot_count)
