#!/usr/bin/env python3

# ---------------------------------------------------------------------
# Very basic implimentation of fully python implimentation of streaming
# Raspberry Pi camera to uStream using picamera piped to ffmpeg
# internally within this python script using subprocess.Popen
# ---------------------------------------------------------------------

import subprocess
import picamera
from time import sleep, time
from datetime import datetime
import errno

# uStream server info
# uStream keys
#RTMP_URL="rtmp://1.21705518.fme.ustream.tv/ustreamVideo/21705518"
#STREAM_KEY="fKb9NJUycD2unefr9JhukXybZBRSB3Wq"
# uStream2 keys
RTMP_URL="rtmp://1.22079439.fme.ustream.tv/ustreamVideo/22079439"
STREAM_KEY="U8LmvKcPe3pCU5gbb5m2pexDXHCRBJDW"

snapshot_frequency = 60 * 60  #frequency of snapshops in seconds

max_images = 24 		# Maximum number of images to keep

def stream_now(val):
	global stream
	global cmdline
	print("Camera has been closed", camera.closed)
	print("Camera is recording", camera.recording)
	if val == "restart":
		print("re-opening pipe")
		stream = subprocess.Popen(cmdline, stdin=subprocess.PIPE)
		sleep(1)
		print("About to start recording")
		camera.start_recording(stream.stdin, format='h264', bitrate = 500000)
	if val == "start":
		print("About to start recording")
		camera.start_recording(stream.stdin, format='h264', bitrate = 500000)
	
#Function to take a snapshop image	
def snap_shot(name):
	camera.capture('images/'+ name +'.jpg', use_video_port=True)  	

# ffmpeg command line
cmdline =['ffmpeg', 
			'-i' , '-', 
			'-vcodec', 'copy', 
			'-an', 
			'-metadata', 'title=\"Ipswich IP1 bird box camera\"', 
			'-f', 'flv',
			 RTMP_URL +'/' + STREAM_KEY]


# Setup up pipe to ffmpeg

print("Setup stream")
stream = subprocess.Popen(cmdline, stdin=subprocess.PIPE)
sleep(1)

start= time()
last = start
snap_shot_count = 0

#Set up picamera
with picamera.PiCamera() as camera:
	camera.resolution = (960, 540)
	camera.framerate = 25
	camera.vflip = True
	camera.hflip = True
	camera.annotate_background = picamera.Color('black')
	while True:
		try:
			if not camera.recording:
				stream_now("start")
			i = datetime.now()
			now = i.strftime('%d %b %Y - %H:%M:%S')
			camera.annotate_text = ' Bird Cam - ' + now + ' '
			camera.wait_recording(.2)
	
			if time() - last > snapshot_frequency:  # Take snap shot
				print("taking snap shot No.",snap_shot_count)
				snap_shot('image'+str(snap_shot_count))
				last = time()
				if snap_shot_count >= max_images:
					snap_shot_count = 0
				else:
					snap_shot_count += 1
	
		except IOError as e:
			if e.errno == errno.EPIPE or e.errno == errno.EINVAL:
				stream.kill()
				stream_now("restart")

#	except KeyboardInterrupt:
#		camera.stop_recording() 
	
#		finally:
#			stream.stdin.close()
#			stream.wait()
#			print("Camera safely shut down")
#			print("Good bye")
	
