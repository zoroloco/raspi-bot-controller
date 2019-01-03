# methods for handling data coming in from Arduino for this specific project.

import json
import urllib2
import requests
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
                if self.servos.get(int(servo)).update_state(int(pos)):  # only post the new position if state changed
                    self.post_data(servo, pos)

    # POST to remote server
    @staticmethod
    def post_data(servo, pos):
        try:
            data = {'servo': servo, 'pos': pos}
            req = urllib2.Request(remoteHost + '/move')
            req.add_header('Content-Type', 'application/json')
            urllib2.urlopen(req, json.dumps(data))
        except BaseException as e:
            print("Error sending post data to remote host:", e)

    @staticmethod
    def post_connect():
        try:
            requests.get(url=remoteHost + '/connect')
        except BaseException as e:
            print("Error sending connect to remote host:", e)

    @staticmethod
    def post_disconnect():
        try:
            requests.get(url=remoteHost + '/disconnect')
        except BaseException as e:
            print("Error sending disconnect to remote host:", e)
