/* 
 *  
 *  Name: Margo Sikes
 *  
 *  Course: CSCI 1470
 *  
 *  Assignment: Project
 *  
 *  Set up variables for pin numbers and input values
 *  Set up the Serial port at 57600 baud rate
 *  Begin looping
 *     Read values from the three sensors
 *     Print the values to Serial data
 *     
  */


int leftPin = A3;
int rightPin = A4;
int xPin = A2;
int yPin = A1;
int zPin = A0;
int leftValue = 0;
int rightValue = 0;
int xValue = 0;
int yValue = 0;
int zValue = 0;

void setup() {
  Serial.begin(57600);
}

void loop() {
  delay(200);
  xValue = analogRead(xPin);
  yValue = analogRead(yPin);
  zValue = analogRead(zPin);
  leftValue = analogRead(leftPin);
  rightValue = analogRead(rightPin);

  Serial.print(xValue);
  Serial.print(" ");
  Serial.print(yValue);
  Serial.print(" ");
  Serial.print(zValue);
  Serial.print(" ");
  Serial.print(leftValue);
  Serial.print(" ");
  Serial.print(rightValue);
  Serial.print("\n");
}
