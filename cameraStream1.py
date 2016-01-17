#!/usr/bin/env python3

import os
import sys
import subprocess
import picamera

#--------------------------------------------------------- 
# Start capturing video

RTMP_URL="rtmp://1.21705518.fme.ustream.tv/ustreamVideo/21705518"
STREAM_KEY="fKb9NJUycD2unefr9JhukXybZBRSB3Wq"
cmdline =['ffmpeg', '-i' ,'-', '-vcodec', 'copy', '-an', '-metadata', 'title=\"Streaming from raspberry pi camera\"', '-f', 'flv', RTMP_URL,'/', STREAM_KEY]
print ("--------------")
print (cmdline)
print ("--------------")

#cmdline = ['vlc', '--demux', 'h264', '-']
    #cmdline = ['mplayer', '-fps', '25', '-cache', '1024', '-']
#player = subprocess.Popen(cmdline, stdout=subprocess.PIPE)
player = subprocess.Popen(cmdline)


#sys.stdout = os.fdopen(sys.stdout.fileno(), 'wb', 0)

with picamera.PiCamera() as camera: 
	camera.resolution = (640, 480)
	camera.framerate = 30
	camera.vflip = True
	camera.hflip = True
	camera.start_recording(player, format='h264')
	camera.wait_recording(10)
	camera.stop_recording()
	

	
