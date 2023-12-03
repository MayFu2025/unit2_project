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
        t+=1

    print(data)


# print(time)
# print(temp1)

# graph of temp1
# temp1_graph=draw_graph(t=time, v=temp1, color='black', title="temp1")
# plt.show()

#smoothing graph of temp1
# temp1_smoothing = draw_graph(t=time, v=smoothing(x=temp1, size_window=5))
# plt.show()
#
# print(f"temp1:{temp1}")
# print(f"temp2:{temp2}")
# print(f"temp3:{temp3}")


# avg graph of temp
temp1_avg=basic_info(x=temp1, y=temp2, z=temp3)
print(f"mean:{temp1_avg[0]}")
print(f"std: {temp1_avg[1]}")
print(f"min: {temp1_avg[2]}")
print(f"{temp1_avg[3]}")
print(temp1_avg[4])


temp_avg = draw_graph(t=time, v=temp1_avg[4],color='black', title="temperature average")
plt.show()


