import csv

time = []
t1 = []
t2 = []
t3 = []
h1 = []
h2 = []
h3 = []
with open ('final_readings.csv', mode='r') as f:
    data = f.readlines()
    for line in data:
        rec = line.strip().split(',')
        time.append(float(rec[0]))
        t1.append(float(rec[2]))
        t2.append(float(rec[3]))
        t3.append(float(rec[4]))
        h1.append(float(rec[5]))
        h2.append(float(rec[6]))
        h3.append(float(rec[7]))
#
# fig = plt.figure(figsize=(8, 10))
# plt.subplot(3,2,1)
# plt.plot(time, t1, color='red')
# plt.title('temp1')
# plt.ylim(5,40)
# plt.subplot(3,2,3)
# plt.plot(time, t2, color='blue')
# plt.title('temp2')
# plt.ylim(5,40)
# plt.subplot(3,2,5)
# plt.plot(time, t3, color='green')
# plt.title('temp3')
# plt.ylim(5,40)
# plt.subplot(3,2,2)
# plt.plot(time, h1, color='red')
# plt.title('hum1')
# plt.ylim(20,80)
# plt.subplot(3,2,4)
# plt.plot(time, h2, color='blue')
# plt.title('hum2')
# plt.ylim(20,80)
# plt.subplot(3,2,6)
# plt.plot(time, h3, color='green')
# plt.title('hum3')
# plt.ylim(20,80)
# plt.show()
