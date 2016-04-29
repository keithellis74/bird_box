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
# Python script to turn on the IR LED

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
