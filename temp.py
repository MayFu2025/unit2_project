import serial
import time
arduino = serial.Serial(port='/dev/cu.usbserial-10', baudrate=9600, timeout=.1)

def read():
    data = ""
    while len(data)<1:
        data = arduino.readline()
    return data

while True:
    time.sleep(0.1)
    value = read() #wait until data is in the port
    msg = value.decode('utf-8')
    print(msg)
