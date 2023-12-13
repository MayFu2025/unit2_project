#include "DHT.h"
#define DHTTYPE DHT11   // DHT 22  (AM2302), AM2321

#define DHTPIN1 13     // what pin we're connected to
#define DHTPIN2 5 
#define DHTPIN3 2 

DHT dht1(DHTPIN1, DHTTYPE);
DHT dht2(DHTPIN2, DHTTYPE);
DHT dht3(DHTPIN3, DHTTYPE);

void setup() {
 pinMode(12, OUTPUT);//PIN 12 used as a 5V port
 digitalWrite(12,HIGH);
 pinMode(3, OUTPUT);//PIN 12 used as a 5V port
 digitalWrite(3,HIGH);
 Serial.begin(9600);
 Serial.println(F("Hello! Arduino has started"));
 dht1.begin();
 dht2.begin();
 dht3.begin();
}

void loop() {
  delay(1000);
  // Readings for DHT1
  float h1 = dht1.readHumidity();
  float t1 = dht1.readTemperature();
  float h2 = dht2.readHumidity();
  float t2 = dht2.readTemperature();
  float h3 = dht3.readHumidity();
  float t3 = dht3.readTemperature();

  //Check for errors
  if (isnan(h1) || isnan(t1) || isnan(h2) || isnan(t2) || isnan(h3) || isnan(t3)) {
   Serial.println(F("Failed to read from DHT sensor!"));
   if (isnan(h1) || isnan(t1)) {
    Serial.println(F("Failed to read from sensor 1"));
   }
   if (isnan(h2) || isnan(t2)) {
    Serial.println(F("Failed to read from sensor 2"));
   }
  if (isnan(h3) || isnan(t3)) {
    Serial.println(F("Failed to read from sensor 3"));
   }
  return;
  }

  // Print and check the readings for DHT1
  Serial.print(t1);
  Serial.print(",");
  Serial.print(t2);
  Serial.print(",");
  Serial.print(t3);
  Serial.print(",");
  Serial.print(h1);
  Serial.print(",");
  Serial.print(h2);
  Serial.print(",");
  Serial.print(h3);
}