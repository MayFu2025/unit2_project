import matplotlib.pyplot as plt
from graph_lib import draw_graph, smoothing, basic_info

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

print(len(time))
print(len(smoothing(x=temp1, size_window=5)[1]))


# temp, humid graph
# plt.subplot(2,3,1)
# temp1_graph=draw_graph(t=time, v=temp1, color='black', title="temp1")
#
# plt.subplot(2,3,2)
# temp2_graph=draw_graph(t=time, v=temp2, color='black', title="temp2")
#
# plt.subplot(2,3,3)
# temp3_graph=draw_graph(t=time, v=temp3, color='black', title="temp3")
#
# plt.subplot(2,3,4)
# humid1_graph=draw_graph(t=time, v=humid1, color='black', title="humid1")
#
# plt.subplot(2,3,5)
# humid2_graph=draw_graph(t=time, v=humid2, color='black', title="humid2")
#
# plt.subplot(2,3,6)
# humid3_graph=draw_graph(t=time, v=humid3, color='black', title="humid3")
# plt.show()


# smoothing graph
plt.subplot(2,3,1)
temp1_graph=draw_graph(smoothing(x=temp1, size_window=5)[0], smoothing(x=temp1, size_window=5)[1], color='black', title="smooth temp1")

plt.subplot(2,3,2)
temp1_graph=draw_graph(smoothing(x=temp2, size_window=5)[0], smoothing(x=temp2, size_window=5)[1], color='black', title="smooth temp2")

plt.subplot(2,3,3)
temp1_graph=draw_graph(smoothing(x=temp3, size_window=5)[0], smoothing(x=temp3, size_window=5)[1], color='black', title="smooth temp3")

plt.subplot(2,3,4)
temp1_graph=draw_graph(smoothing(x=humid1, size_window=5)[0], smoothing(x=humid1, size_window=5)[1], color='black', title="smooth humid1")

plt.subplot(2,3,5)
temp1_graph=draw_graph(smoothing(x=humid2, size_window=5)[0], smoothing(x=humid2, size_window=5)[1], color='black', title="smooth humid2")

plt.subplot(2,3,6)
humid3_graph=draw_graph(t=time, v=humid3, color='black', title="humid3")
plt.show()




# basic info graph of temp
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


