import calculadora_pb2 as calc_pb2
import socket

class Server():
    def __init__(self,ip_server,server_port):
        self.serversocket= socket.socket(family=socket.AF_INET,
                                         type=socket.SOCK_DGRAM)   
        self.serversocket.bind((ip_server,server_port))

    
    def listen_user(self):
        message,address = self.serversocket.recvfrom(1024)
        return message,address
    
    
    def operation(self,message):
            
        request = calc_pb2.RequestCalc()
        response = calc_pb2.ResponseCalc()
        
        request.ParseFromString(message)
    
        if request.operation==0:
            response.value = request.num_1+request.num_2
        if request.operation==1:
            response.value = request.num_1-request.num_2
        if request.operation==2:
            response.value = request.num_1/request.num_2
        if request.operation==3:
            response.value = request.num_1*request.num_2
        
        return response.SerializeToString()
    
    def send_message(self,message,client_address):
        self.serversocket.sendto(message,client_address)
        
        
        
        
        
        