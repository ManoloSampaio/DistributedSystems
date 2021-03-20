from homeassis import HomeAssistent
from _thread import *
import threading 
import pika
import grpc

import HAgrpc_pb2
import HAgrpc_pb2_grpc
import EnvMsg_pb2
import app_pb2

def add_app_users(HA):
    while True:
        connection,address=HA.server_socket_1.accept()
        start_new_thread(listen_app_users,
                         (connection,address))

def listen_app_users(connection,address):
    while True:
        messagem=connection.recv(1024)
        user_request = app_pb2.Request_APP()
        user_request.ParseFromString(messagem)
        
        if user_request.request_type<5:
            if user_request.name in list(HA.object_dict.keys()):

                if user_request.request_type==0:
                    response = app_pb2.Response_APP()
                    stub=HAgrpc_pb2_grpc.ActuatorGRPCStub(
                         HA.object_dict[user_request.name])
                    request = HAgrpc_pb2.Request() 
                    msg=stub.SeeStatus(request)
                    response.object_name   = msg.name
                    response.object_result = msg.result 
                    connection.send(response.SerializeToString())
                    
                if user_request.request_type==1:
                    response = app_pb2.Response_APP()
                    response.object_name = user_request.name
                    response.object_result = HA.sensor_dict[user_request.name]
                    connection.send(response.SerializeToString())
                    
                if user_request.request_type==2:
                    response = app_pb2.Response_APP()
                    stub=HAgrpc_pb2_grpc.ActuatorGRPCStub(HA.object_dict[user_request.name])
                    request = HAgrpc_pb2.Request(value=user_request.value) 
                    msg=stub.ModStatus(request)
                    
                    response.object_name   = msg.name
                    response.object_result = msg.result 
                    response.response_type =0
                    connection.send(response.SerializeToString())
                            
                if user_request.request_type==3:
                    response = app_pb2.Response_APP()
                    stub=HAgrpc_pb2_grpc.ActuatorGRPCStub(HA.object_dict[user_request.name])
                    request = HAgrpc_pb2.Request() 
                    
                    if user_request.aux=='OFF':
                        msg=stub.TunrnOff(request)
                        response.on_off_status = 'Dispositivo Esta OFF'
                    
                    if user_request.aux=='ON':
                        msg=stub.TunrnOn(request)
                        response.on_off_status = 'Dispositivo Esta ON' 
                    
                    response.object_name   = msg.name
                    response.response_type =1       
                    connection.send(response.SerializeToString())
                
                if user_request.request_type==4:
                   response = app_pb2.Response_APP()
                   stub=HAgrpc_pb2_grpc.ActuatorGRPCStub(HA.object_dict[user_request.name])
                   request = HAgrpc_pb2.Request()
                   msg=stub.SeeComands(request)
                   response.object_name   = user_request.name
                   response.object_comands[:] = msg.object_comands 
                   connection.send(response.SerializeToString())
               
            else:
                server_response = app_pb2.Response_APP()
                server_response.object_name = 'NOT EXISTS'
                server_response.response_type=2
                connection.send(server_response.SerializeToString())
                
        if user_request.request_type==5:
            server_response = app_pb2.Response_APP()
            server_response.object_name = 'LIST OBJECTS'
            server_response.list_object = str(list(HA.object_dict.keys()))
            server_response.response_type=2
            connection.send(server_response.SerializeToString())
        
        if user_request.request_type==6:
            server_response = app_pb2.Response_APP()
            server_response.list_object = str(HA.atuadores)
            connection.send(server_response.SerializeToString())
        
        if user_request.request_type==7:
            server_response = app_pb2.Response_APP()
            server_response.list_object = str(HA.sensores)
            connection.send(server_response.SerializeToString())                
        
        if user_request.request_type==8:
            connection.close()
            break    

def add_object(connection):
    while True:
        msg_response=EnvMsg_pb2.ToHomeAssitent()
        msg = connection.recv(1024)
        msg_response.ParseFromString(msg)
        
        if msg.decode() =='':
           break
        
        if msg_response.type==0:
            connection_rabbit = pika.BlockingConnection(
                                pika.ConnectionParameters(
                                host='localhost'))
            channel = connection_rabbit.channel()
            
            HA.object_dict[msg_response.queue_name]=channel
            HA.sensores.append(msg_response.queue_name)
            HA.sensor_dict[f'{msg_response.queue_name}']='NULL'
            start_new_thread(listen_sensor,
                            (channel,
                            msg_response.queue_name,HA,))
        
        if msg_response.type==1:
            channel = grpc.insecure_channel(f'localhost:{msg_response.grpc_address}')
            
            HA.object_dict[msg_response.object_name]=channel 
            HA.atuadores.append(msg_response.object_name)

def listen_sensor(channel,queue_name,HA):
    while True:
        channel.basic_consume(
                queue_name, 
                lambda ch, method, properties, body: HA.callback_sensor(ch, method, properties, body,
                                                                        queue=queue_name), 
                auto_ack=True
                )
        channel.start_consuming()    
        


HA =HomeAssistent()

HA.server_socket_1.bind(('localhost',65433))
HA.server_socket_1.listen(1)

HA.server_socket_2.bind(('localhost',42000))
HA.server_socket_2.listen(1)

connection,address=HA.server_socket_2.accept()

t_1 = threading.Thread(target = add_object,args=(connection,))
t_2 = threading.Thread(target = add_app_users,args=(HA,))

t_1.start()
t_2.start()