#!/usr/bin/env python3

# ---------------------------------------------------------------------
# Very basic implimentation of fully python implimentation of streaming
# Raspberry Pi camera to uStream using picamera piped to ffmpeg
# internally within this python script using subprocess.Popen
# ---------------------------------------------------------------------

import subprocess
import picamera
from signal import pause
from time import sleep
from datetime import datetime

# uStream server info
# uStream keys
#RTMP_URL="rtmp://1.21705518.fme.ustream.tv/ustreamVideo/21705518"
#STREAM_KEY="fKb9NJUycD2unefr9JhukXybZBRSB3Wq"
# uStream2 keys
RTMP_URL="rtmp://1.22079439.fme.ustream.tv/ustreamVideo/22079439"
STREAM_KEY="U8LmvKcPe3pCU5gbb5m2pexDXHCRBJDW"



# ffmpeg command line
cmdline =['ffmpeg', 
			'-i' , '-', 
			'-vcodec', 'copy', 
			'-an', 
			#'-framerate', '25',
			#'-maxrate', '500000',
			#'-bufsize', '4000k',
			#'-g', '50',
			#'-timestamp', 'now',
			'-metadata', 'title=\"Ipswich IP1 bird box camera\"', 
			'-f', 'flv',
			 RTMP_URL +'/' + STREAM_KEY]

# Setup up pipe to ffmpeg
stream = subprocess.Popen(cmdline, stdin=subprocess.PIPE)

def stream_now():
	print("About to start recording")
	camera.start_recording(stream.stdin, format='h264', bitrate = 500000)


#Set up picamera
with picamera.PiCamera() as camera:
		
#Main loop
	try:
		camera.resolution = (960, 540)
		camera.framerate = 25
		camera.vflip = True
		camera.hflip = True
		camera.annotate_background = picamera.Color('black')
		while True:
			if not camera.recording:
				stream_now()
			i = datetime.now()
			now = i.strftime('%d %b %Y - %H:%M:%S')
			camera.annotate_text = ' Bird Cam - ' + now + ' '
			camera.wait_recording(1)
		#pause()
			
	except KeyboardInterrupt:
		camera.stop_recording() 
	
	finally:
		stream.stdin.close()
		stream.wait()
		print("Camera safely shut down")
		print("Good bye")
	
