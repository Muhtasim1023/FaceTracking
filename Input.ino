#include <Servo.h>

Servo servoX;
Servo servoY;

String serialData;
 
void setup() {
    Serial.begin(9600); 
    delay(1000);  
    servoX.attach(9);
    servoY.attach(10);
    Serial.setTimeout(10);
}
 
void loop() {
    
}

void serialEvent(){
  serialData = Serial.readString();
  servoX.write(parseDataX(serialData));
  servoY.write(parseDataY(serialData));
  
}

int parseDataX(String data){
  data.remove(data.indexOf("X"),1);
  return data.toInt();
}

int parseDataY(String data){
  data.remove(0, data.indexOf("Y") + 1);
  return data.toInt();
}
