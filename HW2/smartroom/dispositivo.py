import socket
import gateway_pb2
import struct
class Gadgets():
    def __init__(self,ip_multicast,port_multicast,Nome_Dispositivo,server_ip,server_port):
        MCAST_GRP = ip_multicast
        MCAST_PORT = port_multicast
        self.multicastsocket = socket.socket(socket.AF_INET, 
                                           socket.SOCK_DGRAM)
        self.cast_adress = (MCAST_GRP,
                            MCAST_PORT)
        self.multicastsocket.bind(('',MCAST_PORT))
        group = socket.inet_aton(MCAST_GRP)
        mreq = struct.pack('4sL', group, socket.INADDR_ANY)
        self.multicastsocket.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP,mreq)
        
        
        self.ON_OFF ='ON' 
        self.nome = Nome_Dispositivo
        self.server_ip = 'localhost'
        self.server_port = server_port
        
        self.socket = socket.socket(socket.AF_INET, 
                                    socket.SOCK_STREAM)
        try:
            self.TCPConnect()
        except:
            self.MulticastConnect()
        
    def TCPConnect(self):
        self.socket.connect((self.server_ip, self.server_port))
        response = gateway_pb2.GadgetsIdent()
        response.nome = self.nome
        response.ip =   self.server_ip
        response.port = self.server_port
        
        self.socket.send(response.SerializeToString())
    
    def MulticastConnect(self):
        connection_message = self.multicastsocket.recv(1024)
        message = gateway_pb2.GatewayRequest()
        message.ParseFromString(connection_message)
        self.socket.connect((self.server_ip, self.server_port))
        
        response = gateway_pb2.GadgetsIdent()
        response.nome = self.nome
        response.ip =   self.server_ip
        response.port = self.server_port
        
        self.socket.send(response.SerializeToString())
        
            