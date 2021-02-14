import socket
import calculadora_pb2 as calc_pb2

class Client():
    def __init__(self,ip_server,server_port):
        self.client_socket= socket.socket(family=socket.AF_INET,
                                          type=socket.SOCK_DGRAM)    
        self.client_socket.connect((ip_server,server_port))
        self.operations = ['+','-','/','*']

       
    def send_mensage(self,x,y,operation):
        request = calc_pb2.RequestCalc()
        request.num_1=float(x)
        request.num_2=float(y)
        request.operation=operation    
                
        self.client_socket.send(request.SerializeToString())
        
        return self.receive_mensage()
    
    def receive_mensage(self):
        response = calc_pb2.ResponseCalc()
        
        mensagem= self.client_socket.recv(1024)
        response.ParseFromString(mensagem)
        return response.value

    
        