from sensor import Sensor
from _thread import *
import threading

def send_data(s):
    while True:
        s.publish()

def get_data(s):
    while True:
        s.get_data()

sensor_type = int(input('Digite o tipo de sensor:' ))
sensor_name = input('Digite o nome do sensor: ')

s=Sensor('localhost',65433,sensor_type,sensor_name)

t_1 = threading.Thread(target = send_data,args=(s,))
t_2 = threading.Thread(target = get_data,args=(s,))

t_1.start()
t_2.start()