#!/usr/bin/python3
import time
import os
import sys
import urllib.request, urllib.parse, urllib.error           # URL functions
import http           # URL functions
import ds18b20


################# Default Constants #################
# These can be changed if required
THINGSPEAKKEY = 'LE6B6L2ZRZ592AA8'
THINGSPEAKURL = 'https://api.thingspeak.com:80'
EXT_ID = "28-041591f7d8ff"
INT_ID = "28-0015220d64ee"
#####################################################

def sendData(url,key, field1, field2, ext_temp, int_temp):
  """
  Send event to internet site
  """

  values = {'key' : key,'field1' : ext_temp, 'field2' : int_temp}

#  params = urllib.parse(values)
  headers = {"Content-type": "application/x-www-form-urlencoded","Accept":"text/plain"}
  conn = http.client.HTTPConnection(url)
  conn.request("POST", "/update",values, headers)
  response - conn.getresponse()
  print((response.status, response.reason))
  log = time.strftime("%d-%m-%Y,%H:%M:%S") + ","
  log = log + "{:.1f}C".format(ext_temp) + ","
  log = log + "{:.2f}mBar".format(int_temp) + ","

  try:
    # Send data to Thingspeak
    response = urllib.request.urlopen(req, None, 5)
    html_string = response.read()
    response.close()
    log = log + 'Update ' + html_string

  #except urllib2.HTTPError, e:
  #  log = log + 'Server could not fulfill the request. Error code: ' + e.code
  #except urllib2.URLError, e:
  #  log = log + 'Failed to reach server. Reason: ' + e.reason
  except:
    log = log + 'Unknown error'

  print(log)

def main():

	global THINGSPEAKKEY
	global THINGSPEAKURL
	global EXT_ID
	global INT_ID

 
	while True:
	  ext_temperature=ds18b20.gettemp(EXT_ID)
	  int_temperature=ds18b20.gettemp(INT_ID)
	  sendData(THINGSPEAKURL,THINGSPEAKKEY,'field1','field2',ext_temperature,int_temperature)
	  sys.stdout.flush()
	  time.sleep(60)

if __name__=="__main__":
   main()
