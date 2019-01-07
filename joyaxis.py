# This class will maintain state of an axis of a joystick. This pretty much represents one servo (x or y).

import datetime


class JoyAxis:
    move_time_threshold_ms = 200  # Threshold of time in ms to act upon since last move.
    servo_min_pos = 3000
    servo_max_pos = 9000
    HIGH = 1
    LOW = 0
    degree = 33.3  # 33.3 in the [3000-9000] range is = to 1 degree in the [0-180] range.
    move_precision = degree * 1  # This is how much to move per toggle.

    def __init__(self, servo):
        self.servo = servo
        self.pos = -1  # The position of the servo.
        self.last_move_dt = datetime.datetime.now()

    #  cur_pos = 0 for LOW or 1 for HIGH
    def update_state(self, cur_pos):
        cur_move_dt = datetime.datetime.now()
        if cur_pos is not None:

            if self.pos == -1:
                self.pos = 6000  # Reset to center at first.

            move_diff_ms = int((cur_move_dt - self.last_move_dt).total_seconds()) * 1000

            if move_diff_ms > JoyAxis.move_time_threshold_ms:
                if cur_pos == JoyAxis.HIGH and self.pos < JoyAxis.servo_max_pos:
                    self.pos += JoyAxis.move_precision
                    self.last_move_dt = datetime.datetime.now()
                    print("Moved forward to:" + str(self.servo) + ":" + str(self.pos))
                elif cur_pos == JoyAxis.LOW and self.pos > JoyAxis.servo_min_pos:
                    self.pos -= JoyAxis.move_precision
                    self.last_move_dt = datetime.datetime.now()
                    print("Moved backward to:" + str(self.servo) + ":" + str(self.pos))

        return self.pos
