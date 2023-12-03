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
        t1 = line.split(',')[2]
        t2 = line.split(',')[3]
        t3 = line.split(',')[4]
        h1 = line.split(',')[5]
        h2 = line.split(',')[6]
        h3 = line.split(',')[7].strip()

        temp1.append(float(t1))
        temp2.append(float(t2))
        temp3.append(float(t3))
        humid1.append(float(h1))
        humid2.append(float(h2))
        humid3.append(float(h3))
        time.append(t)
        t+=5

print(len(time))
print(len(smoothing(x=temp1, size_window=5)))


# print(time)
# print(temp1)


plt.subplot(2,3,1)
temp1_graph=draw_graph(t=time, v=temp1, color='black', title="temp1")

plt.subplot(2,3,2)
temp2_graph=draw_graph(t=time, v=temp2, color='black', title="temp2")

plt.subplot(2,3,3)
temp3_graph=draw_graph(t=time, v=temp3, color='black', title="temp3")

plt.subplot(2,3,4)
humid1_graph=draw_graph(t=time, v=humid1, color='black', title="humid1")

plt.subplot(2,3,5)
humid2_graph=draw_graph(t=time, v=humid2, color='black', title="humid2")

plt.subplot(2,3,6)
humid3_graph=draw_graph(t=time, v=humid3, color='black', title="humid3")
plt.show()



# graph of temp1


# humid2_graph=draw_graph(t=time, v=humid2, color='black', title="humid2")
# plt.show()

#smoothing graph of temp1
# temp1_smoothing = draw_graph(t=time, v=smoothing(x=temp1, size_window=5), color="red", title="temperature1 smoothing graph")
# plt.show()
#
# print(f"temp1:{temp1}")
# print(f"temp2:{temp2}")
# print(f"temp3:{temp3}")


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


