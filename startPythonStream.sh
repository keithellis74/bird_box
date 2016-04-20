#!/bin/bash

# This bash script calls a python script which outputs picamera
# output to stout, this script then pipes that through ffmpeg to 
# stream to uStream


#Birdcam stream settings
RTMP_URL=rtmp://1.21705518.fme.ustream.tv/ustreamVideo/21705518
STREAM_KEY=fKb9NJUycD2unefr9JhukXybZBRSB3Wq

# Stream to Sensehat test stream
#RTMP_URL=rtmp://1.22079439.fme.ustream.tv/ustreamVideo/22079439
#STREAM_KEY=U8LmvKcPe3pCU5gbb5m2pexDXHCRBJDW

while :
do
	python3 cameraStreamBash1.py | ffmpeg -i - -vcodec copy -an -metadata title="Streaming from raspberry pi camera" -f flv $RTMP_URL/$STREAM_KEY
    sleep 2
done
