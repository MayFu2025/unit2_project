import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from graph_lib import draw_graph, smoothing, basic_info, standardalization, take_data
import numpy as np
from datetime import datetime as dt
from datetime import timedelta
import matplotlib.dates as mdates
from scipy.signal import savgol_filter
import sklearn.metrics as metrics
from matplotlib.ticker import MaxNLocator

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
        date_list.append(tdatetime)
        temp1.append(float(rec[2]))
        temp2.append(float(rec[3]))
        temp3.append(float(rec[4]))
        humid1.append(float(rec[5]))
        humid2.append(float(rec[6]))
        humid3.append(float(rec[7]))
        time.append(t)
        t+=5


#region #get remote data
with open('remote_readings.csv', mode='r') as f:
    data = f.readlines()
    r_temp1 = []
    r_temp2 = []
    r_temp3 = []
    r_humid1 = []
    r_humid2 = []
    r_humid3 = []
    r_humid1_fake = []
    r_time =[]
    t = 0
    r_time_list = []

    for line in data:
        rec = line.split(',')
        tdatetime = dt.strptime(rec[0][:16], '%Y-%m-%d %H:%M')
        r_temp1.append(float(rec[1]))
        r_temp2.append(float(rec[2]))
        r_temp3.append(float(rec[3]))
        r_humid1.append(float(rec[4]))
        r_humid2.append(float(rec[5]))
        r_humid3.append(float(rec[6]))
        r_humid1_fake.append(float(rec[7]))
        r_time.append(tdatetime)
        r_time_list.append(t)
        t += 5

#endregion

c = ["red", "blue", "green"]

#region # remote temp, humid graph 6box
locator = MaxNLocator(nbins=7)

fig = plt.figure(figsize=(30,20))
plt.subplots_adjust(hspace=0.5)

plt.subplot(2,3,1) # temp1
plt.ylim(0,60)
temp1_graph=draw_graph(t=r_time, v=r_temp1, color='red', title="remote temperature1")
plt.xlabel("time", fontsize=20)
plt.ylabel("temperature (C)", fontsize=20)
plt.gca().xaxis.set_major_locator(locator)
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m-%d %H:%M'))


plt.subplot(2,3,2) # temp2
plt.ylim(0,60)
temp2_graph=draw_graph(t=r_time, v=r_temp2, color='blue', title="remote temperature2")
plt.xlabel("time", fontsize=20)
plt.ylabel("temperature (C)", fontsize=20)
plt.gca().xaxis.set_major_locator(locator)
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m-%d %H:%M'))


plt.subplot(2,3,3) # temp3
plt.ylim(0,60)
temp3_graph=draw_graph(t=r_time, v=r_temp3, color='green', title="remote temperature3")
plt.xlabel("time", fontsize=20)
plt.ylabel("temperature (C)", fontsize=20)
plt.gca().xaxis.set_major_locator(locator)


plt.subplot(2,3,4) # humid1
plt.ylim(0,100)
humid1_graph=draw_graph(t=r_time, v=r_humid1, color='red', title="remote humid1")
plt.xlabel("time", fontsize=20)
plt.ylabel("humidity (%)", fontsize=20)
plt.gca().xaxis.set_major_locator(locator)
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m-%d %H:%M'))


plt.subplot(2,3,5) #humid2
plt.ylim(0,100)
humid2_graph=draw_graph(t=r_time, v=r_humid2, color='blue', title="remote humid2")
plt.xlabel("time", fontsize=20)
plt.ylabel("humidity (%)", fontsize=20)
plt.gca().xaxis.set_major_locator(locator)
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m-%d %H:%M'))

plt.subplot(2,3,6) #humid3
plt.ylim(0,100)
humid3_graph=draw_graph(t=r_time, v=r_humid3, color='green', title="remote humid3")
plt.xlabel("time", fontsize=20)
plt.ylabel("humidity (%)", fontsize=20)
plt.gca().xaxis.set_major_locator(locator)
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m-%d %H:%M'))


plt.show()
#endregion

#region # humid graph 6box
fig = plt.figure(figsize=(30,20))
plt.subplots_adjust(hspace=0.5)

plt.subplot(2,3,1) # temp1
plt.ylim(0,60)
temp1_graph=draw_graph(t=date_list, v=temp1, color='red', title="local temp1")
plt.xlabel("time", fontsize=20)
plt.ylabel("temperature (C)", fontsize=20)
plt.gca().xaxis.set_major_locator(mdates.HourLocator(interval=10))

plt.subplot(2,3,2) # temp2
plt.ylim(0,60)
temp2_graph=draw_graph(t=date_list, v=temp2, color='blue', title="local temp2")
plt.xlabel("time", fontsize=20)
plt.ylabel("temperature (C)", fontsize=20)
plt.gca().xaxis.set_major_locator(mdates.HourLocator(interval=10))

plt.subplot(2,3,3) # temp3
plt.ylim(0,60)
temp3_graph=draw_graph(t=date_list, v=temp3, color='green', title="local temp3")
plt.xlabel("time", fontsize=20)
plt.ylabel("temperature (C)", fontsize=20)
plt.gca().xaxis.set_major_locator(mdates.HourLocator(interval=10))

plt.subplot(2,3,4) # humid1
plt.ylim(0,100)
humid1_graph=draw_graph(t=date_list, v=humid1, color='red', title="local humid1")
plt.xlabel("time", fontsize=20)
plt.ylabel("humidity (%)", fontsize=20)
plt.gca().xaxis.set_major_locator(mdates.HourLocator(interval=10))

