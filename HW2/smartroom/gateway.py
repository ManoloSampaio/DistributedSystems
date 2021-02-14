import socket
import struct
import sys
import gateway_pb2
import app_pb2
class Gateway():
    def __init__(self,ip_multicast,port_multicast):
        MCAST_GRP = ip_multicast
        MCAST_PORT = port_multicast
        
        self.multicastsocket = socket.socket(
                                           socket.AF_INET, 
                                           socket.SOCK_DGRAM
                                           )

        self.multicastsocket.setsockopt(
                                      socket.SOL_SOCKET, 
                                      socket.SO_REUSEADDR,1 
                                      )
        
        self.cast_address = (MCAST_GRP,
                            MCAST_PORT)
        
        self.server_socket_1 = socket.socket(socket.AF_INET, 
                                             socket.SOCK_STREAM)
        
        self.server_socket_2 = socket.socket(socket.AF_INET, 
                                             socket.SOCK_STREAM)

        self.client_vectors = []
        self.object_dict = {}
        self.sensor_value = 'NULL'
    
    def send_to_object(self,mensagem,client_ident):
        server_request = gateway_pb2.GatewayRequest()
        
        connection = self.object_dict[f'{mensagem.name}']
        server_request.aux =mensagem.aux
        server_request.request_type = mensagem.request_type
        server_request.value = mensagem.value
        server_request.client_ident = client_ident

        connection.send(server_request.SerializeToString())

    def send_to_user(self,connection,mensagem):
        server_response = app_pb2.Response_APP()
        server_response.object_name = mensagem.name
        server_response.object_result = mensagem.result
        connection.send(server_response.SerializeToString()) 
        
    def find(self):
        mensage = gateway_pb2.GatewayRequest()
        for i in range(0,2):
            self.multicastsocket.sendto(
                                 mensage.SerializeToString(), 
                                 self.cast_address
                                )