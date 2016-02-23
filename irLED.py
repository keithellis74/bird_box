#!/usr/bin/python3

#Python script to turn on the IR LED

from gpiozero import PWMLED
from signal import pause
from optparse import OptionParser

DEFAULT_VALUE = 0.7

#add command line options

parser = OptionParser()

parser.add_option("-v", "--vaule", dest="value", help=" use -v ? to set value of irLED PWM, valid values are 0 through to 1" )


options, arguments = parser.parse_args()
if options.value:
	value = float(options.value)
	print("Using specified value =",options.value)
	
else:
	print("No value was given")
	value = DEFAULT_VALUE
	print("Using default value =",value)
ir = PWMLED(22)
ir.frequency = 25 # Set frequency stream frame rate
ir.value = value
pause()

