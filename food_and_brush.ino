#include <Servo.h> 

int servoPin = 3; 

Servo Servo1; 

int servoPin2 = 2; 

Servo Servo2; 


unsigned long previousMillis = 0; // last time update
long interval = 5000; // interval at which to do something (milliseconds)
void setup() { 
   Servo1.attach(servoPin); 
   Servo2.attach(servoPin2); 
}
void loop(){ 
  int i = 5;
   
   unsigned long currentMillis = millis();

  if(currentMillis - previousMillis > interval) {
     previousMillis = currentMillis;  
     
     Servo1.write(0); 
     delay(1000); 
     // Make servo go to 90 degrees 
     Servo1.write(90); 
     delay(1000); 
     // Make servo go to 180 degrees 

     
     while (i >= 0) {
      i--;
      Servo2.write(0); 
      delay(1000); 
      // Make servo go to 90 degrees 
      Servo2.write(360); 
      delay(1000); 
      // Make servo go to 180 degrees 
     }
     
  }
   
   
   
}
