# This class will maintain state of an axis of a joystick. This pretty much represents one servo.
# Here we are pretty much ignoring the joystick positions when it is going back to the middle neutral position.
# We only care about user movement on the x or y axis.


class JoyAxis:
    def __init__(self):
        self.last_pos = -1
        self.move_forward = False
        self.move_backward = False

    # Return true if state updated. State not updated if direction changed without first originating at neutral.
    # The above logic is done to simulate a real joystick movement.
    def update_state(self, cur_pos):
        if self.last_pos == -1:
            self.last_pos = cur_pos

        pos_diff = cur_pos - self.last_pos
        in_neutral_zone = 5920 < cur_pos < 6070  # neutral zone is +- 50 due to any shaking.

        if in_neutral_zone:
            self.move_backward = False
            self.move_forward = False

        if pos_diff > 0:
            if not self.move_backward and not in_neutral_zone:
                self.move_forward = True
                self.last_pos = cur_pos
                print("Moved forward to:", cur_pos)
                return True
        elif pos_diff < 0:
            if not self.move_forward and not in_neutral_zone:
                self.move_backward = True
                self.last_pos = cur_pos
                print("Moved backward to:", cur_pos)
                return True

        return False
