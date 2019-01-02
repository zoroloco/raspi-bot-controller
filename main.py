#!/usr/bin/python2

import sys
import getopt
from serialin import SerialIn
from serialout import SerialOut


# Start by reading the command line arguments.
try:
    opts, args = getopt.getopt(sys.argv[1:], 'd:b', ['device=', 'baud='])
except getopt.GetoptError:
    sys.stderr.write("Invalid commandline argument.\n")
    sys.exit(2)


for opt, arg in opts:
    if opt in ('--device', 'd'):
        device = arg
    if opt in ('--baud', 'b'):
        baud = arg

if not baud or not device:
    sys.stderr.write("Device and Baud rate are required.\n")
    sys.exit(2)

# Spawn two threads. One for reading data from Arduino and the other to write data to Arduino.
serialInThread = SerialIn(1, "SerialIn", device, baud)
if serialInThread:
    serialInThread.start()
else:
    sys.stderr.write("Error starting thread serialIn\n")

serialOutThread = SerialOut(2, "SerialOut", device, baud)
if serialOutThread:
    serialOutThread.start()
else:
    sys.stderr.write("Error starting thread serialOut\n")
