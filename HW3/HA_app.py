from gateway import Gateway
from _thread import *
import threading 
import pika
import grpc

import HAgrpc_pb2
import HAgrpc_pb2_grpc
import EnvMsg_pb2
import HAmsg_pb2
import app_pb2

def add_app_users(HA):
    while True:
        connection,address=HA.server_socket_1.accept()
        HA.client_vector.append(connection)
        start_new_thread(listen_app_users,(connection,address))

def listen_app_users(connection,address):
    while True:
        messagem=connection.recv(1024)
        user_request = app_pb2.Request_APP()
        user_request.ParseFromString(messagem)
        
        if user_request.request_type<5:
            if user_request.name in list(HA.object_dict.keys()):
                
                if user_request.request_type==0:
                    stub=HAgrpc_pb2_grpc.ActuatorGRPCStub(
                         HA.object_dict[user_request.name])
                    request = HAgrpc_pb2.Request(value=user_request.value) 
                    response=SeeStatus(request)
                    
                if user_request.request_type==1:
                    response = app_pb2.Response_APP()
                    response.object_name = user_request.name
                    response.object_result = HA.sensor_dict[user_request.name]
                    connection.send(response.SerializeToString())
                
                if user_request.request_type==2:
                    stub=HAgrpc_pb2_grpc.ActuatorGRPCStub(HA.object_dict[user_request.name])
                    request = HAgrpc_pb2.Request(value=user_request.value) 
                    response=stub.ModStatus(request)
                            
                if user_request.request_type==3:
                    stub=HAgrpc_pb2_grpc.ActuatorGRPCStub(HA.object_dict[user_request.name])
                    request = HAgrpc_pb2.Request(value=user_request.value) 
                    response=stub.TunrnOff(request)
                    
                    
                if user_request.request_type==4:   
                    stub=HAgrpc_pb2_grpc.ActuatorGRPCStub(HA.object_dict[user_request.name])
                    request = HAgrpc_pb2.Request(value=user_request.value) 
                    response=stub.TunrnOn(request)
            else:
                server_response = app_pb2.Response_APP()
                server_response.object_name = 'NOT EXISTS'
                server_response.exists = 0
        
        if user_request.request_type==5:
            server_response = app_pb2.Response_APP()
            server_response.object_name = 'LIST OBJECTS'
            server_response.list_object = str(list(HA.object_dict.keys()))
            connection.send(server_response.SerializeToString())
                    
        if user_request.request_type==7:
            HA.remove_user(connection)
            connection.close()
            break    

def add_object(connection):
    while True:
        msg_response=EnvMsg_pb2.ToHomeAssitent()
        msg = connection.recv(1024)
        msg_response.ParseFromString(msg)
        if msg_response.type==0:
            connection_rabbit = pika.BlockingConnection(
                                pika.ConnectionParameters(
                                host='localhost'))
            channel = connection_rabbit.channel()
            HA.object_dict[msg_response.queue_name]=channel
            print(list(HA.object_dict.keys()))
            HA.sensor_dict[f'{msg_response.queue_name}']='NULL'
            start_new_thread(listen_sensor,
                            (channel,
                            msg_response.queue_name,HA,))
        if msg_response.type==1:
            print(msg_response.grpc_address)
            channel = grpc.insecure_channel('localhost:50051',
                      options=(('grpc.enable_http_proxy', 0),))
            HA.object_dict[msg_response.object_name]=channel 

def listen_sensor(channel,queue_name,HA):
    while True:
        
        channel.basic_consume(
                queue_name, 
                lambda ch, method, properties, body: HA.callback_sensor(ch, method, properties, body,queue=queue_name), 
                auto_ack=True
                )
        channel.start_consuming()
        
        


HA =Gateway()

HA.server_socket_1.bind(('localhost',65433))
HA.server_socket_1.listen(1)

HA.server_socket_2.bind(('localhost',40000))
HA.server_socket_2.listen(1)

connection,address=HA.server_socket_2.accept()

t_1 = threading.Thread(target = add_object,args=(connection,))
t_2 = threading.Thread(target = add_app_users,args=(HA,))

t_1.start()
t_2.start() 
