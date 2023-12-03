import csv
import matplotlib.pyplot as plt
import numpy as np

def get_records():
    time = []
    t1 = []
    t2 = []
    t3 = []
    h1 = []
    h2 = []
    h3 = []
    with open ('final_readings.csv', mode='r') as f:
        data = f.readlines()
        for line in data:
            rec = line.strip().split(',')
            time.append(rec[0])
            t1.append(rec[2])
            t2.append(rec[3])
            t3.append(rec[4])
            h1.append(rec[5])
            h2.append(rec[6])
            h3.append(rec[7])
    return time, t1, t2, t3, h1, h2, h3

time, t1, t2, t3, h1, h2, h3 = get_records()

fig = plt.figure(figsize=(8, 10))
plt.subplot(3,2,1)
plt.plot(time, t1, color='red', label='temp1')
plt.subplot(3,2,3)
plt.plot(time, t2, color='blue', label='temp2')
plt.subplot(3,2,5)
plt.plot(time, t3, color='green', label='temp3')
plt.subplot(3,2,2)
plt.plot(time, h1, color='red', label='hum1')
plt.subplot(3,2,4)
plt.plot(time, h2, color='blue', label='hum2')
plt.subplot(3,2,6)
plt.plot(time, h3, color='green', label='hum3')
plt.show()
