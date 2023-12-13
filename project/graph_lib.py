import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

plt.style.use('ggplot')

# take out data from csv file
def take_data():
    with open('final_readings.csv', mode='r') as f:
        data = f.readlines()
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
            temp1.append(float(rec[2])) #0
            temp2.append(float(rec[3])) #1
            temp3.append(float(rec[4])) #2
            humid1.append(float(rec[5])) #3
            humid2.append(float(rec[6])) #4
            humid3.append(float(rec[7])) #5
            time.append(t) #6
            t+=5

    return temp1, temp2, temp3, humid1, humid2, humid3, time

# draw graph
def draw_graph (t:list, v:list, color:str, title:str):
    plt.plot(t, v, color=f"{color}")
    plt.title(title, fontsize=30)
    plt.xticks(rotation=30)
    plt.tick_params(labelsize=25)
    plt.gca().xaxis.set_major_locator(mdates.HourLocator(interval=10))


# smoothing
def smoothing(x:list, size_window:int=5):
    smooth_x = []
    smooth_time = []
    for i in range(0, len(x) + size_window, size_window):
        points = sum(x[i: i + size_window]) / size_window
        smooth_x.append(points)
        smooth_time.append(i)
        points = sum(x[i + (size_window // 2): i + size_window + (size_window // 2)]) / size_window
        smooth_x.append(points)
        smooth_time.append(i)

    return smooth_time, smooth_x

# average
def basic_info (x:list, y:list, z:list):
    total=[]
    mean = []
    std = []
    min_val = []
    max_val = []
    avg = []
    median = []

    for i in range(len(x)):
        total.append([x[i],y[i],z[i]])

    for item in total:
        mean.append(np.mean(item)) #0
        std.append(np.std(item)) #1
        min_val.append(np.min(item)) #2
        max_val.append(np.max(item)) #3
        median.append(np.median(item)) #4

    return mean, std, min_val, max_val, median


def standardalization (data:list):
    data_array = np.array(data)
    data_reshaped = data_array.reshape(-1, 1)
    scaler = StandardScaler()
    sc_data = scaler.fit_transform(data_reshaped)
    time = np.arange(sc_data.shape[0])

    return time, sc_data



