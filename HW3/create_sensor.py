from sensor import Sensor
import time
from _thread import *
import threading 

def get_data(sensor):
    while True:
        time.sleep(2.5)
        sensor.get_data()

def send_data(sensor):
    while True:
        time.sleep(5)
        sensor.publish()
    
    
sensor_type=input('Tipo de sensor: 1:umidade,2:temperatura,3:luminosidade')
ip_ambiente = 'localhost'
port = 65432
sensor = Sensor(ip_ambiente,port,sensor_type)

t_1 = threading.Thread(target =get_data,args=(sensor,))
t_2 = threading.Thread(target =send_data,args=(sensor,))

t_1.start()
t_2.start()