plt.subplot(2,3,5) #humid2
plt.ylim(0,100)
humid2_graph=draw_graph(t=date_list, v=humid2, color='blue', title="local humid2")
plt.xlabel("time", fontsize=20)
plt.ylabel("humidity (%)", fontsize=20)
plt.gca().xaxis.set_major_locator(mdates.HourLocator(interval=10))

plt.subplot(2,3,6) #humid3
plt.ylim(0,100)
humid3_graph=draw_graph(t=date_list, v=humid3, color='green', title="local humid3")
plt.xlabel("time", fontsize=20)
plt.ylabel("humidity (%)", fontsize=20)
plt.gca().xaxis.set_major_locator(mdates.HourLocator(interval=10))

plt.show()
#endregion

#region #temp, humid both local remote average
fig = plt.figure(figsize=(40,20))
plt.subplots_adjust(hspace=1, bottom=0.5)
plt.subplot(2,1,1)

l_temp_avg=basic_info(temp1,temp2,temp3)[0]
r_temp_avg=basic_info(r_temp1,r_temp2,r_temp3)[0]

plt.plot(date_list,l_temp_avg, label="local temperature", c='red', lw=5)
plt.plot(r_time,r_temp_avg, label="remote temperature", c='pink', lw=5)

plt.gca().xaxis.set_major_locator(mdates.HourLocator(interval=5))
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m-%d %H:%M'))
plt.xticks(fontsize=30, rotation=30, ha='right')
plt.yticks(fontsize=30)
plt.title("temperature average",fontsize=50)
plt.xlabel("time", fontsize=30)
plt.ylabel("temperature (C)", fontsize=30)
plt.tight_layout()
plt.legend(fontsize=30, loc="upper right")

plt.subplot(2,1,2)
plt.rcParams['figure.subplot.bottom'] = 1

l_humid_avg=basic_info(humid1,humid2,humid3)[0]
r_humid_avg=basic_info(r_humid1_fake,r_humid2,r_humid3)[0]

plt.plot(date_list,l_humid_avg, label="local temperature", c='red', lw=5)
plt.plot(r_time,r_humid_avg, label="remote temperature", c='pink', lw=5)

plt.gca().xaxis.set_major_locator(mdates.HourLocator(interval=5))
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m-%d %H:%M'))
plt.xticks(fontsize=30, rotation=30, ha='right')
plt.yticks(fontsize=30)
plt.title("humidity average", fontsize=50)
plt.xlabel("time", fontsize=30)
plt.ylabel("humidity (%)", fontsize=30)
plt.tight_layout()
plt.legend(fontsize=30)
plt.show()
#endregion

#region #standardscaler graph
fig = plt.figure(figsize=(30,20))
plt.subplot(2,3,1)
time, sc_temp1 = standardalization(take_data()[0])
plt.plot(date_list, sc_temp1, color=c[0])
plt.title("standardized temp1", fontsize=20)
plt.xlabel("time", fontsize=20)
plt.ylabel("temperature (C)", fontsize=20)
plt.xticks(rotation=30)
plt.gca().xaxis.set_major_locator(mdates.HourLocator(interval=10))

plt.subplot(2,3,2)
time, sc_temp2 = standardalization(take_data()[1])
plt.title("standardized temp2", fontsize=20)
plt.plot(date_list, sc_temp2, color=c[1])
plt.xlabel("time", fontsize=20)
plt.ylabel("temperature (C)", fontsize=20)
plt.xticks(rotation=30)
plt.gca().xaxis.set_major_locator(mdates.HourLocator(interval=10))

plt.subplot(2,3,3)
time, sc_temp3 = standardalization(take_data()[2])
plt.title("standardized temp3", fontsize=20)
plt.plot(date_list, sc_temp3, color=c[2])
plt.xlabel("time", fontsize=20)
plt.ylabel("temperature (C)", fontsize=20)
plt.xticks(rotation=30)
plt.gca().xaxis.set_major_locator(mdates.HourLocator(interval=10))

plt.subplot(2,3,4)
time, sc_humid1 = standardalization(take_data()[3])
plt.title("standardized humid1", fontsize=20)
plt.plot(date_list, sc_humid1, color=c[0])
plt.xlabel("time", fontsize=20)
plt.ylabel("humidity (%)", fontsize=20)
plt.xticks(rotation=30)
plt.gca().xaxis.set_major_locator(mdates.HourLocator(interval=10))

plt.subplot(2,3,5)
time, sc_humid2 = standardalization(take_data()[4])
plt.title("standardized humid2", fontsize=20)
plt.plot(date_list, sc_humid2, color=c[1])
plt.xlabel("time", fontsize=20)
plt.ylabel("humidity (%)", fontsize=20)
plt.xticks(rotation=30)
plt.gca().xaxis.set_major_locator(mdates.HourLocator(interval=10))

plt.subplot(2,3,6)
time, sc_humid3 = standardalization(take_data()[5])
plt.title("standardized humid3", fontsize=20)
plt.plot(date_list, sc_humid3, color=c[2])
plt.xlabel("time", fontsize=20)
plt.ylabel("humidity (%)", fontsize=20)
plt.xticks(rotation=30)
plt.gca().xaxis.set_major_locator(mdates.HourLocator(interval=10))

plt.show()
#endregion

#region #smoothing 1box
fig = plt.figure(figsize=(40,20))
plt.subplot(2,1,1)

temp1_s = savgol_filter(temp1, 20, 2)
temp2_s = savgol_filter(temp2, 20, 2)
temp3_s = savgol_filter(temp3, 20, 2)
plt.plot(date_list,temp1_s, label="temperature1", c='red', lw=5)
plt.plot(date_list,temp2_s, label="temperature2", c='blue', lw=5)
plt.plot(date_list,temp3_s, label="temperature3", c='green', lw=5)

