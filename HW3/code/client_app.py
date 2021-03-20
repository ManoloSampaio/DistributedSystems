from _thread import *
import threading 
import time
import app_pb2
from client import SmartRoomClient

def listen_message(client):
    message =client.read_message()
    
    if message.response_type==0:    
        print(f"({message.object_name}):{message.object_result}")
        
    elif message.response_type==1:
        print(f"({message.object_name}):{message.on_off_status}\n")
    
    elif message.response_type==2:
        print(f"({message.object_name}):{message.list_object}\n")
    
    elif message.response_type==3:
        print(f"({message.object_name}):{message.object_comands}\n")
    
    return message

def listen_sensor(client,command,request_message):
    global follow
    follow =1
    while follow!=0:    
        time.sleep(3.5)
        request_message.request_type = 1
        request_message.name = command    
        if follow==0:
            break
        client.send_message(request_message.SerializeToString())
        message = listen_message(client)
        

def send_message(client):
    while True:
        request_message = app_pb2.Request_APP()

        print("APP MENU:")
        print("Digite /LIST para ver objetos conectados ao Home Assistant.")    
        print("Digite /SAIR para sair do app.")
        print("Digite o nome do dispositivo para conectar a um dispositivo.\n")
        
        command = input('')
        
        if command=='/LIST':
            request_message.request_type = app_pb2.Request_APP().RequestType.ListObjects
            client.send_message(request_message.SerializeToString())
            listen_message(client)
        
        elif command=='/SAIR':
            request_message.request_type = app_pb2.Request_APP().RequestType.LogOut
            client.send_message(request_message.SerializeToString())
            client.client_socket.close()
            print("Desligando APP")
            break
        
        elif client.discover_atuator(command)==True:
            lista_comandos = client.discover_comands(command)
            print('Comandos: ',lista_comandos)
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
        
        elif client.discover_sensor(command)==True:            
            global follow
            follow =1
            t_2 = threading.Thread(target=listen_sensor, args=(client,command,request_message,))
            t_2.start()
            follow=int(input())

server_ip = '127.0.0.1'
server_port = 65433
client = SmartRoomClient(server_ip,server_port)
print("Conectando com o servidor")

t_1 = threading.Thread(target=send_message, args=(client,))

t_1.start()
