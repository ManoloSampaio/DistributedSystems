from _thread import *
import threading 
import time
import app_pb2
from client import SmartRoomClient

def listen_message(client):
    message =client.read_message()
    if message.object_name=='LIST OBJECTS':
        print(f"({message.object_name}):{message.list_object}")
    if message.object_name=='EXISTS':
        if message.exists ==1:
            print(f"(Server): Objeto encontrado")
        if message.exists ==0:
            print(f"(Server): Objeto nao encontrado")
    if message.object_name!='LIST OBJECTS' and message.object_name!='EXISTS':
        print(f"({message.object_name}):{message.object_result}")
    return message
        
def send_message(client):
    while True:
        request_message = app_pb2.Request_APP()

        print("APP MENU:")
        print("Digite /LIST para ver objetos conectados ao gateaway")    
        print("Digite /SAIR para sair do app")
        print("Digite o nome do objeto conectado")
        
        command = input('')
        
        if command=='/LIST':
            request_message.request_type = app_pb2.Request_APP().RequestType.ListObjects
            client.send_message(request_message.SerializeToString())
            listen_message(client)
        
        if command=='/SAIR':
            request_message.request_type = app_pb2.Request_APP().RequestType.LogOut
            client.send_message(request_message.SerializeToString())
            client.client_socket.close()
            print("Desligando APP")
            break
        
        if command!='/SAIR' and command!='/LIST':
            request_message = app_pb2.Request_APP()

            request_message.request_type = app_pb2.Request_APP().RequestType.VerifyObject
            request_message.value = command
            client.send_message(request_message.SerializeToString())
            message= listen_message(client)
            
            if message.exists==1:
                request_message.request_type = app_pb2.Request_APP().RequestType.DiscoverComands
                request_message.name =command
                client.send_message(request_message.SerializeToString())
                listen_message(client)    
                desire=input('Digite Comando: ')        
                request= app_pb2.Request_APP()
                
                if desire=='vol':
                    request.request_type=app_pb2.Request_APP.RequestType.ModStatus
                    request.value = input('Qual o Volume Desejado: ')
                    request.aux = 'vol'
                    request.name = command
                    client.send_message(request.SerializeToString())
                    listen_message(client)
                    
                if desire=='chanel':
                    request.request_type=app_pb2.Request_APP.RequestType.ModStatus
                    request.value = input('Qual o Canal Desejado: ')
                    request.aux = 'chanel'
                    request.name = command
                    client.send_message(request.SerializeToString())
                    listen_message(client)
                    
                if desire=='svol':
                    request.request_type=app_pb2.Request_APP.RequestType.ReadStatus
                    request.aux = 'svol'
                    request.name = command
                    client.send_message(request.SerializeToString())
                    listen_message(client)
                    
                if desire=='schnael':
                    request.request_type=app_pb2.Request_APP.RequestType.ReadStatus
                    request.aux = 'schanel'
                    request.name = command
                    client.send_message(request.SerializeToString())
                    listen_message(client)
                    
                if desire=='off':
                    request.request_type=app_pb2.Request_APP.RequestType.ModOnOf
                    request.name = command
                    client.send_message(request.SerializeToString())
                    listen_message(client)
                
                if desire=='on':
                    request.request_type=app_pb2.Request_APP.RequestType.ModOnOf
                    request.name = command
                    client.send_message(request.SerializeToString())
                    listen_message(client)
                    
                if desire=='sensor':
                    request.request_type=app_pb2.Request_APP.RequestType.ReadSensor
                    request.name = command
                    client.send_message(request.SerializeToString())
                    listen_message(client)
                    
                if desire=='temp':
                    request.request_type=app_pb2.Request_APP.RequestType.ModStatus
                    request.value = input('Qual a temperatura desejada: ')
                    request.aux = desire
                    request.name = command
                    client.send_message(request.SerializeToString())
                    listen_message(client)
                    
                if desire=='sstemp':
                    request.request_type=app_pb2.Request_APP.RequestType.ReadStatus
                    request.aux = desire
                    request.name = command
                    client.send_message(request.SerializeToString())
                    listen_message(client)
                    


    
server_ip = '127.0.0.1'
server_port = 65433

client = SmartRoomClient(server_ip,server_port)
print("Conectando com o servidor")

t_1 = threading.Thread(target=send_message, args=(client,))

t_1.start()
