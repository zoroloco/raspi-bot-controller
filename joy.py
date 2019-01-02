#!/usr/bin/python2

import sys
import threading
import getopt
import serial
import json
import urllib2
import requests
from sys import stdin

device = ''
baud = ''
remoteHost = 'http://192.168.1.237:7482'


# serialIn thread - Thread that handles data coming from the Arduino.
class serialIn (threading.Thread):
    def __init__(self, threadID, name,device,baud):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name     = name
        self.arduino  = connect(self.name,device,baud)
        postConnect()

    def run(self):
        if not self.arduino:
            return 1

        if receiveData(self.arduino):
            return 1

        self.arduino.close()


# serialOut thread - Thread that handles messages going to the Arduino.
class serialOut (threading.Thread):
    def __init__(self, threadID, name, device, baud):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.arduino = connect(self.name, device, baud)

    def run(self):
        if not self.arduino:
            return 1

        if sendData(self.arduino):
            return 1

        self.arduino.close()


# Connect
def connect(threadName,device,baud):
    try:
        arduino = serial.Serial(device, baud, timeout=0)
        if arduino:
            sys.stdout.write("{SERIALPY:CONNECTED-"+threadName+"}")
            sys.stdout.flush()
            return arduino
        else:
            sys.stderr.write(threadName+"Error with call to serial.Serial during connection.")
            return None
    except Exception as e:
        sys.stderr.write(threadName+": Error opening serial port.\n")
        print(e)

    return None


# TX - received data from stdin to send down to the arduino.
def sendData(arduino):
    while 1:
        try:
            cmd = (stdin.readline()).encode('utf-8')
            arduino.write(cmd)
        except serial.SerialException:
            sys.stderr.write("Serial exception while writing. Port probably closed.")
            return 1
        except serial.SerialTimeoutException:
            sys.stderr.write("Serial timeout exception while writing.")
            return 1


# RX - data received from the arduino.
# only post data every 800ms at most so http won't be flooded.
def receiveData(arduino):
    while 1:
      try:
        input = arduino.readline()
        if input is not None:
            postData(input)
            sys.stdout.write(input)
            sys.stdout.flush()
      except serial.SerialException:
        sys.stderr.write("Serial exception while reading. Port probably closed.")
        return 1


# POST to remote server
# Convert 1:3400 -> servo:1,pos:3400
def postData(cmd):
    if cmd is not None:
      cmd = cmd.replace('\r\n', '')
      splitStr = cmd.split(':')
      if splitStr is not None and len(splitStr) > 1:
        if splitStr[0].isdigit() and splitStr[1].isdigit():
          data = {'servo':splitStr[0],'pos':splitStr[1]}
          req = urllib2.Request(remoteHost+ '/move')
          req.add_header('Content-Type', 'application/json')
          urllib2.urlopen(req, json.dumps(data))


def postConnect():
    requests.get(url=remoteHost+ '/connect')


def postDisconnect():
    requests.get(url=remoteHost+ '/disconnect')


# Start
try:
    opts, args = getopt.getopt(sys.argv[1:], 'd:b', ['device=','baud='])
except getopt.GetoptError:
    sys.stderr.write("Invalid commandline argument.\n")
    sys.exit(2)

for opt, arg in opts:
    if opt in ('--device','d'):
        device = arg
    if opt in ('--baud','b'):
        baud = arg

if not baud or not device:
    sys.stderr.write("Device and Baud rate are required.\n")
    sys.exit(2)

# Start thread management
serialInThread = serialIn(1, "SerialIn", device,baud)
if serialInThread:
    serialInThread.start()
else:
    sys.stderr.write("Error starting thread serialIn\n")

serialOutThread= serialOut(2, "SerialOut", device,baud)
if serialOutThread:
    serialOutThread.start()
else:
    sys.stderr.write("Error starting thread serialOut\n")
