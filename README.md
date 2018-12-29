# raspi-bot-controller

A way to control raspi-bot with a raspberry pi 3 and some joystick controllers attached.

This program will spawn a child process which is a python script. The python script will listen
on the serial port for data coming from an arduino.  The arduino will have a joystick attached. When
the joystick moves, the position of the X or Y axis will be sent to the python script through the serial
port.  The python script will then pass this data to the node JS script via stdout.  The node script will
then send this data to the remote server, which can be found on my repository of raspi-bot.
