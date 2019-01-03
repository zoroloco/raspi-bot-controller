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

String j1XLabel = "1:";
String j1YLabel = "3:";
String j2XLabel = "5:";
String j2YLabel = "0:";
String j3XLabel = "4:";
String j3YLabel = "7:";

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
  Serial.println(j1XLabel+mapPosition(analogRead(j1x)));
  Serial.println(j1YLabel+mapPosition(analogRead(j1y)));
  Serial.println(j2YLabel+mapPosition(analogRead(j2x)));
  Serial.println(j2XLabel+mapPosition(analogRead(j2y)));
  Serial.println(j3XLabel+mapPosition(analogRead(j3x)));
  Serial.println(j3YLabel+mapPosition(analogRead(j3y)));
}

//Joystick range is [0-1023]. This must map to servo range of [3000-9000]
int mapPosition(int pos){
  float f = pos / joystickMaxPos;
  return (servoMaxPos * f) + servoOffset;
}
