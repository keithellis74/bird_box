#!/usr/bin/env python3

# ---------------------------------------------------------------------
# Very basic implimentation of fully python implimentation of streaming
# Raspberry Pi camera to uStream using picamera piped to ffmpeg
# internally within this python script using subprocess.Popen
# ---------------------------------------------------------------------

import subprocess
import picamera

# uStream server info
# uStream keys
RTMP_URL="rtmp://1.21705518.fme.ustream.tv/ustreamVideo/21705518"
STREAM_KEY="fKb9NJUycD2unefr9JhukXybZBRSB3Wq"

# ffmpeg command line
cmdline =['ffmpeg', '-i' , '-', '-vcodec', 'copy', '-an', '-metadata', 'title=\"Ipswich IP1 bird box camera\"', '-f', 'flv', RTMP_URL +'/' + STREAM_KEY]

# Setup up pipe to ffmpeg
stream = subprocess.Popen(cmdline, stdin=subprocess.PIPE)

#Set up picamera
camera = picamera.PiCamera()
		
#Main loop
try:
	camera.resolution = (960, 540)
	camera.framerate = 25
	camera.vflip = True
	camera.hflip = True
	camera.start_recording(stream.stdin, format='h264', bitrate = 500000)
	while True:
		camera.wait_recording(60) 
	
except KeyboardInterrupt:
		camera.stop_recording()

finally:
	camera.close()
	stream.stdin.close()
	stream.wait()
	print("Camera safely shut down")
	print("Good bye")
