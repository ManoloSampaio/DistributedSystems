from sensor import Sensor
from _thread import *
import threading

def send_data(s):
    while True:
        s.publish()

def get_data(s):
    while True:
        s.get_data()

sensor_type = int(input('\nDigite 1: Sensor de Umidade\nDigite 2: Sensor de Temperatura\nDigite 3: Sensor de luminosidade\n'))
sensor_name = input('Digite o nome do sensor: ')

s=Sensor('localhost',50000,sensor_type-1,sensor_name)
s.get_data()

t_1 = threading.Thread(target = send_data,args=(s,))
t_2 = threading.Thread(target = get_data,args=(s,))

t_1.start()
t_2.start()