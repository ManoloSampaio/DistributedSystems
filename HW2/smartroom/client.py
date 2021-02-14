import socket
import app_pb2
class SmartRoomClient():
    def __init__(self,server_ip,server_port):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((server_ip, server_port))
        
    
    def read_message(self):
        
        message=self.client_socket.recv(1024)
        response_object =app_pb2.Response_APP()
        response_object.ParseFromString(message)
        return response_object
        
    def send_message(self,message):
        self.client_socket.send(message)