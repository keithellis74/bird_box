#!/bin/bash
# Copyright 2016 Keith Ellis
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
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
