import matplotlib.pyplot as plt
from graph_lib import draw_graph,smoothing

with open('testcase.csv', mode='r') as f:
    data = f.readlines()
    temp1 = []
    hum1 = []
    temp2 = []
    hum3 = []
    temp3 = []
    hum3 = []
    t=0
    time=[]
    for i in range(len('testcase.csv')):
        t1 = line.split(',')[1]
        t2 = line.split(',')[2]
        t3 = line.split(',')[3]
        h1 = line.split(',')[4]
        h2 = line.split(',')[5]
        h3 = line.split(',')[6]

        temp1.append(t1)
        temp2.append(t2)
        temp3.append(t3)
        humid1.append(h1)
        humid2.append(h2)
        humid3.append(h3)
        time.append(t)
        t+=1

    print(data)


# graph of temp1
temp1_graph=draw_graph(t=time, v=temp1, color='black')
plt.show()

#smoothing graph of temp1
temp1_smoothing = draw_graph(t=time, v=smoothing(x=temp1, size_window='5'))
plt.show()


