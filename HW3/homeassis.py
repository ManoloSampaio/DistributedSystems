import socket
import struct
import sys
import HAgrpc_pb2
import HAgrpc_pb2_grpc
import app_pb2

class HomeAssistent():
    def __init__(self):
        
        
        self.server_socket_1 = socket.socket(socket.AF_INET, 
                                             socket.SOCK_STREAM)
        
        self.server_socket_2 = socket.socket(socket.AF_INET, 
                                             socket.SOCK_STREAM)

        self.client_vector = []
        self.object_dict = {}
        self.sensor_dict = {}
        self.sensores = []
        self.atuadores= []
        
    def remove_user(self,connection_user):
        for i in range(len(self.client_vector)):
            if self.client_vector[i]==connection_user:
                self.client_vector.pop(i)
    
    def send_to_user(self,connection,message):
        server_response = app_pb2.Response_APP()
        server_response.object_name = message.name
        server_response.object_result = message.result
        server_response.object_status = message.object_status
        if message.object_comands!=[]:
            server_response.object_comands[:] = message.object_comands
        connection.send(server_response.SerializeToString())
        
    def callback_sensor(self,ch, method, properties, body,queue):
        self.sensor_dict[queue]=float(body.decode('utf-8'))
     