#!/usr/bin/env python3

import os
import sys
import subprocess
import picamera
import io

# uStream keys
RTMP_URL="rtmp://1.21705518.fme.ustream.tv/ustreamVideo/21705518"
STREAM_KEY="fKb9NJUycD2unefr9JhukXybZBRSB3Wq"

# ffmpeg command line
cmdline =['ffmpeg', '-i' ,'-', '-vcodec', 'copy', '-an', '-metadata', 'title=\"Streaming from raspberry pi camera\"', '-f', 'flv', RTMP_URL,'/', STREAM_KEY]
print ("--------------")
print (cmdline)
print ("--------------")

stream = io.BytesIO()


#player = subprocess.Popen(cmdline, stdout=subprocess.PIPE)


#sys.stdout = os.fdopen(sys.stdout.fileno(), 'wb', 0)

process = subprocess.Popen(cmdline ,stdin = subprocess.PIPE, shell = True)
while True:
	process.stdin.write(stream)

with picamera.PiCamera() as camera: 
	camera.resolution = (640, 480)
	camera.framerate = 30
	camera.vflip = True
	camera.hflip = True
	camera.start_recording(stream, format='h264')
	camera.wait_recording(10)
	camera.stop_recording()
	
#subprocess.Popen('pipe | cmdline',stdin = subprocess.PIPE, shell=False)	

#while True:
#	pass

#process.stdin.write('%d\n' % i)
		

	
