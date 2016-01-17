#!/bin/bash

RTMP_URL=rtmp://1.21705518.fme.ustream.tv/ustreamVideo/21705518
STREAM_KEY=fKb9NJUycD2unefr9JhukXybZBRSB3Wq

python3 cameraStream1.py | ffmpeg -i - -vcodec copy -an -metadata title="Streaming from raspberry pi camera" -f flv $RTMP_URL/$STREAM_KEY


#python3 cameraStream.py | ffmpeg -i - -vcodec copy -an -r 30 -f flv $RTMP_URL/$STREAM_KEY
