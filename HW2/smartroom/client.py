import socket
class SmartRoomClient():
    def __init__(self,server_ip,server_port):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((server_ip, server_port))
        
    
    def rec_mensage(self):
        mensagem=self.client_socket.recv(1024).decode()
        return mensagem
    
    def send_mensage(self,mensagem):
        self.client_socket.send(mensagem)