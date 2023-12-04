import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import numpy as np

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
            temp1.append(float(rec[2]))
            temp2.append(float(rec[3]))
            temp3.append(float(rec[4]))
            humid1.append(float(rec[5]))
            humid2.append(float(rec[6]))
            humid3.append(float(rec[7]))
            time.append(t)
            t+=5


# draw graph
def draw_graph (t:list, v:list, color:str, title:str):
    plt.plot(t, v, color=f"{color}")
    plt.title(title, fontsize=30)
    plt.tick_params(labelsize=25)

# smoothing
def smoothing(x:list, size_window:int=5):
    time = 0
    smooth_x = []
    smooth_time = []
    for i in range(0, len(x), size_window):
        points=sum(x[i : i + size_window]) / size_window
        smooth_x.append(points)
        smooth_time.append(time)
        time += 1
    return smooth_time, smooth_x

# average
def basic_info (x:list, y:list, z:list):
    total=[]
    mean = []
    std = []
    min_val = []
    max_val = []
    avg = []

    for i in range(len(x)):
        total.append([x[i],y[i],z[i]])
        # print(total)
        # print(total[i])

    for item in total:
        mean.append(np.mean(item)) #0
        std.append(np.std(item)) #1
        min_val.append(np.min(item)) #2
        max_val.append(np.max(item)) #3
        avg.append(np.sum(item)//3) #4

    return mean, std, min_val, max_val, avg



