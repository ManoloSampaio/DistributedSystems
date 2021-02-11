from _thread import *
import threading 
import time
import app_pb2
from client import SmartRoomClient
def listen_mensage(client):
    while True:
        mensage =client.read_mensage()
        print(f"({mensage.object_name}):{mensage.result}")
        
def send_mensage(client):
    print("Enviar Mensagem")
    while True:    
        mensagem_object=input('')
        mensagem_type=input('')
        request_mensage = app_pb2.Request_APP()
        if mensagem_type=='mod':
            request_mensage.rtype = app_pb2.Request_APP.RequestType.ModStatus
            if mensagem_object=='tv':
                status=input('Insira o volume')
            
            if mensagem_object=='ar':
                status=input('Insira a temperatura desejada')
            
            if mensagem_object=='lampada':
                status=input('Insira a cor da lampada')        

        request_mensage.status_modification = status
        if mensagem_type == 'sensor':
            request_mensage.rtype = app_pb2.Request_APP.RequestType.ReadSensor
        
        if mensagem_type == 'status':
            request_mensage.rtype = app_pb2.Request_APP.RequestType.ReadStatus
        
        if mensagem_type =='ligar' or mensagem_type=='desligar':
            request_mensage.rtype = app_pb2.Request_APP.RequestType.ModOnOf
            if mensagem_type=='ligar':
                request_mensage.on_off= app_pb2.Request_APP.ON_OFF.ON
            else:
                request_mensage.on_off=app_pb2.Request_APP.ON_OFF.OFF
        
        if mensagem_object == 'tv':
            request_mensage.gtype = app_pb2.Request_APP.GType.TV
            request_mensage.nome = 'Televisao'
        if mensagem_object == 'ar':
            request_mensage.gtype = app_pb2.Request_APP.GType.AR
        
        if mensagem_object == 'lamp':
            request_mensage.gtype = app_pb2.Request_APP.GType.LAMPADA
        
        client.send_mensage(request_mensage.SerializeToString())
        


    
server_ip = '127.0.0.1'
server_port = 65433

client = SmartRoomClient(server_ip,server_port)
print("Conectando com o servidor")
t_1 = threading.Thread(target=send_mensage, args=(client,))
t_2 = threading.Thread(target=listen_mensage, args=(client,))

t_1.start()
t_2.start()