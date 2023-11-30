import csv
import serial
import pyfirmata
import datetime
from pyfirmata import Arduino
import time

user = {"username": "MMproject", "password": "MMproject2"}
ip = "192.168.6.153"

id = "cu.usbserial-110"
arduino = serial.Serial(port=f'/dev/{id}', baudrate=9600, timeout=0.1)
print("Connection Successful")


s0 = arduino.digital[2]
s0 = pyfirmata.INPUT

s1 = arduino.digital[2]
s1 = pyfirmata.INPUT

s2 = arduino.digital[2]
s2 = pyfirmata.INPUT

for s in [0,1,2]:
    with open(f"sens_{s}.csv", mode='a') as s_data:
        # Creates the csv file for each sensor at first repeat
        writer = csv.writer()
        writer.writerow([datetime.date.today(), 0, "other"])


def read():
    data = ""
    while len(data) < 1:
        data = arduino.readline()
    return data.decode('utf-8')  #utf-8 is the same as ascii