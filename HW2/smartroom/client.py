import socket
import app_pb2
class SmartRoomClient():
    def __init__(self,server_ip,server_port):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((server_ip, server_port))
        
    
    def read_mensage(self):
        
        mensagem=self.client_socket.recv(1024)
        response_object =app_pb2.Response_APP()
        response_object.ParseFromString(mensagem)
        return response_object
        
    def send_mensage(self,mensagem):
        self.client_socket.send(mensagem)