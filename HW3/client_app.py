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
        print("Digite /LIST para ver objetos conectados ao gateaway.")    
        print("Digite /SAIR para sair do app.")
        print("Digite o nome do objeto: ")
        
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
            request_message.name = command
            request_message.request_type=2
            request_message.aux = 'temp'
            request_message.value=input('Qual a temperatura desejada')
            client.send_message(request_message.SerializeToString())
            message = listen_message(client)                

    
server_ip = '127.0.0.1'
server_port = 65433

client = SmartRoomClient(server_ip,server_port)
print("Conectando com o servidor")

t_1 = threading.Thread(target=send_message, args=(client,))

t_1.start()
