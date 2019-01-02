import serial
import sys
from serialbase import SerialBase
from raspyhandler import RaspyHandler as DataHandler


# serialIn thread - Thread that handles data coming from the Arduino.
class SerialIn(SerialBase):
    def __init__(self, thread_id, name, device, baud):
        super(SerialIn, self).__init__(thread_id, name, device, baud)
        self.datahandler = DataHandler()
        self.datahandler.process_init()

    # RX - data received from the arduino.
    def receive_data(self):
        while 1:
            try:
                data = self.arduino.readline()
                if data is not None:
                    self.datahandler.process_input_data(data)
                    sys.stdout.write(data)
                    sys.stdout.flush()
            except serial.SerialException:
                sys.stderr.write("Serial exception while reading. Port probably closed.")
                return 1

    def run(self):
        if not self.arduino:
            return 1

        if self.receive_data():
            return 1

        self.arduino.close()
