from gateway import Gateway
from _thread import *
import threading 
#import app_pb2
import gateway_pb2

def add_app_users(gateway):
    while True:
        connection,adress=gateway.server_socket_1.accept()
        start_new_thread(listen_app_users,(connection,))

def add_dispositivos(gateway):
    while True:
        object_name,ip,port=gateway.find_dispositivos()
        print(object_name)
        gateway.object_dict[f'{object_name}'],adress=gateway.server_socket_2.connect((ip,port))    
        start_new_thread(listen_object,(gateway.object_dict[f'{object_name}'],))


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
        user_request = app_pb2.Request()
        user_request.ParseFromString(mensagem)
        gateway.send_to_object(user_request)
                

print("Adicionando Users:")
gateway = Gateway('228.0.0.8',60000)

#gateway.server_socket_1.bind(('127.0.0.1',65432))
#gateway.server_socket_1.listen(1)

t_1 = threading.Thread(target = add_dispositivos(gateway))

t_1.start()
            
