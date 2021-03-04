#include <Arduino.h>
#include "WiFi.h"
#define SIZE_OF_ARRAY 3
#define pin_1 36
#define pin_2 39

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

float volt_conv(int d){

  float v = 3.3*d/4095;
  return v;

}

void demo() {  //dummy data-set generator
  
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

void exp_1() { //real experiment code
  uint8_t d1 = analogRead(pin_1);
  uint8_t d2 = analogRead(pin_2);
  data[0] =  volt_conv(d1);
  data[1] =  volt_conv(d2);
  send_array(data);
  delay(1);
}


void loop() {

  Serial.flush();
  exp_1();
  
  // put your main code here, to run repeatedly:
}