# ticks = time[::50]
# labels = [dt.strftime(date, '%m-%d %H:%M') for date in date_list[::50]]
# plt.xticks(ticks, labels, fontsize=30, rotation=30, ha='right')

plt.gca().xaxis.set_major_locator(mdates.HourLocator(interval=5))
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m-%d %H:%M'))
plt.xticks(fontsize=30, rotation=30, ha='right')
plt.yticks(fontsize=30)
plt.title("savgol_filter smoothing temperature (windowsize=20)",fontsize=50)
plt.xlabel("time", fontsize=30)
plt.ylabel("temperature (C)", fontsize=30)
plt.tight_layout()
plt.legend(fontsize=30, loc="upper right")

plt.subplot(2,1,2)
plt.rcParams['figure.subplot.bottom'] = 1
humid1_s = savgol_filter(humid1, 20, 2)
humid2_s = savgol_filter(humid2, 20, 2)
humid3_s = savgol_filter(humid3, 20, 2)
plt.plot(date_list,humid1_s, label="humid1", c='red', lw=5)
plt.plot(date_list,humid2_s, label="humid2", c='blue', lw=5)
plt.plot(date_list,humid3_s, label="humid3", c='green', lw=5)

plt.gca().xaxis.set_major_locator(mdates.HourLocator(interval=5))
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m-%d %H:%M'))
plt.xticks(fontsize=30, rotation=30, ha='right')

plt.yticks(fontsize=30)
plt.title("savgol_filter smoothing humidity (windowsize=20)", fontsize=50)
plt.xlabel("time", fontsize=30)
plt.ylabel("humidity (%)", fontsize=30)
plt.tight_layout()
plt.legend(fontsize=30, loc ="upper right")
plt.show()
#endregion

#region # temperature error bar
mean = basic_info(temp1, temp2, temp3)[0]
std = basic_info(temp1, temp2, temp3)[1]
min = basic_info(temp1, temp2, temp3)[2]
max = basic_info(temp1, temp2, temp3)[3]
median = basic_info(temp1, temp2, temp3)[4]

fig = plt.figure(figsize=(40,10))
plt.plot(date_list, median,'o', markersize=8)
plt.errorbar(date_list, mean, std, errorevery=(0,10),color="#023047")
plt.fill_between(date_list, max, min, alpha=0.5, linewidth=0, color="#8ecae6")

plt.gca().xaxis.set_major_locator(mdates.HourLocator(interval=5))
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m-%d %H:%M'))
plt.xticks(fontsize=30, rotation=30, ha='right')
plt.yticks(fontsize=30)

plt.xlabel("time", fontsize=30)
plt.ylabel("average temperature (C)", fontsize=30)
plt.title("local temperature error bar (n=576)", fontsize=50)
plt.tight_layout()
plt.show()
#endregion

#region # remote temperature error bar
mean = basic_info(r_temp1, r_temp2, r_temp3)[0]
std = basic_info(r_temp1, r_temp2, r_temp3)[1]
min = basic_info(r_temp1, r_temp2, r_temp3)[2]
max = basic_info(r_temp1, r_temp2, r_temp3)[3]
median = basic_info(r_temp1, r_temp2, r_temp3)[4]

fig = plt.figure(figsize=(40,10))
plt.plot(r_time, median,'o', markersize=8)
plt.errorbar(r_time, mean, std, errorevery=(0,10),color="#023047")
plt.fill_between(r_time, max, min, alpha=0.5, linewidth=0, color="#8ecae6")

plt.gca().xaxis.set_major_locator(mdates.HourLocator(interval=5))
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m-%d %H:%M'))
plt.xticks(fontsize=30, rotation=30, ha='right')
plt.yticks(fontsize=30)

plt.xlabel("time", fontsize=30)
plt.ylabel("average temperature (C)", fontsize=30)
plt.title("remote temperature error bar (n=632)", fontsize=50)
plt.tight_layout()
plt.show()
#endregion

#region # humidity error bar
basic_info_list=[]
for i in range(5):
    info = basic_info(humid1, humid2, humid3)[i]
    basic_info_list.append(info)

mean, std, min, max, median = basic_info_list

fig = plt.figure(figsize=(40,10))
plt.plot(date_list, mean, c='black')
plt.plot(date_list, median,'o', markersize=8)
plt.errorbar(date_list, mean, std, errorevery=(0,10),color="#023047")
plt.fill_between(date_list, max, min, alpha=0.5, linewidth=0, color="#8ecae6")

plt.gca().xaxis.set_major_locator(mdates.HourLocator(interval=5))
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m-%d %H:%M'))
plt.xticks(fontsize=30, rotation=30, ha='right')
plt.yticks(fontsize=30)

plt.xlabel("time", fontsize=30)
plt.ylabel("average humidity (%)", fontsize=30)
plt.title("local humidity error bar (n=576)", fontsize=50)
plt.tight_layout()
plt.show()
#endregion

#region # remote humidity error bar
basic_info_list=[]
for i in range(5):
    info = basic_info(r_humid1_fake, r_humid2, r_humid3)[i]
    basic_info_list.append(info)

mean, std, min, max, median = basic_info_list

fig = plt.figure(figsize=(40,10))
plt.plot(r_time, mean, c='black')
plt.plot(r_time, median,'o', markersize=8)
plt.errorbar(r_time, mean, std, errorevery=(0,10),color="#023047")
plt.fill_between(r_time, max, min, alpha=0.5, linewidth=0, color="#8ecae6")

