# This class will maintain state of an axis of a joystick. This pretty much represents one servo (x or y).

import datetime


class JoyAxis:
    user_move_time_threshold_ms = 1800  # 1.2 seconds of constant user movement.
    servo_min_pos = 3000
    servo_max_pos = 9000
    degree = 33.3  # 33.3 in the [3000-9000] range is = to 1 degree in the [0-180] range.
    move_precision = degree * 1  # This is how much to move per toggle.
    neutral_high = 6070  # The highest value we consider being in the neutral position.
    neutral_low = 5920  # The lowest value we consider being in the neutral position.

    def __init__(self, servo):
        self.servo = servo
        self.pos = -1  # The position of the servo.
        self.move_forward = False
        self.move_backward = False
        self.last_neutral_dt = datetime.datetime.now()
        self.single_toggle_done = False

    def update_state(self, cur_pos):
        cur_move_dt = datetime.datetime.now()
        move_diff_ms = int((cur_move_dt - self.last_neutral_dt).total_seconds()) * 1000

        if cur_pos is not None:

            in_neutral_zone = JoyAxis.neutral_low < cur_pos < JoyAxis.neutral_high

            if self.pos is -1:  # first time.
                self.pos = cur_pos

            if in_neutral_zone:
                self.move_backward = False
                self.move_forward = False
                self.last_neutral_dt = datetime.datetime.now()
                self.single_toggle_done = False

            if cur_pos > JoyAxis.neutral_high:  # if in forward position.
                if not self.move_backward and not in_neutral_zone:
                    self.move_forward = True
                    if not self.single_toggle_done or (move_diff_ms > JoyAxis.user_move_time_threshold_ms):
                        self.single_toggle_done = True
                        if self.pos < JoyAxis.servo_max_pos:  # max bounds check.
                            self.pos += JoyAxis.move_precision
                            print("Moved forward to:" + str(self.servo) + ":" + str(self.pos))
            elif cur_pos < JoyAxis.neutral_low:  # if in backward position.
                if not self.move_forward and not in_neutral_zone:
                    self.move_backward = True
                    if not self.single_toggle_done or (move_diff_ms > JoyAxis.user_move_time_threshold_ms):
                        self.single_toggle_done = True
                        if self.pos > JoyAxis.servo_min_pos:  # min bounds check.
                            self.pos -= JoyAxis.move_precision
                            print("Moved backward to:" + str(self.servo) + ":" + str(self.pos))

        return self.pos

