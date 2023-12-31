import requests
from datetime import datetime

user = {"username": "MMproject", "password": "MMproject2"}
ip = "192.168.6.153"


# Register User [COMPLETE]
# answer = requests.post(f'http://{ip}/register', json=user)
# print(answer.json())

# Log-in to get Cookie
answer = requests.post(f'http://{ip}/login', json=user)
# print(answer.json()) [CHECKED THAT IT WORKS]
cookie = answer.json()["access_token"]
print(cookie)


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
list_search = [ item for item in sensors if item['sensor_id'] == 31]
print(list_search)


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


from_dt= datetime(2023, 12, 6, 10, 45)
to_dt=datetime(2023, 12, 8, 16, 25)

def get_sensor_w_date(id:int=1, ip:str="192.168.6.153"):
    request = requests.get(f"http://{ip}/readings")
    data = request.json()
    sensors = data['readings'][0]
    sensor = []
    for s in sensors:
        if s['sensor_id'] == id:
            sensor_datetime = datetime.strptime(s['datetime'], "%Y-%m-%dT%H:%M:%S.%f")
            if from_dt <= sensor_datetime<= to_dt:
                sensor.append(s['value'])
    return sensor

# print(get_sensor(2))
# print(len(get_sensor(2)))
# print(get_sensor_w_date(1))
# print(len(get_sensor_w_date(1)))
# print(get_sensor_w_date(2))

# print(get_sensor_w_date(0))
# print(get_sensor_w_date(1))
# print(get_sensor_w_date(2))
# print(get_sensor_w_date(3))
# print(get_sensor_w_date(4))
# print(get_sensor_w_date(5))
