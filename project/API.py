import requests

user = {"username": "MMproject", "password": "MMproject2"}
ip = "192.168.6.153"


# Register User [COMPLETE]
# answer = requests.post(f'http://{ip}/register', json=user)
# print(answer.json())

# Log-in to get Cookie
answer = requests.post(f'http://{ip}/login', json=user)
# print(answer.json()) [CHECKED THAT IT WORKS]
cookie = answer.json()["access_token"]

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
