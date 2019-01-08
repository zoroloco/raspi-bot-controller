# raspi-bot-controller

This project is for the physical control of raspi-bot with joysticks.

1. Upload joystick.ino to your arduino. Be sure to change the pins to match the ones being used
   in your joysticks. This will send a HIGH=1 , LOW=2 or NEUTRAL = -1 depending on the position of
   the joystick axis. You should first plug in your joystick and see in the serial plotter where it
   hovers as a neutral. Give yourself a buffer of a few degrees to set your neutral position.
   
2. Python script will read the joystick position from the arduino and post it to a remote server.
