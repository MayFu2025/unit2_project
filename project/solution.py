import serial
import time
import datetime
import requests
from API import user, ip, cookie, header

id = "cu.usbserial-110"
arduino = serial.Serial(port=f'/dev/{id}', baudrate=9600, timeout=0.1)
print("Connection Successful")


def read():
    data = ""
    while len(data) < 1:
        data = arduino.readline()
    return data.decode('utf-8')  #utf-8 is the same as ascii


humidity = []
temperature = []
t = 0
for i in range(172801):
    msg = read()
    print(t, msg)
    time.sleep(1)
    t += 1

    # Storing Data in CSV File every 5 minutes
    if t%300 == 0:
        date = datetime.datetime.now()
        line = f'{t},{date},{msg}\n'
        with open('final_readings.csv', mode='a') as f:
            data = f.writelines(line)

        # Storing Data in Sensors on Server
        a = []
        sensor_id = 29
        r = 0
        for category in msg:
            for reading in category:
                a.append(reading)
        while sensor_id <= 34:
            record = {f'sensor_id':{sensor_id}, 'value':a[r]}
            answer = requests.post(f'http://{ip}/reading/new', json=record, headers=header)
            sensor_id += 1
            r += 1

