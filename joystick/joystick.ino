/*
ELBOW = 0;
HEAD_PAN = 1;  j1x
HEAD_TILT = 3; j1y
SHOULDER = 4;
BASE = 5;
HAND = 6;
WRIST = 7;
*/

const int j1b = 2; //button
const int j1x = A0; //x-axis
const int j1y = A1; //y-axis

const int j2 = 3;
const int j2x = A2;
const int j2y = A3;

const int j3 = 4;
const int j3x = A4;
const int j3y = A5;

String j1XLabel = "1:";
String j1YLabel = "3:";

int changeThreshold = 5;
int j1xLast = -1;
int j1yLast = -1;

float joystickMaxPos = 1024;
float servoMaxPos = 6000;
float servoOffset = 3000;

void setup() {
    pinMode(j1b, INPUT_PULLUP);
    Serial.begin(9600);
}

void loop() {
  int j1xCurrent = analogRead(j1x);
  if(abs(j1xLast-j1xCurrent) > changeThreshold){
      Serial.println(j1XLabel+mapPosition(j1xCurrent));
      j1xLast = j1xCurrent;
  }

  int j1yCurrent = analogRead(j1y);
  if(abs(j1yLast-j1yCurrent) > changeThreshold){
      Serial.println(j1YLabel+mapPosition(j1yCurrent));
      j1yLast = j1yCurrent;
  }
}

//Joystick range is [0-1023]. This must map to servo range of [3000-9000]
int mapPosition(int pos){
  float f = pos / joystickMaxPos;
  return (servoMaxPos * f) + servoOffset;
}
