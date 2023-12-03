import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import numpy as np

plt.style.use('ggplot')

# draw graph
def draw_graph (t:list[int], v:list[int], color:str, title):
    plt.plot(t, v, color=f"{color}")
    plt.title(title)

# smoothing
def smoothing(x:list[int], size_window:int=5):
    smooth_x = []
    for i in range(0, len(x), size_window):
        points=sum(x[i : i + size_window]) / size_window
        smooth_x.append(points)
    return smooth_x

# average
def basic_info (x:list[int], y:list[int], z:list[int]):
    total=[]
    mean = []
    std = []
    min = []
    max = []
    avg = []
    for t in rnage(len(x)):
        total.append([int(x[i]),int(y[i]),int(z[i])])
    for x in total:
        mean.append(np.mean(i))
        std.append(np.std(i))
        min.append(np.min(i))
        max.append(np.max(i))
        avg.append(np.sum(i)/3)

    return mean, std, min, max, avg


