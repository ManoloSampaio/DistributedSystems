import socket
import struct
import sys
import gateway_pb2

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
        
        self.cast_adress = (MCAST_GRP,
                            MCAST_PORT)
        
        self.gaggets_vector = []
        self.gaggets_ip = []
                
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    def get_status(self,gtype):
        mensagem=gateway_pb2.Request()
        mensage.gtype = gtype
        mensage.rtype = gateway_pb2.Request().RequestType().ReadStatus
        self.multicastsocket.send(mensagem.SerializeToString())
        gagget_response = self.multicastsocket.recv(1024)
        
    def set_status(self,gtype):
            
    def find_dispositivos(self):
        mensage = json.dumps({'mensagem':'IDENTIFIQUE',
                               'origin':'Server'}).encode()
        
        self.multicastsockt.sendto(message, 
                                   self.cast_adress)
    
    def recieve_dispositivos(self):
        mensage = self.multicastsock.recv(1024).decode()
        
        mensage = eval(mensagem)
        tipo = mensage['tipo']
        ip   = mensage['ip']
        port = mensage['port']
        
        self.gaggets_vector.append(tipo)
        self.gaggets_ip.append((ip,port))

    def 