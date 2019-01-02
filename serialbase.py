# Base class for a serial connection

import threading
import sys
import serial


class SerialBase(threading.Thread):
    def __init__(self, thread_id, name, device, baud):
        threading.Thread.__init__(self)
        self.threadID = thread_id
        self.name = name
        self.arduino = super.connect_to_device(self.name, device, baud)

    def connect_to_device(self, thread_name, device, baud):
        try:
            self.arduino = serial.Serial(device, baud, timeout=0)
            if self.arduino:
                sys.stdout.write("{SERIALPY:CONNECTED-" + thread_name + "}")
                sys.stdout.flush()
            else:
                sys.stderr.write(thread_name + "Error with call to serial.Serial during connection.")
                return None
        except Exception as e:
            sys.stderr.write(thread_name + ": Error opening serial port.\n")
            print(e)

        return None
