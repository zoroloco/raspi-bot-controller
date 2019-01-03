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
const int j2b = 3;
const int j2x = A2;
const int j2y = A3;
const int j3b = 3;
const int j3x = A4;
const int j3y = A5;

String j1XLabel = "1:"; //HEAD PAN
String j1YLabel = "3:"; //HEAD TILT
String j2XLabel = "5:"; //BASE
String j2YLabel = "0:"; //ELBOW
String j3XLabel = "4:"; //SHOULDER
String j3YLabel = "7:"; //WRIST

int changeThreshold = 8;
int j1xLast = -1;
int j1yLast = -1;
int j2xLast = -1;
int j2yLast = -1;
int j3xLast = -1;
int j3yLast = -1;

float joystickMaxPos = 1024;
float servoMaxPos = 6000;
float servoOffset = 3000;

void setup() {
    pinMode(j1b, INPUT_PULLUP);
    pinMode(j2b, INPUT_PULLUP);
    pinMode(j3b, INPUT_PULLUP);
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

  int j2xCurrent = analogRead(j2x);
  if(abs(j2xLast-j2xCurrent) > changeThreshold){
      Serial.println(j2XLabel+mapPosition(j2xCurrent));
      j2xLast = j2xCurrent;
  }

  int j2yCurrent = analogRead(j2y);
  if(abs(j2yLast-j2yCurrent) > changeThreshold){
      Serial.println(j2YLabel+mapPosition(j2yCurrent));
      j2yLast = j2yCurrent;
  }

  int j3xCurrent = analogRead(j3x);
  if(abs(j3xLast-j3xCurrent) > changeThreshold){
      Serial.println(j3XLabel+mapPosition(j3xCurrent));
      j3xLast = j3xCurrent;
  }

  int j3yCurrent = analogRead(j3y);
  if(abs(j3yLast-j3yCurrent) > changeThreshold){
      Serial.println(j3YLabel+mapPosition(j3yCurrent));
      j3yLast = j3yCurrent;
  }
}

//Joystick range is [0-1023]. This must map to servo range of [3000-9000]
int mapPosition(int pos){
  float f = pos / joystickMaxPos;
  return (servoMaxPos * f) + servoOffset;
}
