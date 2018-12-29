const int S_pin = 2;
const int X_pin = A0;
const int Y_pin = A1;

void setup() {
pinMode(S_pin, INPUT_PULLUP);
Serial.begin(9600);
}

void loop() {
Serial.print("S Pin: ");
Serial.print(digitalRead(S_pin));
Serial.print("\n");
Serial.print("X-axis: ");
Serial.print(analogRead(X_pin));
Serial.print("\n");
Serial.print("Y-axis: ");
Serial.println(analogRead(Y_pin));
Serial.print("\n");
delay(200);
}