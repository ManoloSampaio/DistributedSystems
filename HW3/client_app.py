from _thread import *
import threading 
import time
import app_pb2
from client import SmartRoomClient

def listen_message(client):
    message =client.read_message()
    
    if message.object_name=='LIST OBJECTS':
        print(f"({message.object_name}):{message.list_object}")
    
    if message.object_name!='LIST OBJECTS' and message.object_name!='EXISTS':
        
        print(f"({message.object_name}):{message.object_result}")
    
    return message
        
def send_message(client):
    while True:
        request_message = app_pb2.Request_APP()

        print("APP MENU:")
        print("Digite /LIST para ver objetos conectados ao gateaway.")    
        print("Digite /SAIR para sair do app.")
        print("Digite o name do objeto: ")
        
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
        
        if command!='/SAIR' and command!='/LIST' and client.discover_atuator(command)==True:
            lista_comandos = client.discover_comands(command)
            print(lista_comandos)
            comando = input('Digite o comando: ')
            request_message = app_pb2.Request_APP()
            if comando in lista_comandos:
                
                if comando=='umi':
                    
                    request_message.value = float(input('Digite a umidade: '))
                    request_message.request_type = 2
                    request_message.name = command
                    request_message.aux = comando
                    
                if comando=='temp':
                    request_message.value = float(input('Digite a temperatura: '))
                    request_message.request_type = 2
                    request_message.name = command
                    request_message.aux = comando
                    
                if comando=='light':
                    request_message.value = float(input('Digite a potencia iluminacao: '))
                    request_message.request_type = 2
                    request_message.name = command
                    request_message.aux = comando
                    
                if comando in ['sumi','stemp','slight']:
                    request_message.aux = comando
                    request_message.request_type = 0
                    request_message.name = command
                
                if comando=='off':
                    request_message.aux = 'OFF'
                    request_message.request_type = 3
                    request_message.name = command
                
                if comando=='on':
                    request_message.aux = 'ON'
                    request_message.request_type = 3
                    request_message.name = command
                
                client.send_message(request_message.SerializeToString())
                message = listen_message(client)                
        elif command!='/SAIR' and command!='/LIST' and client.discover_sensor(command)==True:            
                request_message.request_type = 1
                request_message.name = command

server_ip = '127.0.0.1'
server_port = 65433

client = SmartRoomClient(server_ip,server_port)
print("Conectando com o servidor")

t_1 = threading.Thread(target=send_message, args=(client,))

t_1.start()
