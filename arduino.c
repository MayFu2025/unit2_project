#include "DHT.h"


#define DHT1 13     // Digital pin connected to the DHT sensor
#define DHT2 13     // Digital pin connected to the DHT sensor
#define DHT3 13     // Digital pin connected to the DHT sensor

#define DHTTYPE DHT11   // DHT 22  (AM2302), AM2321

DHT dht(DHTPIN, DHTTYPE);
void setup() {
 pinMode(12, OUTPUT);//PIN 12 used as a 5V port
 digitalWrite(12,HIGH);
 Serial.begin(9600);
 Serial.println(F("Hello! Arduino has started"));
 dht.begin();
}
void loop() {
 delay(1000);
 float h1 = dht.readHumidity();
 float t1 = dht.readTemperature();
 // Check if any reads failed and exit early (to try again).
 if (isnan(h) || isnan(t)) {
   Serial.println(F("Failed to read from DHT sensor!"));
   return;
 }
 Serial.print(F("Humidity:"));
 Serial.print(h);
 Serial.print(F("% Temperature:"));
 Serial.print(t);
 Serial.println(F("C"));
}
