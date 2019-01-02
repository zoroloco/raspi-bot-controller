# This class will maintain state of an axis of a joystick. This pretty much represents one servo.
# Here we are pretty much ignoring the joystick positions when it is going back to the middle neutral position.
# We only care about user movement on the x or y axis.


class JoyAxis:
    def __init__(self):
        self.last_pos = -1
        self.move_forward = False
        self.move_backward = False
        self.neutral_reset = False

    # Return true if state updated. State not updated if direction changed without first originating at neutral.
    # The above logic is done to simulate a real joystick movement.
    def update_state(self, cur_pos):
        if self.last_pos == -1:
            self.last_pos = cur_pos

        if 5950 < cur_pos < 6050:  # neutral position +- 50 due to any shaking.
            self.neutral_reset = True
        else:
            self.neutral_reset = False

        if(cur_pos - self.last_pos > 0) and (self.move_forward or self.neutral_reset):
            self.move_forward = True
            self.move_backward = False
            self.neutral_reset = False
            self.last_pos = cur_pos
            return True
        elif(cur_pos - self.last_pos < 0) and (self.move_backward or self.neutral_reset):
            self.move_backward = True
            self.move_forward = False
            self.neutral_reset = False
            self.last_pos = cur_pos
            return True

        return False
