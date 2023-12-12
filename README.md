![11e470e9022f4fc5b367429bcbb285bc](https://github.com/comsci-uwc-isak/unit2_2023/assets/53995212/1d14b1d3-ae39-4ef3-8ec9-3329630eacae)

# Unit 2: A Distributed Weather Station for ISAK

## Criteria A: Planning

## Problem definition
As winter arrives, the residents of Room 20C of the house R4-Up have reported waking up to sore throats and cold-like symptoms in the mornings. They suspect that the main reason for this is either the temperature or humidity of the room, but they still believe that there is a possibility for other factors to be at play as well. If they can be sure the reason for their suffering is the temperature, the residents can collectively decide to turn up the heater in their room. Similarly, if they can be sure that the humidity is to blame, together they will invest in a humidifier (or dehumidifier) for their room.

Room 20C is asking for a way to record the temperature and humidity of the room, to be able to look back and review if they can conclude that one or both are contributing to their sufferings in the morning.

## Proposed Solution
Considering the client requirements an adequate solution includes a low cost sensing device for humidity and temperature and a custom data script that process and anaysis the samples acquired. For a low cost sensing device an adequate alternative is the DHT11 sensor[^1] which is offered online for less than 5 USD and provides adequare precision and range for the client requirements (Temperature Range: 0°C to 50°C, Humidity Range: 20% to 90%). Similar devices such as the DHT22, AHT20 or the AM2301B [^2] have higher specifications, however the DHT11 uses a simple serial communication (SPI) rather than more eleborated protocols such as the I2C used by the alternatives. For the range, precision and accuracy required in this applicaiton the DHT11 provides the best compromise. Connecting the DHT11 sensor to a computer requires a device that provides a Serial Port communication. A cheap and often used alternative for prototyping is the Arduino UNO microcontroller [^3]. "Arduino is an open-source electronics platform based on easy-to-use hardware and software"[^4]. In additon to the low cost of the Arduino (< 6USD), this devide is programable and expandable[^1]. Other alternatives include diffeerent versions of the original Arduino but their size and price make them a less adequate solution.

Considering the budgetary constrains of the client and the hardware requirements, the software tool that I proposed for this solution is Python. Python's open-source nature and platform independence contribute to the long-term viability of the system. The use of Python simplifies potential future enhancements or modifications, allowing for seamless scalability without the need for extensive redevelopment [^5][^6]. In comparison to the alternative C or C++, which share similar features, Python is a High level programming language (HLL) with high abstraction [^7]. For example, memory management is automatic in Python whereas it is responsability of the C/C++ developer to allocate and free up memory [^7], this could result in faster applications but also memory problems. In addition a HLL language will allow me and future developers extend the solution or solve issues proptly.  

**Design statement**
Using an arduino and DHT 11 sensors, we will construct a system that can measure the temperature and humidity of 3 different locations inside room 20C, where our client wishes to check. To do this, we will use Python in the IDE Pycharm, as well as a variation of C++ in the Arduino IDE [^8]. We will also create visualizations of the data that was collected using the pyplot module from the matplotlib library in Python, on Pycharm.

[^1]: Industries, Adafruit. “DHT11 Basic Temperature-Humidity Sensor + Extras.” Adafruit Industries Blog RSS, https://www.adafruit.com/product/386. 
[^2]: Nelson, Carter. “Modern Replacements for DHT11 and dht22 Sensors.” Adafruit Learning System, https://learn.adafruit.com/modern-replacements-for-dht11-dht22-sensors/what-are-better-alternatives.   
[^3]:“How to Connect dht11 Sensor with Arduino Uno.” Arduino Project Hub, https://create.arduino.cc/projecthub/pibots555/how-to-connect-dht11-sensor-with-arduino-uno-f4d239.  
[^4]:Team, The Arduino. “What Is Arduino?: Arduino Documentation.” Arduino Documentation | Arduino Documentation, https://docs.arduino.cc/learn/starting-guide/whats-arduino.  
[^5]:Tino. “Tino/PyFirmata: Python Interface for the Firmata (Http://Firmata.org/) Protocol. It Is Compliant with Firmata 2.1. Any Help with Updating to 2.2 Is Welcome. the Capability Query Is Implemented, but the Pin State Query Feature Not Yet.” GitHub, https://github.com/tino/pyFirmata. 
[^6]:Python Geeks. “Advantages of Python: Disadvantages of Python.” Python Geeks, 26 June 2021, https://pythongeeks.org/advantages-disadvantages-of-python/. 
[^7]: Real Python. “Python vs C++: Selecting the Right Tool for the Job.” Real Python, Real Python, 19 June 2021, https://realpython.com/python-vs-cpp/#memory-management. 
[^8]: Emeritus. "What are the Key Pros and Cons of the Arduino Programming Language?" Emeritus, Emeritus, 25 January 2023, https://emeritus.org/blog/coding-arduino-programming-language.

## Success Criteria
1. The solution provides a visual representation of the Humidity and Temperature values inside a dormitory (Local) and outside the house (Remote) for a period of minimum 48 hours. 
1. ```[HL]``` The local variables will be measure using a set of 3 sensors around the dormitory.
2. The solution provides a mathematical modelling for the Humidity and Temperature levels for each Local and Remote locations. ```(SL: linear model)```, ```(HL: non-lineal model)```
3. The solution provides a comparative analysis for the Humidity and Temperature levels for each Local and Remote locations including mean, standad deviation, minimum, maximum, and median.
4. ```(SL)```The Local samples are stored in a csv file and ```(HL)``` posted to the remote server as a backup.
5. The solution provides a prediction for the subsequent 12 hours for both temperature and humidity.
6. The solution includes a poster summarizing the visual representations, model and analysis created. The poster includes a recommendation about healthy levels for Temperature and Humidity.

_TOK Connection: To what extent does ```the use of data science``` in climate research influence our understanding of environmental issues, and what knowledge questions arise regarding the ```reliability, interpretation, and ethical implications``` of data-driven approaches in addressing climate change_

1. How does our use of technology shape our understanding of the environment
2. What responsibilities do we have as technologists when it comes to handling personal data related to our living spaces?
3. What cultural and contextual factors might impact our interpretation of the results, especially when comparing our local readings with those from the campus? 

# Criteria B: Design

## System Diagram **HL**
![HL](https://github.com/comsci-uwc-isak/unit2_2023/assets/53995212/4891d5e9-b8ab-46ed-bd75-b606e25e3383)

**Fig.2** shows the system diagram for the proposed solution (**HL**). The indoor variables will be measured using an Arduino and three DHT11 sensors located inside a room. Three sensors are used to determine more precisely the physical values and include measurement uncertainty. The outdoor variables will be requested to the remote server using a GET request to the API of the server at ```192.168.6.153/readings```. The local values are stored in a CSV database locally and a backup copy will be store in the remote server using the **Weather API**. 


## Record of Tasks
| Task No | Planned Action                                     | Planned Outcome                                                                                                        | Time estimate | Target completion date | Criterion |
|---------|----------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|---------------|------------------------|-----------|
| 1       | Write the Problem context                          |                                                                                                                        | 10min         | Nov 22                 | A         |
| 2       |                                                    |                                                                                                                        |               |                        | A         |
| 3       | Code and Upload Program for Arduino on Arduino IDE | Create and upload program for data collection onto the arduino                                                         | 30min         | Nov 29                 |           |
| 4       | Construct Arduino Circuit for Data Collection      | Have sensors connected to the Arduino, ready to connect to the computer and start collecting data                      | 1hr           | Nov 29                 |           |
| 5       | Code Data Collection Method on PyCharm             | Create a program that retrieves data from the Arduino, stores it in a csv file, and uploads it onto server on PyCharm. | 1hr           | Nov 29                 |           |
| 6       | Test and Finalize Hardware and Software            | Fix any bugs or add additional functions as neccesary before starting final data collection                            | 3hr           | Nov 30                 |           |
| 7       | Collect Temperature and Humidity Data for 48 Hours | Collect data per 5 minutes over the course of 48 hours from 3 different sensors                                        | 48hr          | Nov 30 ~ Dec 3         |           |
| 8       | Construct Graphs Using Pyplot                      | Have graphs for raw data and average using pyplot                                                                      | 1hr           | Dec 4                  |           |
## Test Plan

# Criteria C: Development
```.jupyter
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
```

```.python


```


## List of techniques used

## Development


# Criteria D: Functionality

A 7 min video demonstrating the proposed solution with narration
