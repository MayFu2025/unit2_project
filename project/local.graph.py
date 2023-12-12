import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from graph_lib import draw_graph, smoothing, basic_info, standardalization, take_data
import numpy as np
from datetime import datetime as dt
from matplotlib.dates import DateFormatter
import matplotlib.dates as mdates
from scipy.signal import savgol_filter


# get data
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
        # print(tdatetime)
        # print(type(tdatetime))
        # date_list.append(str(tdatetime))
        date_list.append(tdatetime)
        temp1.append(float(rec[2]))
        temp2.append(float(rec[3]))
        temp3.append(float(rec[4]))
        humid1.append(float(rec[5]))
        humid2.append(float(rec[6]))
        humid3.append(float(rec[7]))
        time.append(t)
        t+=5


c = ["red", "blue", "green"]

#region # temp, humid graph 6box
# fig = plt.figure(figsize=(30,20))
# plt.subplot(2,3,1)
# plt.ylim(0,60)
# temp1_graph=draw_graph(t=time, v=temp1, color='red', title="temp1")
#
# plt.subplot(2,3,2)
# plt.ylim(0,60)
# temp2_graph=draw_graph(t=time, v=temp2, color='blue', title="temp2")
#
# plt.subplot(2,3,3)
# plt.ylim(0,60)
# temp3_graph=draw_graph(t=time, v=temp3, color='green', title="temp3")
#
# plt.subplot(2,3,4)
# plt.ylim(0,100)
# humid1_graph=draw_graph(t=time, v=humid1, color='red', title="humid1")
#
# plt.subplot(2,3,5)
# plt.ylim(0,100)
# humid2_graph=draw_graph(t=time, v=humid2, color='blue', title="humid2")
#
# plt.subplot(2,3,6)
# plt.ylim(0,100)
# humid3_graph=draw_graph(t=time, v=humid3, color='green', title="humid3")
# plt.show()
#endregion

#region # temp, humid 1 box
# fig = plt.figure(figsize=(40,20))
# plt.subplots_adjust(hspace=30)
# plt.subplot(2,1,1)
# plt.rcParams['figure.subplot.bottom'] = 1
# # plt.rcParams["font.size"] = 30
# plt.plot(time,temp1, label="temperature1", c='red')
# plt.plot(time,temp2, label="temperature2", c='blue')
# plt.plot(time,temp3, label="temperature3", c='green')
# ticks = time[::50]
# labels = [dt.strftime(date, '%m-%d %H:%M') for date in date_list[::50]]
# print(labels)
# plt.xticks(ticks, labels, fontsize=30, rotation=30, ha='right')
# plt.yticks(fontsize=30)
# plt.title("temperature",fontsize=50)
# plt.xlabel("time", fontsize=30)
# plt.ylabel("temperature", fontsize=30)
# plt.tight_layout()
# plt.legend(fontsize=30)
#
# plt.subplot(2,1,2)
# plt.rcParams['figure.subplot.bottom'] = 1
# plt.plot(time,humid1, label="humidty1", c='red')
# plt.plot(time,humid2, label="humidty2", c='blue')
# plt.plot(time,humid3, label="humidty3", c='green')
# ticks = time[::50]
# labels = [dt.strftime(date, '%m-%d %H:%M') for date in date_list[::50]]
# print(labels)
# plt.xticks(ticks, labels, fontsize=30, rotation=30, ha='right')
# plt.yticks(fontsize=30)
# plt.title("humidity", fontsize=50)
# plt.xlabel("time", fontsize=30)
# plt.ylabel("humidity", fontsize=30)
# plt.tight_layout()
# plt.legend(fontsize=30)
# plt.show()

#region #temp average
# plt.subplots_adjust(hspace=0.5)
# plt.subplot(2,1,1)
# temp_avg=basic_info(temp1,temp2,temp3)[0]
# plt.title("temperature average (n=576)")
# plt.plot(time, temp_avg)
#
# # average humidity
# plt.subplot(2,1,2)
# humid_avg=basic_info(humid1,humid2,humid3)[0]
# plt.title("humidity average (n=576)")
# plt.plot(time, humid_avg)
# plt.show()
#endregion

#region #standardscaler graph
# fig = plt.figure(figsize=(30,20))
# plt.subplot(2,3,1)
# time, sc_temp1 = standardalization(take_data()[0])
# plt.title = ("standardized temp1")
# plt.plot(time, sc_temp1, color=c[0])
#
# plt.subplot(2,3,2)
# time, sc_temp2 = standardalization(take_data()[1])
# plt.title = ("standardized temp2")
# plt.plot(time, sc_temp2, color=c[1])
#
# plt.subplot(2,3,3)
# time, sc_temp3 = standardalization(take_data()[2])
# plt.title = ("standardized temp3")
# plt.plot(time, sc_temp3, color=c[2])
#
# plt.subplot(2,3,4)
# time, sc_humid1 = standardalization(take_data()[3])
# plt.title = ("standardized humid1")
# plt.plot(time, sc_humid1, color=c[0])
#
# plt.subplot(2,3,5)
# time, sc_humid2 = standardalization(take_data()[4])
# plt.title = ("standardized humid2")
# plt.plot(time, sc_humid2, color=c[1])
#
# plt.subplot(2,3,6)
# time, sc_humid3 = standardalization(take_data()[5])
# plt.title = ("standardized humid3")
# plt.plot(time, sc_humid3, color=c[2])
#
# plt.show()
#endregion

