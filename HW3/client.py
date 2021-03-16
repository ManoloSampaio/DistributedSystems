import socket
import app_pb2
class SmartRoomClient():
    def __init__(self,server_ip,server_port):
        self.client_socket = socket.socket(socket.AF_INET, 
                                           socket.SOCK_STREAM)
        self.client_socket.connect((server_ip, server_port))
        
    
    def read_message(self):
        
        message=self.client_socket.recv(1024)
        response =app_pb2.Response_APP()
        response.ParseFromString(message)
        return response
        
    def send_message(self,message):
        self.client_socket.send(message)
    
    def discover_comands(self,object_name):
        request = app_pb2.Request_APP()
        request.request_type = 4
        request.name = object_name
        
        self.client_socket.send(request.SerializeToString())
        msg = self.client_socket.recv(1024)
        
        mensage = app_pb2.Response_APP()
        mensage.ParseFromString(msg)
        return mensage.object_comands
    
    def discover_atuator(self,object_name):
        request_message = app_pb2.Request_APP()
        request_message.request_type = app_pb2.Request_APP().RequestType.VerifyActuator
        self.send_message(request_message.SerializeToString())
        message =self.read_message()
        
        if object_name in message.list_object:
            return True
        else:
            return False
    
    def discover_sensor(self,object_name):
        request_message = app_pb2.Request_APP()
        request_message.request_type = app_pb2.Request_APP().RequestType.VerifySensor
        self.send_message(request_message.SerializeToString())
        message =self.read_message()
        
        if object_name in message.list_object:
            return True
        else:
            return False