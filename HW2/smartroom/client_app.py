from _thread import *
import threading 
import time
import app_pb2
from client import SmartRoomClient

def listen_mensage(client):
    mensage =client.read_mensage()
    if mensage.object_name=='LIST OBJECTS':
        print(f"({mensage.object_name}):{mensage.list_object}")
    if mensage.object_name=='EXISTS':
        if mensage.exists ==1:
            print(f"(Server): Objeto encontrado")
        if mensage.exists ==0:
            print(f"(Server): Objeto nao encontrado")
    else:
        print(f"({mensage.object_name}):{mensage.object_result}")
    return mensage
        
def send_mensage(client):
    print("Send Mensage:")
    while True:
        request_mensage = app_pb2.Request_APP()

        print("APP MENU:")
        print("Type /LIST to see all objects names")    
        print("Type the object name to interact with a object")
        command = input('')
        
        if command=='/LIST':
            request_mensage.request_type = app_pb2.Request_APP().RequestType.ListObjects
            client.send_mensage(request_mensage.SerializeToString())
            listen_mensage(client)
        else:
            request_mensage = app_pb2.Request_APP()

            request_mensage.request_type = app_pb2.Request_APP().RequestType.VerifyObject
            request_mensage.value = command
            print(request_mensage.value)
            client.send_mensage(request_mensage.SerializeToString())
            mensage= listen_mensage(client)
            if mensage.exists==1:
                request_mensage.request_type = app_pb2.Request_APP().RequestType.DiscoverComands
                request_mensage.name =command
                client.send_mensage(request_mensage.SerializeToString())
                listen_mensage(client)    
                desire=input('')        
                request= app_pb2.Request_APP()
                if desire=='vol':
                    request.request_type=app_pb2.Request_APP.RequestType.ModStatus
                    request.value = input('Qual o Volume Desejado')
                    request.aux = 'vol'
                if desire=='chanel':
                    request.request_type=app_pb2.Request_APP.RequestType.ModStatus
                    request.value = input('Qual o Canal Desejado')
                    request.aux = 'chanel'
                if desire=='svol':
                    request.request_type=app_pb2.Request_APP.RequestType.ReadStatus
                    request.aux = 'svol'
                if desire=='schnael':
                    request.request_type=app_pb2.Request_APP.RequestType.ReadStatus
                    request.aux = 'schanel'
                if request.request_type=='off':
                    request.request_type=app_pb2.Request_APP.RequestType.ModOnOf
                request.name = command
                client.send_mensage(request.SerializeToString())
                listen_mensage(client)


    
server_ip = '127.0.0.1'
server_port = 65433

client = SmartRoomClient(server_ip,server_port)
print("Conectando com o servidor")

t_1 = threading.Thread(target=send_mensage, args=(client,))
t_2 = threading.Thread(target=listen_mensage, args=(client,))

t_1.start()
#t_2.start()