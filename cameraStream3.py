import subprocess
import picamera
import time


# uStream server info
# uStream keys
RTMP_URL="rtmp://1.21705518.fme.ustream.tv/ustreamVideo/21705518"
STREAM_KEY="fKb9NJUycD2unefr9JhukXybZBRSB3Wq"


# ffmpeg command line
cmdline =['ffmpeg', '-i' , '-', '-vcodec', 'copy', '-an', '-metadata', 'title=\"Streaming from raspberry pi camera\"', '-f', 'flv', RTMP_URL +'/' + STREAM_KEY]


# Setup up pipe to ffmpeg
stream = subprocess.Popen(cmdline, stdin=subprocess.PIPE)


camera = picamera.PiCamera()
try:
	camera.resolution = (640, 480)
	camera.framerate = 30
	camera.vflip = True
	camera.hflip = True
	print("Starting video streaming")
	camera.start_recording(stream.stdin, format='h264', quality = 30)
	print("waiting 30 seconds")
	try:
		while True:
			pass
	except KeyboardInterrupt:
		camera.stop_recording()
	#camera.wait_recording(30)
	print("30 seconds expired, stopping stream")
#	camera.stop_recording()
finally:
	camera.close()
	stream.stdin.close()
	stream.wait()


