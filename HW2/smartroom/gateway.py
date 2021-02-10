import socket
import struct
import sys
import gateway_pb2
#import app_pb2
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
        print(self.cast_address)
        self.multicastsocket.bind(self.cast_address)
        
        self.client_dict = {}
        self.object_dict = {}
                
        self.server_socket_1 = socket.socket(socket.AF_INET, 
                                             socket.SOCK_STREAM)
        
        self.server_socket_2 = socket.socket(socket.AF_INET, 
                                             socket.SOCK_STREAM)
    
    def send_to_object(self,mensagem):
        server_request = gateway_pb2.Request()
        connection = self.mensagem.object_dict[f'{mensagem.object_name}']
        server_request.rtype = mensagem.rtype
        server_request.value = mensagem.value
        server_request.ip = mensagem.ip
        server_request.port = mensagem.port

        connection.send(server_request)
           
    def send_to_user(self,connection,mensagem):
        server_response = app_pb2.Response()
        server_response.object_name = mensagem.object_name
        server_response.result = mensagem.result
        connection.send(server_response) 
        

    def find_dispositivos(self):
        mensage = gateway_pb2.MulticastRequest()
        mensage.nome = 'server'
        self.multicastsocket.sendto(mensage.SerializeToString(), 
                                   self.cast_address)
        
        mensage.ParseFromString(self.multicastsocket.recv(1024))
        
        return mensage.object_name,mensage.ip,mensage.port