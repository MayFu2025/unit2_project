import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import numpy as np

plt.style.use('ggplot')

# draw graph
def draw_graph (t:list[int], v:list[int], color:str, title:str):
    plt.plot(t, v, color=f"{color}")
    plt.title(title)

# smoothing
def smoothing(x:list[float], size_window:int=5):
    smooth_x = []
    for i in range(0, len(x), size_window):
        points=sum(x[i : i + size_window]) / size_window
        smooth_x.append(points)
    return smooth_x

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


