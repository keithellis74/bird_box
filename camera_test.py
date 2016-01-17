#!/usr/bin/end python3
import time
import picamera
import io
import subprocess
import socket

#UStream keys
RTMP_URL="rtmp://1.21705518.fme.ustream.tv/ustreamVideo/21705518"
STREAM_KEY="fKb9NJUycD2unefr9JhukXybZBRSB3Wq"

#camera = picamera.PiCamera()

#stream = io.BytesIO()
#with picamera.PiCamera() as camera:
#    camera.resolution = (640, 480)
#    camera.start_recording(stream, format='h264', quality=23)
#    camera.wait_recording(15)
#    camera.stop_recording()

#subprocess.call("ffmpeg -i %s- -vcodec copy -an -metadata title="Streaming from #raspberry pi camera" -f flv %s / %s", $("stream", "RTMP_URL", "STREAM_KEY"))

client_socket = socket.socket()
client_socket.connect(('my_server', 8000))

connection = client_socket.makefile('wb')
try:
	with picamer.Picamera() as camera:
		camera.resolution = (640, 480)
		camera.framerate = 24
		# Start a preview and let camera warm up for 2 seconds
		camera.start_preview()
		time.sleep(2)
		# Start recording, sending the output to the connection
		camera.start_recording(connection, format='h264')
		camera.wait_recording(60)
		camera.stop_recording()
finally:
	connection.close()
	client_socket.close()
