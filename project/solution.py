import serial
import time
import datetime
import requests
from API import user, ip

id = "cu.usbserial-110"  #id of Arduino on computer
arduino = serial.Serial(port=f'/dev/{id}', baudrate=9600, timeout=0.1)  #id of Arduino on computer
print("Connection Successful")  #Let user know Arduino is connected


def read():
    data = ""
    while len(data) < 1:  #When data is empty
        data = arduino.readline()  #Read data collected on Arduino (sensors)
    return data.decode('utf-8')  #utf-8 is the same as ascii


humidity = []
temperature = []
t = 0
for i in range(172801): #17800 seconds is 48 hours
    msg = read()
    print(t, msg)
    time.sleep(1)
    t += 1

    ## Record the data once in 5 minutes
    if t%300 == 0:
        ## Storing Data in CSV File every 5 minutes
        date = datetime.datetime.now()  #Find time data of the moment
        line = f'{t},{date},{msg}\n'  #Time in seconds, datetime, msg containing sensor readings
        with open('final_readings.csv', mode='a') as f:  #Open file in mode append
            data = f.writelines(line)  #Add line to CSV file


        ## Storing Data in Sensors on Server
        a = list(msg.split(','))
        sensor_id = 29
        r = 0
        # Login and Gain Access Token
        login = requests.post(f'http://{ip}/login', json=user)
        cookie = login.json()["access_token"]
        header = {'Authorization': f'Bearer {cookie}'}
        # Create new posts for each sensor on the server
        while sensor_id <= 34:
            record = {f'sensor_id':sensor_id, 'value':a[r]}
            print(record)  # To check what data the program sends to the server
            answer = requests.post(f'http://{ip}/reading/new', json=record, headers=header)
            sensor_id += 1
            r += 1