plt.gca().xaxis.set_major_locator(mdates.HourLocator(interval=5))
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m-%d %H:%M'))
plt.xticks(fontsize=30, rotation=30, ha='right')
plt.yticks(fontsize=30)

plt.xlabel("time", fontsize=30)
plt.ylabel("average humidity (%)", fontsize=30)
plt.title("remote humidity error bar (n=576)", fontsize=50)
plt.tight_layout()
plt.show()
#endregion

#region # local model quadratic by using polyval
fig = plt.figure (figsize=(40,20))
plt.subplots_adjust(hspace=0.5)
plt.subplot(2,1,1)

temp_coeffs = []
fitted_temp_arrays = []

for i in range(1, 4):
    temp_list_name = f"temp{i}"  # Create the variable name dynamically
    temp_list = globals()[temp_list_name]  # Access the variable using globals()
    coeffs = np.polyfit(time, temp_list, 2)
    temp_coeffs.append(coeffs)
    fitted_temp = np.polyval(coeffs, time)
    fitted_temp_arrays.append(fitted_temp)

    plt.plot(date_list, temp_list, label=f"temperature{i}", c=c[i - 1]) # Plot the original temperature data
    plt.gca().xaxis.set_major_locator(mdates.HourLocator(interval=5))
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m-%d %H:%M'))

# Unpack the fitted temperature arrays
fitted_temp1, fitted_temp2, fitted_temp3 = fitted_temp_arrays
c_temp1, c_temp2, c_temp3 = temp_coeffs

# Plot the fitted temperature data
plt.plot(date_list, fitted_temp1, label=f"quadratic model temperature1 T(t) ={c_temp1[0]:.2f}^2+{c_temp1[1]:.2f}t+{c_temp1[2]:.2f}", linestyle='--', c=c[0])
plt.plot(date_list, fitted_temp2, label=f"quadratic model temperature2 T(t) ={c_temp2[0]:.2f}^2+{c_temp2[1]:.2f}t+{c_temp2[2]:.2f}", linestyle='--', c=c[1])
plt.plot(date_list, fitted_temp3, label=f"quadratic model temperature3 T(t) ={c_temp3[0]:.2f}^2+{c_temp3[1]:.2f}t+{c_temp3[2]:.2f}", linestyle='--', c=c[2])

r2_1 = metrics.r2_score(temp_list, fitted_temp1)
print(f"temp1_fit: {r2_1}")

r2_2 = metrics.r2_score(temp_list, fitted_temp2)
print(f"temp2_fit: {r2_2}")

r2_3 = metrics.r2_score(temp_list, fitted_temp3)
print(f"temp3_fit: {r2_3}")

plt.gca().xaxis.set_major_locator(mdates.HourLocator(interval=5))
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m-%d %H:%M'))
plt.xticks(fontsize=30, rotation=30, ha='right')
plt.yticks(fontsize=20)
plt.xlabel("time", fontsize=30)
plt.ylabel("temperature (C)", fontsize=30)
plt.title("local temperature quadratic model", fontsize=40)
plt.legend(fontsize=20, loc='upper right', ncol=3)

plt.subplot(2,1,2)
humid_coeffs = []
fitted_humid_arrays = []

for i in range(1, 4):
    humid_list_name = f"humid{i}"  # Create the variable name dynamically
    humid_list = globals()[humid_list_name]  # Access the variable using globals()

    coeffs = np.polyfit(time,  humid_list, 2)
    humid_coeffs.append(coeffs)
    fitted_humid = np.polyval(coeffs, time)
    fitted_humid_arrays.append(fitted_humid)

    # Plot the original humidity data
    plt.plot(date_list, humid_list, label=f"temperature{i}", c=c[i - 1])
    plt.gca().xaxis.set_major_locator(mdates.HourLocator(interval=5))
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m-%d %H:%M'))

# Unpack the fitted humidity arrays
fitted_humid1, fitted_humid2, fitted_humid3 = fitted_humid_arrays
c_humid1, c_humid2, c_humid3 = humid_coeffs

# Plot the fitted humidity data
plt.plot(date_list, fitted_humid1, label=f"quadratic model humid1 H(t) ={c_humid1[0]:.2f}^2+{c_humid1[1]:.2f}t+{c_humid1[2]:.2f}", linestyle='--', c=c[0])
plt.plot(date_list, fitted_humid2, label=f"quadratic model humid2 H(t) ={c_humid2[0]:.2f}^2+{c_humid2[1]:.2f}t+{c_humid2[2]:.2f}", linestyle='--', c=c[1])
plt.plot(date_list, fitted_humid3, label=f"quadratic model humid3 H(t) ={c_humid3[0]:.2f}^2+{c_humid3[1]:.2f}t+{c_humid3[2]:.2f}", linestyle='--', c=c[2])

r2_1 = metrics.r2_score(temp_list, fitted_temp1)
print(f"humid1_fit: {r2_1}")

r2_2 = metrics.r2_score(temp_list, fitted_temp2)
print(f"humid2_fit: {r2_2}")

r2_3 = metrics.r2_score(temp_list, fitted_temp3)
print(f"humid3_fit: {r2_3}")

plt.gca().xaxis.set_major_locator(mdates.HourLocator(interval=5))
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m-%d %H:%M'))
plt.xticks(fontsize=30, rotation=30, ha='right')

plt.yticks(fontsize=20)
plt.title("local humidity quadratic model", fontsize=40)
plt.xlabel("time", fontsize=30)
plt.ylabel("humidity (%)", fontsize=30)
plt.legend(fontsize=20, loc='upper right', ncol=3)
plt.tight_layout()
plt.show()
#endregion

