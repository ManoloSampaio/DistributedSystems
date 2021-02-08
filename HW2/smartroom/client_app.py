from _thread import *
import threading 
import time
import app_pb2
from client import SmartRoomClient
def listen_mensage(client):
    while True:
        mensage =client.rec_mensage()
        if mensage.ResponseType==app_pb2.Response.ResponseType.STATUS:
           gagget = mensage.object_name
           status = mensage.Status
           print(f"({gagget}):{status}")
        
        if mensage.ResponseType==app_pb2.Response.ResponseType.SENSOR:
           gagget = mensage.object_name
           sensor = mensage.Sensor.sensor_value
           print(f"({gagget}):{sensor}")
        if mensage.ResponseType==app_pb2.Response.ResponseType.AddUser:
           mensage = mensage.Add.wellcome
           print(mensage)
    
def send_mensage(client):
    print("Enviar Mensagem")
    while True:    
        mensagem_type=input('')
        mensagem_object=input('')

        request_mensage = app_pb2.Request()
        if mensagem_type == 'sensor':
            request_mensage.rtype = app_pb2.Request.RequestType.ReadSensor
        
        if mensagem_type == 'mod_status':
            request_mensage.rtype = app_pb2.Request.RequestType.ModStatus
            
        if mensagem_type == 'see_status':
            request_mensage.rtype = app_pb2.Request.RequestType.ReadStatus
        
        if mensagem_object == 'tv':
            request_mensage.gtype = app_pb2.Request.GType.TV
        
        if mensagem_object == 'ar':
            request_mensage.gtype = app_pb2.Request.GType.AR
        
        if mensagem_object == 'lamp':
            request_mensage.gtype = app_pb2.Request.GType.LAMPADA
        
        client.send_mensage(request_mensage.SerializeToString())
        


    
server_ip = '127.0.0.1'
server_port = 65432

client = SmartRoomClient(server_ip,server_port)
print("Conectando com o servidor")
t_1 = threading.Thread(target=send_mensage, args=(client,))
#t_2 = threading.Thread(target=listen_mensage, args=(client,))

t_1.start()
#t_2.start()