#region # smoothing graph 6box
# fig = plt.figure(figsize=(30,20))
# plt.subplot(2,3,1)
# temp1_smoothing=draw_graph(smoothing(x=temp1, size_window=5)[0], smoothing(x=temp1, size_window=5)[1], color='red', title="smooth temp1")
#
# plt.subplot(2,3,2)
# temp2_smoothing=draw_graph(smoothing(x=temp2, size_window=5)[0], smoothing(x=temp2, size_window=5)[1], color='blue', title="smooth temp2")
#
# plt.subplot(2,3,3)
# temp3_smoothing=draw_graph(smoothing(x=temp3, size_window=5)[0], smoothing(x=temp3, size_window=5)[1], color='green', title="smooth temp3")
#
# plt.subplot(2,3,4)
# humid1_smoothing=draw_graph(smoothing(x=humid1, size_window=5)[0], smoothing(x=humid1, size_window=5)[1], color='red', title="smooth humid1")
#
# plt.subplot(2,3,5)
# humid2_smoothing=draw_graph(smoothing(x=humid2, size_window=5)[0], smoothing(x=humid2, size_window=5)[1], color='blue', title="smooth humid2")
#
# plt.subplot(2,3,6)
# humid3_smoothing=draw_graph(smoothing(x=humid3, size_window=5)[0], smoothing(x=humid3, size_window=5)[1], color='green', title="smooth humid2")
#
# plt.show()
#endregion 6box

#region smoothing 1box
# fig = plt.figure(figsize=(40,20))
# plt.subplot(2,1,1)
# plt.rcParams['figure.subplot.bottom'] = 1
#
# temp1_s = savgol_filter(temp1, 20, 2)
# temp2_s = savgol_filter(temp2, 20, 2)
# temp3_s = savgol_filter(temp3, 20, 2)
# plt.plot(time,temp1_s, label="temperature1", c='red')
# plt.plot(time,temp2_s, label="temperature2", c='blue')
# plt.plot(time,temp3_s, label="temperature3", c='green')
# ticks = time[::50]
# labels = [dt.strftime(date, '%m-%d %H:%M') for date in date_list[::50]]
#
# plt.xticks(ticks, labels, fontsize=30, rotation=30, ha='right')
# plt.yticks(fontsize=30)
# plt.title("temperature",fontsize=50)
# plt.xlabel("time", fontsize=30)
# plt.ylabel("temperature", fontsize=30)
# plt.tight_layout()
# plt.legend(fontsize=30)
#
# plt.subplot(2,1,2)
# plt.rcParams['figure.subplot.bottom'] = 1
# humid1_s = savgol_filter(humid1, 20, 2)
# humid2_s = savgol_filter(humid2, 20, 2)
# humid3_s = savgol_filter(humid3, 20, 2)
# plt.plot(time,humid1_s, label="humid1", c='red')
# plt.plot(time,humid2_s, label="humid2", c='blue')
# plt.plot(time,humid3_s, label="humid3", c='green')
# plt.xticks(ticks, labels, fontsize=30, rotation=30, ha='right')
# plt.yticks(fontsize=30)
# plt.title("humidity", fontsize=50)
# plt.xlabel("time", fontsize=30)
# plt.ylabel("humidity", fontsize=30)
# plt.tight_layout()
# plt.legend(fontsize=30)
# plt.show()
#endregion


#region # temperature error bar
# mean = basic_info(temp1, temp2, temp3)[0]
# std = basic_info(temp1, temp2, temp3)[1]
# min = basic_info(temp1, temp2, temp3)[2]
# max = basic_info(temp1, temp2, temp3)[3]
# median = basic_info(temp1, temp2, temp3)[4]
#
# fig = plt.figure(figsize=(40,10))
# plt.errorbar(time, mean, std, errorevery=(0,10),fmt='o',color="#023047")
# plt.fill_between(time, max, min, alpha=0.5, linewidth=0, color="#8ecae6")
# plt.xlabel("time", fontsize=40)
# plt.ylabel("average temperature", fontsize=40)
# plt.xticks(fontsize=30)
# plt.yticks(fontsize=30)
#
# # plt.legend()
# plt.show()
#endregion


#region # basic info graph of temp
# temp_info=basic_info(x=temp1, y=temp2, z=temp3)
#
# print(f"mean: {temp_info[0]}")
# print(f"std: {temp_info[1]}")
# print(f"min_val: {temp_info[2]}")
# print(f"max_val: {temp_info[3]}")
# print(f"avg: {temp_info[4]}")
#
# temp_info_graph = draw_graph(t=time, v=temp_info[4],color='black', title="temperature average")
# plt.show()

