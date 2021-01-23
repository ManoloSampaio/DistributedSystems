import socket
class CalcClient():
    def __init__(self,ip= '192.168.0.18'):
        self.ip_server = ip
        self.client_socket= socket.socket(family=socket.AF_INET,type=socket.SOCK_DGRAM)    

    def send_mensage(self,mensagen_envio):
        self.client_socket.sendto(mensagen_envio.encode(),(self.ip_server,12000))
        return self.receive_mensage()
    
    def receive_mensage(self):
        mensagen_bytes,ip_servidor = self.client_socket.recvfrom(1024)
        return mensagen_bytes.decode()

    
        