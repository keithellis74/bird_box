#!/usr/bin/python3
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
write_key  = "LE6B6L2ZRZ592AA8"
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
