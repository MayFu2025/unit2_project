from graph_lib import take_data, draw_graph
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import numpy as np
import matplotlib.pyplot as plt
from graph_lib import take_data, standardalization

# with open('final_readings.csv', mode='r') as f:
#     data = f.readlines()
#     temp1 = []
#     humid1 = []
#     temp2 = []
#     humid2 = []
#     temp3 = []
#     humid3 = []
#     t=0
#     time=[]
#     for line in data:
#         rec = line.split(',')
#         temp1.append(float(rec[2]))
#         temp2.append(float(rec[3]))
#         temp3.append(float(rec[4]))
#         humid1.append(float(rec[5]))
#         humid2.append(float(rec[6]))
#         humid3.append(float(rec[7]))
#         time.append(t)
#         t+=5

time = take_data()
c = ["red", "blue", "green"]

# standardscaler graph
fig = plt.figure(figsize=(30,20))
plt.subplot(2,3,1)
sc_temp1 = standardalization(take_data[0])
plt.title = ("standardized temp1")
plt.plot(time, sc_temp1, color=c[0])

plt.subplot(2,3,2)
sc_temp2 = standardalization(take_data[1])
plt.title = ("standardized temp2")
plt.plot(time, sc_temp2, color=c[1])

plt.subplot(2,3,3)
sc_temp3 = standardalization(take_data[2])
plt.title = ("standardized temp3")
plt.plot(time, sc_temp3, color=c[2])

plt.subplot(2,3,4)
sc_humid1 = standardalization(take_data[3])
plt.title = ("standardized humid1")
plt.plot(time, sc_humid1, color=c[0])

plt.subplot(2,3,5)
sc_humid2 = standardalization(take_data[4])
plt.title = ("standardized humid2")
plt.plot(time, sc_humid2, color=c[1])

plt.subplot(2,3,6)
sc_humid3 = standardalization(take_data[5])
plt.title = ("standardized humid3")
plt.plot(time, sc_humid3, color=c[2])

plt.show()