#region # remote model quadratic by using polyval
fig = plt.figure (figsize=(40,20))
plt.subplots_adjust(hspace=0.5)
plt.subplot(2,1,1)

temp_coeffs = []
fitted_temp_arrays = []

for i in range(1, 4):
    temp_list_name = f"r_temp{i}"  # Create the variable name dynamically
    temp_list = globals()[temp_list_name]  # Access the variable using globals()
    coeffs = np.polyfit(r_time_list, temp_list, 2)
    temp_coeffs.append(coeffs)
    fitted_temp = np.polyval(coeffs, r_time_list)
    fitted_temp_arrays.append(fitted_temp)

    plt.plot(r_time, temp_list, label=f"temperature{i}", c=c[i - 1]) # Plot the original temperature data
    plt.gca().xaxis.set_major_locator(mdates.HourLocator(interval=5))
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m-%d %H:%M'))

# Unpack the fitted temperature arrays
fitted_temp1, fitted_temp2, fitted_temp3 = fitted_temp_arrays
c_temp1, c_temp2, c_temp3 = temp_coeffs

# Plot the fitted temperature data
plt.plot(r_time, fitted_temp1, label=f"quadratic model temperature1 T(t) ={c_temp1[0]:.2f}^2+{c_temp1[1]:.2f}t+{c_temp1[2]:.2f}", linestyle='--', c=c[0])
plt.plot(r_time, fitted_temp2, label=f"quadratic model temperature2 T(t) ={c_temp2[0]:.2f}^2+{c_temp2[1]:.2f}t+{c_temp2[2]:.2f}", linestyle='--', c=c[1])
plt.plot(r_time, fitted_temp3, label=f"quadratic model temperature3 T(t) ={c_temp3[0]:.2f}^2+{c_temp3[1]:.2f}t+{c_temp3[2]:.2f}", linestyle='--', c=c[2])

r2_1 = metrics.r2_score(temp_list, fitted_temp1)
print(f"temp1_fit: {r2_1}")

r2_2 = metrics.r2_score(temp_list, fitted_temp2)
print(f"temp2_fit: {r2_2}")

r2_3 = metrics.r2_score(temp_list, fitted_temp3)
print(f"temp3_fit: {r2_3}")

plt.gca().xaxis.set_major_locator(mdates.HourLocator(interval=5))
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m-%d %H:%M'))
plt.xticks(fontsize=30, rotation=30, ha='right')
plt.yticks(fontsize=20)
plt.xlabel("time", fontsize=30)
plt.ylabel("temperature (C)", fontsize=30)
plt.title("remote temperature quadratic model", fontsize=40)
plt.legend(fontsize=20, loc='upper right', ncol=3)
# plt.legend(fontsize=20, loc='upper center', bbox_to_anchor=(.5, -.15), ncol=3)


plt.subplot(2,1,2)
humid_coeffs = []
fitted_humid_arrays = []

for i in range(1, 4):
    humid_list_name = f"r_humid{i}"  # Create the variable name dynamically
    humid_list = globals()[humid_list_name]  # Access the variable using globals()

    coeffs = np.polyfit(r_time_list,  humid_list, 2)
    humid_coeffs.append(coeffs)
    fitted_humid = np.polyval(coeffs, r_time_list)
    fitted_humid_arrays.append(fitted_humid)

    # Plot the original temperature data
    plt.plot(r_time, humid_list, label=f"humidity{i}", c=c[i - 1])
    plt.gca().xaxis.set_major_locator(mdates.HourLocator(interval=5))
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m-%d %H:%M'))

# Unpack the fitted temperature arrays
fitted_humid1, fitted_humid2, fitted_humid3 = fitted_humid_arrays
c_humid1, c_humid2, c_humid3 = humid_coeffs

# Plot the fitted temperature data
plt.plot(r_time, fitted_humid1, label=f"quadratic model humid1 H(t) ={c_humid1[0]:.2f}^2+{c_humid1[1]:.2f}t+{c_humid1[2]:.2f}", linestyle='--', c=c[0])
plt.plot(r_time, fitted_humid2, label=f"quadratic model humid2 H(t) ={c_humid2[0]:.2f}^2+{c_humid2[1]:.2f}t+{c_humid2[2]:.2f}", linestyle='--', c=c[1])
plt.plot(r_time, fitted_humid3, label=f"quadratic model humid3 H(t) ={c_humid3[0]:.2f}^2+{c_humid3[1]:.2f}t+{c_humid3[2]:.2f}", linestyle='--', c=c[2])

r2_1 = metrics.r2_score(temp_list, fitted_temp1)
print(f"humid1_fit: {r2_1}")

r2_2 = metrics.r2_score(temp_list, fitted_temp2)
print(f"humid2_fit: {r2_2}")

r2_3 = metrics.r2_score(temp_list, fitted_temp3)
print(f"humid3_fit: {r2_3}")

plt.gca().xaxis.set_major_locator(mdates.HourLocator(interval=5))
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m-%d %H:%M'))
plt.xticks(fontsize=30, rotation=30, ha='right')

plt.yticks(fontsize=20)
plt.title("remote humidity quadratic model", fontsize=40)
plt.xlabel("time", fontsize=30)
plt.ylabel("humidity (%)", fontsize=30)
plt.legend(fontsize=20, loc='upper right', ncol=3)
plt.tight_layout()
plt.show()
#endregion

