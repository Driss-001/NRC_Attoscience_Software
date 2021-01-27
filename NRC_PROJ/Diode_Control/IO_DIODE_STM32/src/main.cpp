#include <Arduino.h>

int8_t PD1 ;
int8_t PD2 ;
int8_t PD3 ;

void setup() {
  
  Serial.begin(115200);
 
  

  // put your setup code here, to run once:
}

void loop() {

  PD1 = random(0,10);
  PD2 = random(0,10);
  
  if (Serial.available()>0) {
    Serial.write(PD1);
    Serial.write(PD2);
  }
  // put your main code here, to run repeatedly:
}