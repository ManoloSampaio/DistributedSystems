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
        
    def callback_sensor(self,ch, method, properties, body,queue):
        self.sensor_dict[queue]=float(body.decode('utf-8'))
     