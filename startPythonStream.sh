#!/bin/bash

# This bash script calls a python script which outputs picamera
# output to stout, this script then pipes that through ffmpeg to 
# stream to uStream

RTMP_URL=rtmp://1.21705518.fme.ustream.tv/ustreamVideo/21705518
STREAM_KEY=fKb9NJUycD2unefr9JhukXybZBRSB3Wq

python3 cameraStreamBash.py | ffmpeg -i - -vcodec copy -an -metadata title="Streaming from raspberry pi camera" -f flv $RTMP_URL/$STREAM_KEY

