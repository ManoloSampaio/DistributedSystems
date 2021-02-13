from arcon import ArCodicionado
from _thread import *
import threading
import time
import gateway_pb2

def send_temperature(ar):
    while True:
        time.sleep(10)
        response = gateway_pb2.GadgetsResponse()
        response.sensor_ident = 1
        response.result = f'Room Temperature {ar.temperature_sensor}'
        ar.socket.send(response.SerializeToString())
    

ar = ArCodicionado('228.0.0.8',50000,'Ar','127.0.0.1',65432)
t_1 = threading.Thread(target=send_temperature, args=(ar,))
t_1.start()
while ar.ON_OFF:    
    ar.receive_mensage()
    ar.change_temperature()
    
    
    