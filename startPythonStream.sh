#!/bin/bash

# This bash script calls a python script which outputs picamera
# output to stout, this script then pipes that through ffmpeg to
# stream to uStream


#Birdcam stream settings
RTMP_URL=rtmp://xxxxxxxxxxxxxxxxxxxxxxx
STREAM_KEY=xxxxxxxxxxxxxxxxxxxxxxx

while :
do
	python3 cameraStreamBash1.py | ffmpeg -i - -vcodec copy -an -metadata title="Streaming from raspberry pi camera" -f flv $RTMP_URL/$STREAM_KEY
    sleep 2
done
