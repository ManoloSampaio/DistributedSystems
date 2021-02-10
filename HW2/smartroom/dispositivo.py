import socket
import gateway_pb2
import struct
class Gadgets():
    def __init__(self,ip_multicast,port_multicast,Nome_Dispositivo,server_ip,server_port):
        MCAST_GRP = ip_multicast
        MCAST_PORT = port_multicast
        
        self.multicastsocket = socket.socket(socket.AF_INET, 
                                           socket.SOCK_DGRAM)

        self.multicastsocket.setsockopt(
                                      socket.SOL_SOCKET, 
                                      socket.SO_REUSEADDR,1
                                      )
        
        self.cast_adress = (MCAST_GRP,
                            MCAST_PORT)
        print(self.cast_adress)
        self.server_address = ('',MCAST_PORT)
        self.multicastsocket.bind(self.server_address)
        group = socket.inet_aton(MCAST_GRP)
        mreq = struct.pack('4sL', group, socket.INADDR_ANY)
        self.multicastsocket.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP,mreq)
        self.ON_OFF ='ON' 
        self.nome = Nome_Dispositivo
        #self.client_socket.connect((server_ip, server_port))
    
    def turnon(self):
        self.ON_OFF='ON'
    
    def turnoff(self):
        self.ON_OFF='OFF'
    
    def indent(self):
        response = gateway_pb2.MulticasRequest()
        response.object_name = self.nome
        response.ip = self.ip
        response.port =self.port
        self.multicastsockt.sendto(response,self.cast_adress)
    
    def recieve_gateway(self,mensagem):
        multicast_request= gateway_pb2.MulticastRequest()
        multicast_request.ParseFromString(mensagem)
        if multicast_request.nome=='server':
            print("Entrei aqui")
            self.indent()
    
    