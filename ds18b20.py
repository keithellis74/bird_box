#!/usr/bin/python3

ext_id = "28-041591f7d8ff"
int_id = "28-0015220d64ee"

def gettemp(id):
  try:
    mytemp = ''
    filename = 'w1_slave'
    f = open('/sys/bus/w1/devices/' + id + '/' + filename, 'r')
    line = f.readline() # read 1st line
    crc = line.rsplit(' ',1)
    crc = crc[1].replace('\n', '')
    if crc=='YES':
      line = f.readline() # read 2nd line
      mytemp = line.rsplit('t=',1)
    else:
      mytemp = 99999
    f.close()

    return (int(mytemp[1])/float(1000))

  except:
    return 99999

if __name__ == '__main__':

  # Script has been called directly
  id = ext_id
  print("Temp : " + '{:.1f}'.format(gettemp(id)/float(1000)))