# region # local model quatric by using polyval
fig = plt.figure (figsize=(40,20))
plt.subplots_adjust(hspace=0.5)
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
plt.plot(time, fitted_temp1, label=f"quatric model temperature1 T(t) ={c_temp1[0]:.2f}t^4+{c_temp1[1]:.2f}t^3+{c_temp1[2]:.2f}^2+{c_temp1[3]:.2f}t+{c_temp1[4]:.2f}", linestyle='--', c=c[0])
plt.plot(time, fitted_temp2, label=f"quatric model temperature2 T(t) ={c_temp2[0]:.2f}t^4+{c_temp2[1]:.2f}t^3+{c_temp2[2]:.2f}^2+{c_temp2[3]:.2f}t+{c_temp2[4]:.2f}", linestyle='--', c=c[1])
plt.plot(time, fitted_temp3, label=f"quatric model temperature3 T(t) ={c_temp3[0]:.2f}t^4+{c_temp3[1]:.2f}t^3+{c_temp3[2]:.2f}^2+{c_temp3[3]:.2f}t+{c_temp3[4]:.2f}", linestyle='--', c=c[2])
r2_1 = metrics.r2_score(temp_list, fitted_temp1)
print(f"temp1_fit: {r2_1}")

r2_2 = metrics.r2_score(temp_list, fitted_temp2)
print(f"temp2_fit: {r2_2}")

r2_3 = metrics.r2_score(temp_list, fitted_temp3)
print(f"temp3_fit: {r2_3}")
# print(f"Quadratic model T(t) ={a:.2f}t^4+{b:.2f}t^3+{c:.2f}^2+{d:.2f}t+{e:.2f}")

ticks = time[::50]
labels = [dt.strftime(date, '%m-%d %H:%M') for date in date_list[::50]]
plt.xticks(ticks, labels, fontsize=15, rotation=45, ha='right')
plt.yticks(fontsize=15)
plt.xlabel("time",fontsize=20)
plt.ylabel("temperature (C)", fontsize=20)
plt.title("local temperature quatric model", fontsize=40)
plt.legend(fontsize=15, loc='upper right', ncol=3)


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
plt.plot(time, fitted_humid1, label=f"quatric model humid1 H(t) ={c_humid1[0]:.2f}t^4+{c_humid1[1]:.2f}t^3+{c_humid1[2]:.2f}^2+{c_humid1[3]:.2f}t+{c_humid1[4]:.2f}", linestyle='--', c=c[0])
plt.plot(time, fitted_humid2, label=f"quatric model humid2 H(t) ={c_humid2[0]:.2f}t^4+{c_humid2[1]:.2f}t^3+{c_humid2[2]:.2f}^2+{c_humid2[3]:.2f}t+{c_humid2[4]:.2f}", linestyle='--', c=c[1])
plt.plot(time, fitted_humid3, label=f"quatric model humid3 H(t) ={c_humid3[0]:.2f}t^4+{c_humid3[1]:.2f}t^3+{c_humid3[2]:.2f}^2+{c_humid3[3]:.2f}t+{c_humid3[4]:.2f}", linestyle='--', c=c[2])


r2_1 = metrics.r2_score(humid_list, fitted_temp1)
print(f"humid1_fit: {r2_1}")

r2_2 = metrics.r2_score(temp_list, fitted_temp2)
print(f"humid2_fit: {r2_2}")

r2_3 = metrics.r2_score(temp_list, fitted_temp3)
print(f"humid3_fit: {r2_3}")

ticks = time[::50]
labels = [dt.strftime(date, '%m-%d %H:%M') for date in date_list[::50]]
plt.xticks(ticks, labels, fontsize=15, rotation=45, ha='right')
plt.yticks(fontsize=15)
plt.title("local humidity quatric model", fontsize=40)
plt.xlabel("time",fontsize=20)
plt.ylabel("humidity (%)", fontsize=20)
plt.legend(fontsize=15, loc='upper right', ncol=3)

plt.show()
#endregion

#region #remote model quatric by using polyval
fig = plt.figure (figsize=(40,20))
plt.subplots_adjust(hspace=0.5)
plt.subplot(2,1,1)

temp_coeffs = []
fitted_temp_arrays = []

for i in range(1, 4):
    temp_list_name = f"r_temp{i}"  # Create the variable name dynamically
    temp_list = globals()[temp_list_name]  # Access the variable using globals()
    coeffs = np.polyfit(r_time_list, temp_list, 4)
    temp_coeffs.append(coeffs)
    fitted_temp = np.polyval(coeffs, r_time_list)
    fitted_temp_arrays.append(fitted_temp)

    plt.plot(r_time, temp_list, label=f"temperature{i}", c=c[i - 1]) # Plot the original temperature data
    plt.gca().xaxis.set_major_locator(mdates.HourLocator(interval=5))
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m-%d %H:%M'))

# Unpack the fitted temperature arrays
fitted_temp1, fitted_temp2, fitted_temp3 = fitted_temp_arrays
c_temp1, c_temp2, c_temp3 = temp_coeffs

# Plot the fitted temperature data
plt.plot(r_time, fitted_temp1, label=f"quatric model temperature1 T(t) ={c_temp1[0]:.2f}t^4+{c_temp1[1]:.2f}t^3+{c_temp1[2]:.2f}^2+{c_temp1[3]:.2f}t+{c_temp1[4]:.2f}", linestyle='--', c=c[0])
plt.plot(r_time, fitted_temp2, label=f"quatric model temperature2 T(t) ={c_temp2[0]:.2f}t^4+{c_temp2[1]:.2f}t^3+{c_temp2[2]:.2f}^2+{c_temp2[3]:.2f}t+{c_temp2[4]:.2f}", linestyle='--', c=c[1])
plt.plot(r_time, fitted_temp3, label=f"quatric model temperature3 T(t) ={c_temp3[0]:.2f}t^4+{c_temp3[1]:.2f}t^3+{c_temp3[2]:.2f}^2+{c_temp3[3]:.2f}t+{c_temp3[4]:.2f}", linestyle='--', c=c[2])

