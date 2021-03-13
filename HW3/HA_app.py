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

def callback_sensor(ch, method, properties, body):
    print(f'Temperature:{body}')

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
        
        if  user_request.request_type<5 and user_request.request_type!=1:
            client_ident = HA.client_vector.index(connection)
            HA.send_to_object(user_request,client_ident)
        
        if user_request.request_type==7:
            HA.remove_user(connection)
            connection.close()
            break
        
        if user_request.request_type==1:
            server_response = app_pb2.Response_APP()
            if HA.sensor_value!='NULL':
                server_response.object_name = user_request.name
                server_response.object_result = gateway.sensor_value
                connection.send(server_response.SerializeToString())
            else:
                client_ident = gateway.client_vector.index(connection)
                HA.send_to_object(user_request,client_ident)
        
        if user_request.request_type==5:
            server_response = app_pb2.Response_APP()
            server_response.object_name = 'LIST OBJECTS'
            server_response.list_object = str(list(HA.object_dict.keys()))
            connection.send(server_response.SerializeToString())    
        
        if user_request.request_type==6:
            vector = list(HA.object_dict.keys())
            if user_request.value not in vector:
                server_response = app_pb2.Response_APP()
                server_response.object_name = 'EXISTS'
                server_response.exists = 0
            else:
                server_response = app_pb2.Response_APP()
                server_response.object_name = 'EXISTS'
                server_response.exists = 1
                
            connection.send(server_response.SerializeToString())
            
def add_sensor(connection):
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
            start_new_thread(listen_sensor,
                            (channel,
                            msg_response.queue_name,))

def listen_sensor(channel,queue_name):
    while True:
        channel.basic_consume(
                queue=queue_name, 
                on_message_callback=callback_sensor, 
                auto_ack=True
                )
        channel.start_consuming()
        #gateway.sensor_data[f'{queue_name}']=msg.
        
def add_atuadores(connection,HA):
    while True:
        msg = EnvMsg_pb2.ToHomeAssitent()
        msg.ParseFromString(connection.recv(1024))
        if msg.type==1:
            channel = grpc.insecure_channel(msg.grpc_address)
            HA.object_dict[msg.object_name]=channel 


HA =Gateway()

HA.server_socket_1.bind(('localhost',65433))
HA.server_socket_1.listen(1)

HA.server_socket_2.bind(('localhost',63000))
HA.server_socket_2.listen(1)
connection,addres=HA.server_socket_2.accept()

t_1 = threading.Thread(target = add_sensor,args=(connection,))
t_2 = threading.Thread(target = add_atuadores,args=(connection,HA,))
t_3 = threading.Thread(target = add_app_users,args=(HA,))

t_3.start()
t_1.start() 
t_2.start()
