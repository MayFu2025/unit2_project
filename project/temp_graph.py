import matplotlib.pyplot as plt
from graph_lib import draw_graph, smoothing, basic_info, take_data

time = take_data()[6]

#temp, humid graph
fig = plt.figure(figsize=(30,20))
plt.subplot(2,3,1)
plt.ylim(0,60)
temp1_graph=draw_graph(t=time, v=take_data()[0], color='red', title="temp1")

plt.subplot(2,3,2)
plt.ylim(0,60)
temp2_graph=draw_graph(t=time, v=take_data()[1], color='blue', title="temp2")

plt.subplot(2,3,3)
plt.ylim(0,60)
temp3_graph=draw_graph(t=time, v=take_data()[2], color='green', title="temp3")

plt.subplot(2,3,4)
plt.ylim(0,100)
humid1_graph=draw_graph(t=time, v=take_data()[3], color='red', title="humid1")

plt.subplot(2,3,5)
plt.ylim(0,100)
humid2_graph=draw_graph(t=time, v=take_data()[4], color='blue', title="humid2")

plt.subplot(2,3,6)
plt.ylim(0,100)
humid3_graph=draw_graph(t=time, v=take_data()[5], color='green', title="humid3")
plt.show()