r2_1 = metrics.r2_score(temp_list, fitted_temp1)
print(f"temp1_fit: {r2_1}")

r2_2 = metrics.r2_score(temp_list, fitted_temp2)
print(f"temp2_fit: {r2_2}")

r2_3 = metrics.r2_score(temp_list, fitted_temp3)
print(f"temp3_fit: {r2_3}")

plt.gca().xaxis.set_major_locator(mdates.HourLocator(interval=5))
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m-%d %H:%M'))
plt.xticks(fontsize=30, rotation=30, ha='right')
plt.yticks(fontsize=20)
plt.xlabel("time", fontsize=30)
plt.ylabel("temperature (C)", fontsize=30)
plt.title("remote temperature quatric model", fontsize=40)
plt.legend(fontsize=20, loc='upper right', ncol=3)
# plt.legend(fontsize=20, loc='upper center', bbox_to_anchor=(.5, -.15), ncol=3)


plt.subplot(2,1,2)
humid_coeffs = []
fitted_humid_arrays = []

for i in range(1, 4):
    humid_list_name = f"r_humid{i}"  # Create the variable name dynamically
    humid_list = globals()[humid_list_name]  # Access the variable using globals()

    coeffs = np.polyfit(r_time_list,  humid_list, 4)
    humid_coeffs.append(coeffs)
    fitted_humid = np.polyval(coeffs, r_time_list)
    fitted_humid_arrays.append(fitted_humid)

    # Plot the original temperature data
    plt.plot(r_time, humid_list, label=f"humidity{i}", c=c[i - 1])
    plt.gca().xaxis.set_major_locator(mdates.HourLocator(interval=5))
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m-%d %H:%M'))

# Unpack the fitted humid arrays
fitted_humid1, fitted_humid2, fitted_humid3 = fitted_humid_arrays
c_humid1, c_humid2, c_humid3 = humid_coeffs

# Plot the fitted temperature data
plt.plot(r_time, fitted_humid1, label=f"quatric model humid1 H(t) ={c_humid1[0]:.2f}t^4+{c_humid1[1]:.2f}t^3+{c_humid1[2]:.2f}^2+{c_humid1[3]:.2f}t+{c_humid1[4]:.2f}", linestyle='--', c=c[0])
plt.plot(r_time, fitted_humid2, label=f"quatric model humid2 H(t) ={c_humid2[0]:.2f}t^4+{c_humid2[1]:.2f}t^3+{c_humid2[2]:.2f}^2+{c_humid2[3]:.2f}t+{c_humid2[4]:.2f}", linestyle='--', c=c[1])
plt.plot(r_time, fitted_humid3, label=f"quatric model humid3 H(t) ={c_humid3[0]:.2f}t^4+{c_humid3[1]:.2f}t^3+{c_humid3[2]:.2f}^2+{c_humid3[3]:.2f}t+{c_humid3[4]:.2f}", linestyle='--', c=c[2])

r2_1 = metrics.r2_score(temp_list, fitted_temp1)
print(f"humid1_fit: {r2_1}")

r2_2 = metrics.r2_score(temp_list, fitted_temp2)
print(f"humid2_fit: {r2_2}")

r2_3 = metrics.r2_score(temp_list, fitted_temp3)
print(f"humid3_fit: {r2_3}")

plt.gca().xaxis.set_major_locator(mdates.HourLocator(interval=5))
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m-%d %H:%M'))
plt.xticks(fontsize=30, rotation=30, ha='right')

plt.yticks(fontsize=20)
plt.title("remote humidity quatric model", fontsize=40)
plt.xlabel("time", fontsize=30)
plt.ylabel("humidity (%)", fontsize=30)
plt.legend(fontsize=20, loc='upper right', ncol=3)
plt.tight_layout()
plt.show()
#endregion

#region # prediction quadratic by using polyval
t=time[-1]
future_time=time[:]
print(t)
for i in range(144):
    t+=5
    future_time.append(t)

fig = plt.figure (figsize=(40,20))
plt.subplots_adjust(hspace=0.5)
plt.subplot(2,1,1)

temp_coeffs = []
fitted_temp_arrays = []

for i in range(1, 4):
    temp_list_name = f"temp{i}"  # Create the variable name dynamically
    temp_list = globals()[temp_list_name]  # Access the variable using globals()
    coeffs = np.polyfit(time, temp_list, 2)
    temp_coeffs.append(coeffs)

    # Using np.polyval for quadratic predictions
    fitted_temp = np.polyval(coeffs, time)
    fitted_temp_arrays.append(fitted_temp)

    f_fitted_temp = np.polyval(coeffs, future_time)

    plt.plot(time, temp_list, label=f"temperature{i}", c=c[i - 1]) # Plot the original temperature data
    plt.gca().xaxis.set_major_locator(mdates.HourLocator(interval=5))
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m-%d %H:%M'))

    plt.plot(future_time[len(time):], f_fitted_temp[len(time):],
             label=f"temperature quadratic prediction{i} T(t) ={coeffs[0]:.2f}^2+{coeffs[1]:.2f}t+{coeffs[2]:.2f}",
             c=c[i - 1], linestyle='--')

current_date = date_list[-1]
future_dates = [current_date + timedelta(minutes=i*5) for i in range(1, 145)]
future_dates = date_list+future_dates
labels = [date.strftime('%m-%d %H:%M') for date in future_dates[::50]]

