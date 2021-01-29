#include <Arduino.h>
#include "WiFi.h"


byte data[2] ; // array to store data

void setup() {
  
  Serial.begin(9600);
  // Set WiFi to station mode and disconnect from an AP if it was previously connected
  WiFi.mode(WIFI_STA);
  WiFi.disconnect();
  delay(100);

  Serial.println("Setup done");
 
  

  // put your setup code here, to run once:
}

void loop() {

  data[0] = random(0,50);
  data[1] = random(0,50);

  Serial.write(data,sizeof(data));
  delay(10);
  // put your main code here, to run repeatedly:
}