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
import io


# uStream2 keys
RTMP_URL="rtmp://1.22079439.fme.ustream.tv/ustreamVideo/22079439"
STREAM_KEY="U8LmvKcPe3pCU5gbb5m2pexDXHCRBJDW"

# ffmpeg command line
cmdline =['ffmpeg', 
			'-i' , '-', 
			'-vcodec', 'copy', 
			'-an', 
			'-metadata', 'title=\"Ipswich IP1 bird box camera\"', 
			'-f', 'flv',
			 RTMP_URL +'/' + STREAM_KEY]

stream = subprocess.Popen(cmdline, stdin=subprocess.PIPE)

data = io.BytesIO()

with picamera.PiCamera() as camera:
	camera.resolution = (640, 480)
	camera.start_recording(data, format='h264', quality=23)
 
	while True:	
		data1 = data.read(1024)
		if not data1:
			break
		stream.stdin.write(data1) 


