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

float joystickMaxPos = 1024;
float servoMaxSegments = 6000;
float servoOffset = 3000;

void setup() {
    pinMode(j1b, INPUT_PULLUP);
    pinMode(j2b, INPUT_PULLUP);
    pinMode(j3b, INPUT_PULLUP);
    Serial.begin(9600);
}

void loop() {
  //Serial.println(j1XLabel+mapPosition(analogRead(j1x)));//5958
  //Serial.println(j1YLabel+mapPosition(analogRead(j1y)));//6023-6029
  //Serial.println(j2XLabel+mapPosition(analogRead(j2x)));//5871
  //Serial.println(j2YLabel+mapPosition(analogRead(j2y)));//6052-6058
  //Serial.println(j3XLabel+mapPosition(analogRead(j3x)));//5970
  //Serial.println(j3YLabel+mapPosition(analogRead(j3y)));//5865

  //readJ1();
  readJ2();
  readJ3();
}

void readJ1(){
  int j1xCurrent = mapPosition(analogRead(j1x));
  if(j1xCurrent > 5965){
    Serial.println(j1XLabel+"1");
  }
  else if(j1xCurrent < 5952){
    Serial.println(j1XLabel+"0");
  }
  else{
    Serial.println(j1XLabel+"-1");
  }

  int j1yCurrent = mapPosition(analogRead(j1y));
  if(j1yCurrent >6035){
    Serial.println(j1YLabel+"1");  
  }
  else if(j1yCurrent < 6018){
    Serial.println(j1YLabel+"0");   
  }
  else{
    Serial.println(j1YLabel+"-1");
  }
}

void readJ2(){
  int j2yCurrent = mapPosition(analogRead(j2y));
  if(j2yCurrent > 6065){
    Serial.println(j2YLabel+"1");  
  }
  else if(j2yCurrent < 6045){
    Serial.println(j2YLabel+"0");  
  }
  else{
    Serial.println(j2YLabel+"-1");
  }
  
  int j2xCurrent = mapPosition(analogRead(j2x));
  if(j2xCurrent > 5880){
    Serial.println(j2XLabel+"1");
  }
  else if(j2xCurrent < 5860){
    Serial.println(j2XLabel+"0"); 
  }
  else{
    Serial.println(j2XLabel+"-1");
  }
}

void readJ3(){
    int j3xCurrent = mapPosition(analogRead(j3x));
  if(j3xCurrent > 5978){
    Serial.println(j3XLabel+"1");
  }
  else if(j3xCurrent < 5960){
    Serial.println(j3XLabel+"0");
  }
  else{
    Serial.println(j3XLabel+"-1");
  }
  
  int j3yCurrent = mapPosition(analogRead(j3y));
  if(j3yCurrent > 5875){
    Serial.println(j3YLabel+"1");
  }
  else if(j3yCurrent < 5855){
    Serial.println(j3YLabel+"0");
  }
  else{
    Serial.println(j3YLabel+"-1");
  }
}

//Joystick range is [0-1023]. This must map to servo range of [3000-9000]
int mapPosition(int pos){
  float f = pos / joystickMaxPos;
  return (servoMaxSegments * f) + servoOffset;
}
