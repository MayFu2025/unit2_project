import requests
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from graph_lib import draw_graph, smoothing, basic_info, standardalization, take_data
import numpy as np
from matplotlib.dates import DateFormatter
import matplotlib.dates as mdates
from scipy.signal import savgol_filter
import sklearn.metrics as metrics

user = {"username": "MMproject", "password": "MMproject2"}
ip = "192.168.6.153"


# Register User [COMPLETE]
# answer = requests.post(f'http://{ip}/register', json=user)
# print(answer.json())

# Log-in to get Cookie
answer = requests.post(f'http://{ip}/login', json=user)
# print(answer.json()) [CHECKED THAT IT WORKS]
cookie = answer.json()["access_token"]
# print(cookie)


# Put the cookie in the header of the request
header = {'Authorization':f'Bearer {cookie}'}

# Create a Sensor
s1_t = {
    'type': 'temperature',
    'location': 'table',
    'name': 'dht1_temp',
    'unit': 'C'
} #id=29

s2_t = {
    'type': 'temperature',
    'location': 'door',
    'name': 'dht2_temp',
    'unit': 'C'
} #id=30

s3_t = {
    'type': 'temperature',
    'location': 'window',
    'name': 'dht3_temp',
    'unit': 'C'
} #id=31

s1_h = {
    'type': 'humidity',
    'location': 'table',
    'name': 'dht1_hum',
    'unit': '%'
} #id=32

s2_h = {
    'type': 'humidity',
    'location': 'door',
    'name': 'dht2_hum',
    'unit': '%'
} #id=33

s3_h = {
    'type': 'humidity',
    'location': 'window',
    'name': 'dht3_hum',
    'unit': '%'
} #id=34

# answer = requests.post(f'http://{ip}/sensor/new', json=s3_h, headers=header)
# print(answer.json())

# See your sensors + id
# answer = requests.get(f"http://{ip}/sensors", headers=header)
# print(answer.json())

# Send a recording to server
# record = {'sensor_id':27,'value':6}
# answer = requests.post(f'http://{ip}/reading/new', json=record, headers=header)
# print(answer.json())

# # Get all my recordings
# answer = requests.get(f"http://{ip}/readings", headers=header)  # "http://{ip}/user/readings"
# data = answer.json()
# readings = data['readings'][0]
# print(answer.json())
# print(readings)

request = requests.get(f"http://192.168.6.153/readings")
data = request.json()
sensors = data['readings'][0]
# sensor = []
list_search = [ item for item in sensors if item['sensor_id'] == 2]
# print(list_search)


# def get_sensor_w(id:int=1, ip:str="192.168.6.153"):
#     request = requests.get(f"http://{ip}/readings")
#     data = request.json()
#     sensors = data['readings'][0]
#     # sensor = []
#     for item in sensors:
#         if item['id'] == '2':
#         print(sensors)
#
#     return sensor

def get_sensor(id:int=1, ip:str="192.168.6.153"):
    request = requests.get(f"http://{ip}/readings")
    data = request.json()
    sensors = data['readings'][0]
    sensor = []
    for s in sensors:
        if s['sensor_id'] == id:
            sensor.append(s['value'])
    return sensor

def smoothing(x:list[int], size_window:int=5, overlap:float=1):
    smooth_x = []
    t = []
    for i in range(0,len(x), size_window):
        points = sum(x[i:(i+size_window)])/(size_window*overlap)
        smooth_x.append(points)
        t.append(i)

    return t, smooth_x




def get_sensor_w_date(id:int=1, ip:str="192.168.6.153"):
    from_dt = datetime(2023, 12, 7, 10, 45)
    to_dt = datetime(2023, 12, 9, 16, 25)
    request = requests.get(f"http://{ip}/readings")
    data = request.json()
    sensors = data['readings'][0]
    sensor = []
    time=[]
    for s in sensors:
        if s['sensor_id'] == id:
            sensor_datetime = datetime.strptime(s['datetime'][:16], "%Y-%m-%dT%H:%M")
            adjusted_sensor_datetime = sensor_datetime - timedelta(days=6)
            if from_dt <= sensor_datetime<= to_dt:
                sensor.append(s['value'])
                time.append(adjusted_sensor_datetime)
    return time,sensor

def fake_humid (x:list, y:list):
    total=[]
    mean = []
    for i in range(len(get_sensor_w_date(id=4)[1])):
        total.append([x[i],y[i]])
    for item in total:
        mean.append(np.mean(item))
    return mean



#