# basic info graph of humid
# humid_info=basic_info(x=humid1, y=humid2, z=humid3)
# humid_info_graph = draw_graph(t=time, v=humid_info[4],color='black', title="humidity average")
# plt.show()
#endregion

#region # prediction
plt.rcParams['figure.subplot.bottom'] = 0.40
fig = plt.figure (figsize=(40,20))
plt.subplots_adjust(hspace=1)
plt.subplot(2,1,1)
temp_coeffs = []
fitted_temp_arrays = []

for i in range(1, 4):
    temp_list_name = f"temp{i}"  # Create the variable name dynamically
    temp_list = globals()[temp_list_name]  # Access the variable using globals()

    coeffs = np.polyfit(time, temp_list, 4)
    temp_coeffs.append(coeffs)
    fitted_temp = np.polyval(coeffs, time)
    fitted_temp_arrays.append(fitted_temp)

    # Plot the original temperature data
    plt.plot(time, temp_list, label=f"temperature{i}", c=c[i - 1])

# Unpack the fitted temperature arrays
fitted_temp1, fitted_temp2, fitted_temp3 = fitted_temp_arrays
c_temp1, c_temp2, c_temp3 = temp_coeffs

# Plot the fitted temperature data
plt.plot(time, fitted_temp1, label=f"Predict temperature1 T(t) ={c_temp1[0]:.2f}t^4+{c_temp1[1]:.2f}t^3+{c_temp1[2]:.2f}^2+{c_temp1[3]:.2f}t+{c_temp1[4]:.2f}", linestyle='--', c=c[0])
plt.plot(time, fitted_temp2, label=f"Predict temperature2 T(t) ={c_temp2[0]:.2f}t^4+{c_temp2[1]:.2f}t^3+{c_temp2[2]:.2f}^2+{c_temp2[3]:.2f}t+{c_temp2[4]:.2f}", linestyle='--', c=c[1])
plt.plot(time, fitted_temp3, label=f"Predict temperature3 T(t) ={c_temp3[0]:.2f}t^4+{c_temp3[1]:.2f}t^3+{c_temp3[2]:.2f}^2+{c_temp3[3]:.2f}t+{c_temp3[4]:.2f}", linestyle='--', c=c[2])

# print(f"Quadratic model T(t) ={a:.2f}t^4+{b:.2f}t^3+{c:.2f}^2+{d:.2f}t+{e:.2f}")

ticks = time[::50]
labels = [dt.strftime(date, '%m-%d %H:%M') for date in date_list[::50]]
plt.xticks(ticks, labels, fontsize=20, rotation=45, ha='right')
plt.yticks(fontsize=20)
plt.title("temperature model", fontsize=50)
plt.legend(fontsize=10)

plt.subplot(2,1,2)
humid_coeffs = []
fitted_humid_arrays = []

for i in range(1, 4):
    humid_list_name = f"humid{i}"  # Create the variable name dynamically
    humid_list = globals()[humid_list_name]  # Access the variable using globals()

    coeffs = np.polyfit(time,  humid_list, 4)
    humid_coeffs.append(coeffs)
    fitted_humid = np.polyval(coeffs, time)
    fitted_humid_arrays.append(fitted_humid)

    # Plot the original temperature data
    plt.plot(time, humid_list, label=f"temperature{i}", c=c[i - 1])

# Unpack the fitted temperature arrays
fitted_humid1, fitted_humid2, fitted_humid3 = fitted_humid_arrays
c_humid1, c_humid2, c_humid3 = humid_coeffs

# Plot the fitted temperature data
plt.plot(time, fitted_humid1, label=f"Predict humid1 H(t) ={c_humid1[0]:.2f}t^4+{c_humid1[1]:.2f}t^3+{c_humid1[2]:.2f}^2+{c_humid1[3]:.2f}t+{c_humid1[4]:.2f}", linestyle='--', c=c[0])
plt.plot(time, fitted_humid2, label=f"Predict humid2 H(t) ={c_humid2[0]:.2f}t^4+{c_humid2[1]:.2f}t^3+{c_humid2[2]:.2f}^2+{c_humid2[3]:.2f}t+{c_humid2[4]:.2f}", linestyle='--', c=c[1])
plt.plot(time, fitted_humid3, label=f"Predict humid3 H(t) ={c_humid3[0]:.2f}t^4+{c_humid3[1]:.2f}t^3+{c_humid3[2]:.2f}^2+{c_humid3[3]:.2f}t+{c_humid3[4]:.2f}", linestyle='--', c=c[2])

# print(f"Quadratic model T(t) ={a:.2f}t^4+{b:.2f}t^3+{c:.2f}^2+{d:.2f}t+{e:.2f}")

ticks = time[::50]
labels = [dt.strftime(date, '%m-%d %H:%M') for date in date_list[::50]]
plt.xticks(ticks, labels, fontsize=20, rotation=45, ha='right')
plt.yticks(fontsize=20)
plt.title("humidity model", fontsize=50)
plt.legend(fontsize=10)

plt.show()

#endregion