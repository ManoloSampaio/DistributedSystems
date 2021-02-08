import json
import socket
class Gadgets():
    def __init__(self,ip_multicast,port_multicast,tipo):
        MCAST_GRP = 'localhost'
        MCAST_PORT = port
        
        self.multicastsockt = socket.socket(socket.AF_INET, 
                                           socket.SOCK_DGRAM)

        self.multicastsockt.setsockopt(socket.SOL_SOCKET, 
                                      socket.SO_REUSEADDR, 
                                      )
        self.status = True
        self.type = tipo
    
    def turnon(self):
        self.status=True
    
    def turnoff(self):
        self.status=False
    
    def send_identification_information(self):
        mensagem = {'tipo':self.type,'ip':self.ip,
                    'port':self.port}
        
        self.multicastsockt.sendto(json.dumps(mensagem).encode())
    
    def recieve_gateway(self,mensage):
        mensagem_dict = eval(mensage)
        if mensagem_dict['tipo']=='gateway':
            send_identification_information()
    
    