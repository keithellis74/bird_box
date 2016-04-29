#!/usr/bin/python3
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
# Post data to thingspeak using thingspeak lib
# https://github.com/mchwalisz/thingspeak
# install sudo pip install thingspeak
#

from time import localtime, strftime
import time
import thingspeak
import ds18b20

channel_id = "88282"
write_key  = "xxxxxxxxxxxxxxxxxxxxxxx"
EXT_ID = "28-041591f7d8ff"
INT_ID = "28-0015220d64ee"
FREQUENCY = 5 * 60 # Record data at this frequency

def publish(channel):

	'''
	Get tempreatures
	'''
	ext_temp = ds18b20.gettemp(EXT_ID)
	int_temp = ds18b20.gettemp(INT_ID)

	try:
		response = channel.update({1:ext_temp, 2:int_temp})
		print ext_temp
		print int_temp
		print strftime("%a, %d %b %Y %H:%M:%S", localtime())
		print response
	except:
		print "connection failed"


#sleep for 16 seconds (api limit of 15 secs)
if __name__ == "__main__":

    channel = thingspeak.Channel(id=channel_id,write_key=write_key)
    while True:
        '''
        Send chanels to thingspeak
        '''

        publish(channel)
        time.sleep(FREQUENCY)
