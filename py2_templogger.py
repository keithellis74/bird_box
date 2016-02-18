#!/usr/bin/python
import time
import os
import sys
import urllib            # URL functions
import urllib2           # URL functions

import ds18b20

################# Default Constants #################
# These can be changed if required
THINGSPEAKKEY = 'ABCDEFGH12345678'
THINGSPEAKURL = 'https://api.thingspeak.com/update'
EXT_ID = "28-041591f7d8ff"
INT_ID = "28-0015220d64ee"
#####################################################



def sendData(url,key,field1,field2,ext_temp,int_temp):
  """
  Send event to internet site
  """

  values = {'key' : key,'field1' : ext_temp, 'field2' : int_temp}

  postdata = urllib.urlencode(values)
  req = urllib2.Request(url, postdata)

  log = time.strftime("%d-%m-%Y,%H:%M:%S") + ","
  log = log + "{:.2f}C".format(ext_temp) + ","
  log = log + "{:.2f}C".format(int_temp) + ","

  try:
    # Send data to Thingspeak
    response = urllib2.urlopen(req, None, 5)
    html_string = response.read()
    response.close()
    log = log + 'Update ' + html_string

  except urllib2.HTTPError, e:
    log = log + 'Server could not fulfill the request. Error code: ' + str(e.code)
  except urllib2.URLError, e:
    log = log + 'Failed to reach server. Reason: ' + e.reason
  except:
    log = log + 'Unknown error'

  print log

def main():

	global THINGSPEAKKEY
	global THINGSPEAKURL
	global EXT_ID
	global INT_ID

	while True:
		ext_temperature=ds18b20.gettemp(EXT_ID)
		int_temperature=ds18b20.gettemp(INT_ID)
		print "internal temp =",int_temperature,"external temp =", ext_temperature
		sendData(THINGSPEAKURL,THINGSPEAKKEY,'field1','field2',ext_temperature,int_temperature)
		sys.stdout.flush()
		
		time.sleep(16)

 

if __name__=="__main__":
   main()
