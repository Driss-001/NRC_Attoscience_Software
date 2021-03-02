#include <Arduino.h>
#include "WiFi.h"
#define SIZE_OF_ARRAY 3

float data[SIZE_OF_ARRAY] ; // array to store data

byte *p = (byte*)data;

char buff[10];

void setup() {
  
  Serial.begin(600000);
  // Set WiFi to station mode and disconnect from an AP if it was previously connected
  WiFi.mode(WIFI_STA);
  WiFi.disconnect();
  delay(100);

  //Serial.println("Setup done");
 
  

  // put your setup code here, to run once:
}


void send_array(float msg[]) {
  

  for (int i=0;i<SIZE_OF_ARRAY;i++){
    //snprintf (buff, sizeof(buff), "%f", data[i]);
    Serial.print(msg[i]);
    if(i!=SIZE_OF_ARRAY-1){
      Serial.print(';');
      }
    }
  Serial.print('\n');
}


void demo() {
  
  uint8_t d = random(0,99);
  float d1 = float(d)/float(100);
  d = random(0,99);
  float d2 = float(d)/float(100);
  d = random(0,99);
  float d3 = float(d)/float(100);
  data[0] = float(random(0,3))+d1;
  data[1] = float(random(0,3))+d2;
  data[2] = float(random(0,3))+d3;
  
  send_array(data);
  
  delay(1);

}



void loop() {
  //dummy data-set generator
  Serial.flush();
  demo();
  
  // put your main code here, to run repeatedly:
}
