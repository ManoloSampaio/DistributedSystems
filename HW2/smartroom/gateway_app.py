from gateway import Gateway
from _thread import *
import threading 
import app_pb2
import gateway_pb2
import time
def add_app_users(gateway):
    while True:
        connection,address=gateway.server_socket_1.accept()
        gateway.client_vectors.append(connection)
        
        print("NEW APP USER ADDRESS:",address)
        
        start_new_thread(listen_app_users,(connection,address))

def listen_app_users(connection,address):
    while True:
        mensagem=connection.recv(1024)
        user_request = app_pb2.Request_APP()
        user_request.ParseFromString(mensagem)
        
        if  user_request.request_type!=4 and user_request.request_type!=6 and user_request.request_type!=1:
            if user_request.request_type==7:
                connection.close()
                break
            
            client_ident = gateway.client_vectors.index(connection)
            gateway.send_to_object(user_request,client_ident)
        
        if user_request.request_type==1:
            server_response = app_pb2.Response_APP()
            if gateway.sensor_value!='NULL':
                server_response.object_name = user_request.name
                server_response.object_result = gateway.sensor_value
                connection.send(server_response.SerializeToString())
            else:
                client_ident = gateway.client_vectors.index(connection)
                gateway.send_to_object(user_request,client_ident)
        
        if user_request.request_type==4:
            server_response = app_pb2.Response_APP()
            server_response.object_name = 'LIST OBJECTS'
            server_response.list_object = str(list(gateway.object_dict.keys()))
            connection.send(server_response.SerializeToString())    
        
        if user_request.request_type==6:
            vector = list(gateway.object_dict.keys())
            if user_request.value not in vector:
                server_response = app_pb2.Response_APP()
                server_response.object_name = 'EXISTS'
                server_response.exists = 0
            else:
                server_response = app_pb2.Response_APP()
                server_response.object_name = 'EXISTS'
                server_response.exists = 1
                
            connection.send(server_response.SerializeToString())
            
def add_gaggets(gateway):
    while True:
        mensagem = gateway_pb2.GadgetsIdent()
        
        connection,address=gateway.server_socket_2.accept()
        
        mensagem.ParseFromString(connection.recv(1024))
        
        print(f'NEW OBJECT ADDRESS:{address}. OBJECT NAME:{mensagem.nome}')
        
        gateway.object_dict[mensagem.nome]=connection   
        
        start_new_thread(listen_gaggets,(connection,))


def listen_gaggets(connection):
    while True:
        mensagem = connection.recv(1024)
        object_response = gateway_pb2.GadgetsResponse()
        object_response.ParseFromString(mensagem)
        
        if object_response.sensor_ident==1:
            gateway.sensor_value = object_response.result
            
        if object_response.sensor_ident==0:    
            i = object_response.client_ident
            connection_app = gateway.client_vectors[i]
            gateway.send_to_user(connection_app,object_response)


gateway = Gateway('228.0.0.8',50000)

gateway.server_socket_2.bind(('127.0.0.1',65432))
gateway.server_socket_2.listen(1)

gateway.server_socket_1.bind(('127.0.0.1',65433))
gateway.server_socket_1.listen(1)

gateway.find()

t_1 = threading.Thread(target = add_gaggets,args=(gateway,))
t_2 = threading.Thread(target = add_app_users,args=(gateway,))

t_1.start() 
t_2.start()