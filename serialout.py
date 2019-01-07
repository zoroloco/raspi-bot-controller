import serial
from serialbase import SerialBase
import sys


# serialOut thread - Thread that handles messages going to the Arduino.
class SerialOut(SerialBase):
    def __init__(self, thread_id, name, device, baud):
        super(SerialOut, self).__init__(thread_id, name, device, baud)

    # TX - received data from stdin to send down to the arduino.
    def send_data(self):
        while 1:
            try:
                cmd = (sys.stdin.readline()).encode('utf-8')
                self.arduino.write(cmd)
            except serial.SerialException:
                sys.stderr.write("Serial-Out exception while writing. Port probably closed.")
                return 1
            except serial.SerialTimeoutException:
                sys.stderr.write("Serial-Out timeout exception while writing.")
                return 1

    def run(self):
        if not self.arduino:
            return 1

        if self.send_data():
            return 1

        self.arduino.close()
