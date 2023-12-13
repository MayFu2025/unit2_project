import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from graph_lib import draw_graph, smoothing, basic_info, standardalization, take_data
import numpy as np
from datetime import datetime as dt
from matplotlib.dates import DateFormatter
import matplotlib.dates as mdates
from scipy.signal import savgol_filter
import sklearn.metrics as metrics

#get date from local
with open('final_readings.csv', mode='r') as f:
    data = f.readlines()
    date_list=[]
    temp1 = []
    humid1 = []
    temp2 = []
    humid2 = []
    temp3 = []
    humid3 = []
    t=0
    time=[]
    for line in data:
        rec = line.split(',')
        tdatetime = dt.strptime(rec[1][:16], '%Y-%m-%d %H:%M')
        date_list.append(tdatetime)
        temp1.append(float(rec[2]))
        temp2.append(float(rec[3]))
        temp3.append(float(rec[4]))
        humid1.append(float(rec[5]))
        humid2.append(float(rec[6]))
        humid3.append(float(rec[7]))
        time.append(t)
        t+=5

c = ["red", "blue", "green"] # color of the graph

#region # temp, humid graph 6box
fig = plt.figure(figsize=(30,20))
plt.subplot(2,3,1)
plt.ylim(0,60)
temp1_graph=draw_graph(t=date_list, v=temp1, color='red', title="temp1")
plt.xticks(rotation=45)
plt.gca().xaxis.set_major_locator(mdates.HourLocator(interval=10))


plt.subplot(2,3,2)
plt.ylim(0,60)
temp2_graph=draw_graph(t=date_list, v=temp2, color='blue', title="temp2")
plt.xticks(rotation=45)
plt.gca().xaxis.set_major_locator(mdates.HourLocator(interval=10))


plt.subplot(2,3,3)
plt.ylim(0,60)
temp3_graph=draw_graph(t=date_list, v=temp3, color='green', title="temp3")
plt.xticks(rotation=45)
plt.gca().xaxis.set_major_locator(mdates.HourLocator(interval=10))


plt.subplot(2,3,4)
plt.ylim(0,100)
humid1_graph=draw_graph(t=date_list, v=humid1, color='red', title="humid1")
plt.xticks(rotation=45)
plt.gca().xaxis.set_major_locator(mdates.HourLocator(interval=10))


plt.subplot(2,3,5)
plt.ylim(0,100)
humid2_graph=draw_graph(t=date_list, v=humid2, color='blue', title="humid2")
plt.xticks(rotation=45)
plt.gca().xaxis.set_major_locator(mdates.HourLocator(interval=10))

plt.subplot(2,3,6)
plt.ylim(0,100)
humid3_graph=draw_graph(t=date_list, v=humid3, color='green', title="humid3")
plt.xticks(rotation=45)
plt.gca().xaxis.set_major_locator(mdates.HourLocator(interval=10))

plt.show()
#endregion

