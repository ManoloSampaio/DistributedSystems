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
        print(self.cast_address)
        aux = ('',MCAST_PORT)
        self.multicastsocket.bind(aux)
        
        self.client_dict = {}
        self.object_dict = {}
                
        self.server_socket_1 = socket.socket(socket.AF_INET, 
                                             socket.SOCK_STREAM)
        
        self.server_socket_2 = socket.socket(socket.AF_INET, 
                                             socket.SOCK_STREAM)
    
    def send_to_object(self,mensagem,adress):
        server_request = gateway_pb2.Request()
        connection = self.object_dict[f'{mensagem.nome}']
        server_request.rtype = mensagem.rtype
        server_request.status = mensagem.status_modification
        server_request.ip = adress[0]
        server_request.port = adress[1]

        connection.send(server_request.SerializeToString())
           
    def send_to_user(self,connection,mensagem):
        server_response = app_pb2.Response_APP()
        server_response.object_name = mensagem.nome
        server_response.object_result = mensagem.result
        connection.send(server_response.SerializeToString()) 
        

    def find_dispositivos(self):
        mensage = gateway_pb2.MulticastRequest()
        mensage.nome = 'server'
        for i in range(0,2):
            self.multicastsocket.sendto(mensage.SerializeToString(), 
                                   self.cast_address)