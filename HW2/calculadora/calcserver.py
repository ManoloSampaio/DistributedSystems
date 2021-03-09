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
    
    def soma(self,x,y):
        return x+y
    
    def subtracao(self,x,y):
        return x-y
    
    def divisao(self,x,y):
        return x/y
    
    def multplicacao(self,x,y):
        return x*y
    
    def operation(self,message):
            
        request = calc_pb2.RequestCalc()
        
        
        request.ParseFromString(message)
        
        x = request.num_1
        y = request.num_2
        
        if request.op==0:
            return self.soma(x,y)
        if request.op==1:
            return self.subtracao(x,y)
        if request.op==2:
            return self.divisao(x,y)
        if request.op==3:
            return self.multplicacao(x,y)
        
        
    def create_response(self,message):
        response = calc_pb2.ResponseCalc()
        response.value = self.operation(message)
        return response.SerializeToString()
    
    def send_message(self,message,client_address):
        self.serversocket.sendto(message,client_address)
        
        
        
        
        
        