ticks = future_time[::50]

plt.xticks(ticks, labels, fontsize=15, rotation=45, ha='right')
plt.yticks(fontsize=15)
plt.xlabel("time", fontsize=20)
plt.ylabel("temperature (C)", fontsize=20)
plt.title("local temperature quadratic prediction", fontsize=40)
plt.legend(fontsize=20, loc='upper right', ncol=3)

plt.subplot(2,1,2)
humid_coeffs = []
fitted_humid_arrays = []

for i in range(1, 4):
    humid_list_name = f"humid{i}"  # Create the variable name dynamically
    humid_list = globals()[humid_list_name]  # Access the variable using globals()

    coeffs = np.polyfit(time,  humid_list, 2)
    humid_coeffs.append(coeffs)
    fitted_humid = np.polyval(coeffs, time)
    fitted_humid_arrays.append(fitted_humid)

    f_fitted_humid = np.polyval(coeffs, future_time)

    # Plot the original temperature data
    plt.plot(time, humid_list, label=f"temperature{i}", c=c[i - 1])
    plt.gca().xaxis.set_major_locator(mdates.HourLocator(interval=5))
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m-%d %H:%M'))

    plt.plot(future_time[len(time):], f_fitted_humid[len(time):],
             label=f"temperature quadratic prediction{i} T(t) ={coeffs[0]:.2f}^2+{coeffs[1]:.2f}t+{coeffs[2]:.2f}",
             c=c[i - 1], linestyle='--')

current_date = date_list[-1]
future_dates = [current_date + timedelta(minutes=i*5) for i in range(1, 145)]
future_dates = date_list+future_dates
labels = [date.strftime('%m-%d %H:%M') for date in future_dates[::50]]

ticks = future_time[::50]

plt.xticks(ticks, labels, fontsize=15, rotation=45, ha='right')
plt.yticks(fontsize=15)
plt.title("local humidity quadratic prediction", fontsize=40)
plt.xlabel("time", fontsize=20)
plt.ylabel("humidity (%)", fontsize=20)
plt.legend(fontsize=15, loc='upper right', ncol=3)
plt.tight_layout()
plt.show()
#endregion

#region # prediction quatric by using polyval
t=time[-1]
future_time=time[:]
print(t)
for i in range(144):
    t+=5
    future_time.append(t)

fig = plt.figure (figsize=(40,20))
plt.subplots_adjust(hspace=0.5)
plt.subplot(2,1,1)

temp_coeffs = []
fitted_temp_arrays = []

for i in range(1, 4):
    temp_list_name = f"temp{i}"  # Create the variable name dynamically
    temp_list = globals()[temp_list_name]  # Access the variable using globals()
    coeffs = np.polyfit(time, temp_list, 4)
    temp_coeffs.append(coeffs)

    # Using np.polyval for quadratic predictions
    fitted_temp = np.polyval(coeffs, time)
    fitted_temp_arrays.append(fitted_temp)

    f_fitted_temp = np.polyval(coeffs, future_time)

    plt.plot(time, temp_list, label=f"temperature{i}", c=c[i - 1]) # Plot the original temperature data
    plt.gca().xaxis.set_major_locator(mdates.HourLocator(interval=5))
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m-%d %H:%M'))

    plt.plot(future_time[len(time):], f_fitted_temp[len(time):],
             label=f"temperature quatric prediction{i} T(t) ={coeffs[0]:.2f}t^4+{coeffs[1]:.2f}t^3+{coeffs[2]:.2f}^2+{coeffs[3]:.2f}t+{coeffs[4]:.2f}",
             c=c[i - 1], linestyle='--')

current_date = date_list[-1]
future_dates = [current_date + timedelta(minutes=i*5) for i in range(1, 145)]
future_dates = date_list+future_dates
labels = [date.strftime('%m-%d %H:%M') for date in future_dates[::50]]

ticks = future_time[::50]

plt.xticks(ticks, labels, fontsize=15, rotation=45, ha='right')
plt.yticks(fontsize=15)
plt.xlabel("time", fontsize=20)
plt.ylabel("temperature (C)", fontsize=20)
plt.title("local temperature quatric prediction", fontsize=40)
plt.legend(fontsize=15, loc='upper right', ncol=3)

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

    f_fitted_humid = np.polyval(coeffs, future_time)

    # Plot the original temperature data
    plt.plot(time, humid_list, label=f"temperature{i}", c=c[i - 1])
    plt.gca().xaxis.set_major_locator(mdates.HourLocator(interval=5))
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m-%d %H:%M'))

    plt.plot(future_time[len(time):], f_fitted_humid[len(time):],
             label=f"temperature quatric prediction{i} T(t) ={coeffs[0]:.2f}t^4+{coeffs[1]:.2f}t^3+{coeffs[2]:.2f}^2+{coeffs[3]:.2f}t+{coeffs[4]:.2f}",
             c=c[i - 1], linestyle='--')

current_date = date_list[-1]
future_dates = [current_date + timedelta(minutes=i*5) for i in range(1, 145)]
future_dates = date_list+future_dates
labels = [date.strftime('%m-%d %H:%M') for date in future_dates[::50]]

ticks = future_time[::50]

plt.xticks(ticks, labels, fontsize=15, rotation=45, ha='right')
plt.yticks(fontsize=15)
plt.title("local humidity quatric prediction", fontsize=40)
plt.xlabel("time", fontsize=20)
plt.ylabel("humidity (%)", fontsize=20)
plt.legend(fontsize=15, loc='upper right', ncol=3)
plt.tight_layout()
plt.show()
#endregion
