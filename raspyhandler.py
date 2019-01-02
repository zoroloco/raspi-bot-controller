# methods for handling data coming in from Arduino for this specific project.

import json
import urllib2
import requests
import sys
from joyaxis import JoyAxis

remoteHost = 'http://192.168.1.237:7482'


class RaspyHandler:
    def __init__(self):
        self.servos = {
            0: JoyAxis(),  # elbow
            1: JoyAxis(),  # head pan
            3: JoyAxis(),  # head tilt
            4: JoyAxis(),  # shoulder
            5: JoyAxis(),  # base
            6: JoyAxis(),  # hand
            7: JoyAxis()  # wrist
        }

    # Action after connection is made to the Arduino.
    def process_init(self):
        self.post_connect()

    # Action after data is received from the Arduino.
    # data = "1:3500"
    def process_input_data(self, data):
        cmd = data.replace('\r\n', '').split(':')
        if cmd is not None and len(cmd) > 1:
            servo = cmd[0]
            pos = cmd[1]
            if servo.isdigit() and pos.isdigit():
                if self.servos.get(servo).update_state(pos):  # only post the new position if state changed
                    self.post_data(servo, pos)
            else:
                sys.stderr.write("Servo and Position input need to be numbers.")

    # POST to remote server
    @staticmethod
    def post_data(servo, pos):
        data = {'servo': servo, 'pos': pos}
        req = urllib2.Request(remoteHost + '/move')
        req.add_header('Content-Type', 'application/json')
        urllib2.urlopen(req, json.dumps(data))

    @staticmethod
    def post_connect():
        requests.get(url=remoteHost + '/connect')

    @staticmethod
    def post_disconnect():
        requests.get(url=remoteHost + '/disconnect')