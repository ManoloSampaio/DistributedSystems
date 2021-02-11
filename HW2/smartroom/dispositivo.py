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
        
        self.server_address = ('',MCAST_PORT)
        self.multicastsocket.bind(self.server_address)
        group = socket.inet_aton(MCAST_GRP)
        mreq = struct.pack('4sL', group, socket.INADDR_ANY)
        self.multicastsocket.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP,mreq)
        self.ON_OFF ='OFF' 
        self.nome = Nome_Dispositivo
        self.server_ip = 'localhost'
        self.server_port = server_port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        
    def turnon(self):
        self.ON_OFF='ON'
    
    def turnoff(self):
        self.ON_OFF='OFF'
    
    def indent(self):
        response = gateway_pb2.MulticastRequest()
        response.nome = self.nome
        response.ip =   self.server_ip
        response.port = self.server_port
        self.socket.connect((self.server_ip, self.server_port))
        print(response)
        self.socket.send(response.SerializeToString())
    
    def recieve_gateway(self,mensagem):
        if self.ON_OFF=='OFF':
            mensagem = self.multicastsocket.recv(1024)
            print(mensagem)
            response = gateway_pb2.MulticastRequest()
            response.ParseFromString(mensagem)
            if response.nome=='server':
                self.ON_OFF='ON'
                self.indent()
        
            