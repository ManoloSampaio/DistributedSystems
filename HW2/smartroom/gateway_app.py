from gateway import Gateway
from _thread import *
import threading 
import app_pb2
import gateway_pb2
 
def add_app_users(gateway):
    print("Adicionando Users:")
    while True:
        connection,adress=gateway.server_socket_1.accept()
        gateway.client_dict[f'{adress[0]}_{adress[1]}']=connection
        print("USER ADRESS:",adress)
        start_new_thread(listen_app_users,(connection,))

def alert_dipositivos(gateway):
    while True:
        gateway.find_dispositivos()

def add_dispositivos(gateway):
    print("Adicionando Dispositivos")
    mensagem = gateway_pb2.MulticastRequest()
    while True:
        connection,adress=gateway.server_socket_2.accept()
        mensagem.ParseFromString(connection.recv(1024))
        print("OBJECT ADRESS:",adress)
        gateway.object_dict[mensagem.nome]=connection    
        start_new_thread(listen_object,(connection,))       


def listen_object(connection):
    while True:
        mensagem = connection.recv(1024)
        
        object_response = gateway_pb2.Response()
        object_response.ParseFromString(mensagem)
        ip = object_response.ip
        port = object_response.port
        
        for i in range(len(gateway.client_dict.values)):
            if gateway.client_dict.values[i][1]==(ip,port):
                connection_app = gateway.client_dict.values[i]
                gateway.sendo_to_user(connection,object_response)
                
def listen_app_users(connection):
    while True:
        mensagem=connection.recv(1024)
        user_request = app_pb2.Request_APP()
        user_request.ParseFromString(mensagem)
        print(user_request)
        gateway.send_to_object(user_request)
                


gateway = Gateway('228.0.0.8',50000)

gateway.server_socket_2.bind(('127.0.0.1',65432))
gateway.server_socket_2.listen(1)

gateway.server_socket_1.bind(('127.0.0.1',65433))
gateway.server_socket_1.listen(1)

t_1 = threading.Thread(target = alert_dipositivos,args=(gateway,))
t_2 = threading.Thread(target = add_dispositivos,args=(gateway,))
t_3 = threading.Thread(target = add_app_users,args=(gateway,))

t_1.start() 


t_2.start()
   
   
t_3.start()     
