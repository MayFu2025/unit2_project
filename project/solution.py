import serial
import time
import datetime
import requests
from API import user, ip

id = "cu.usbserial-110"  #id of Arduino on computer
arduino = serial.Serial(port=f'/dev/{id}', baudrate=9600, timeout=0.1)  #id of Arduino on computer
print("Connection Successful")  #Let user know Arduino is connected


def read() -> str:
    """Read data from Arduino. Return data as a string."""
    data = ""
    while len(data) < 1:  # When data is empty
        data = arduino.readline()  # Read data collected on Arduino (sensors)
    return data.decode('utf-8')  # utf-8 is the same as ascii


humidity = []  # List to store humidity data
temperature = []  # List to store temperature data
t = 0  # Variable to store time elapsed in seconds
for i in range(172801):  # Loop for 17800 seconds (=48 hours)
    msg = read()  # Read data from Arduino
    print(t, msg)  # To check what data the program reads
    time.sleep(1)  # Wait 1 second
    t += 1  # Add 1 to the variable t corresponding to the seconds passed

    # Record the data once in 5 minutes
    if t%300 == 0:  # Per 5 minute interval (=300 seconds)
        # Storing Data in CSV File
        date = datetime.datetime.now()  # Find time data of the moment
        line = f'{t},{date},{msg}\n'  # Time in seconds, datetime, msg containing sensor readings
        with open('final_readings.csv', mode='a') as f:  # Open file in mode append
            data = f.writelines(line)  # Add line to CSV file

        # Storing Data in Sensors on Server
        a = list(msg.split(',')) # Split the msg (data from Arduino) into a list
        sensor_id = 29  # First of our sensors on the server
        r = 0  # Index of the list of readings
        # Login and Gain Access Token
        login = requests.post(f'http://{ip}/login', json=user)  # Login to server
        cookie = login.json()["access_token"]  # Get access token from server
        header = {'Authorization': f'Bearer {cookie}'}  # Create header for authorization
        # Create new posts for each sensor on the server
        while sensor_id <= 34:  # Loop through all of our sensors
            record = {f'sensor_id':sensor_id, 'value':a[r]}  # Create a record for each sensor
            print(record)  # To check what data the program sends to the server
            answer = requests.post(f'http://{ip}/reading/new', json=record, headers=header)  # Send data to server
            sensor_id += 1  # Next sensor
            r += 1  # Next reading

