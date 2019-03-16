#include <Servo.h> 

int servoPin = 3; 

Servo Servo1; 

unsigned long previousMillis = 0; // last time update
long interval = 3600000; // interval at which to do something (milliseconds)
void setup() { 
   Servo1.attach(servoPin); 
}
void loop(){ 
   
   unsigned long currentMillis = millis();

  if(currentMillis - previousMillis > interval) {
     previousMillis = currentMillis;  
     
     Servo1.write(0); 
     delay(1000); 
   
     Servo1.write(90); 
     delay(1000); 

     
  }
   
   
   
}
