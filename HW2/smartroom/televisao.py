from dispositivo import Gadgets
import gateway_pb2

class Television(Gadgets):
    
    def __init__(self,ip_multicast,port_multicast,
                       Nome_Dispositivo,server_ip,server_port):
        
        super().__init__(ip_multicast,port_multicast,
                       Nome_Dispositivo,server_ip,server_port)
        self.chanel = 0
        self.volume = '20'
    
    
    
    def receive_mensage(self):
        response = gateway_pb2.GadgetsResponse()
        request = gateway_pb2.GatewayRequest()
        request.ParseFromString(self.socket.recv(1024))
        
        if request.request_type == 2:
            if request.aux =='vol':
                self.volume = request.value
                response.result =f'VOL: {self.volume}'
            
            if request.aux == 'chanel':
                self.chanel = request.value
                response.result =f'CHANEL: {self.chanel}'
                
        if request.request_type == 0:
            if request.aux =='svol':
                response.result =f'VOL: {self.volume}'
            if request.aux =='schanel':
                response.result =f'CHANEL: {self.chanel}'
        
        if request.request_type == 3:
            self.ON_OFF = 'OFF'
            response.result =f'{self.ON_OFF}' 
        
        if request.request_type == 5:
            response.result = '\n CHANGE VOLUME: Type vol \n CHANGE CHANEL: Type chanel \n SEE VOL: Type svol \n SEE CHANEL: Type schanel \n TURN OFF TV: Type off'
        
        response.name = self.nome
        response.sensor_ident = 0
        self.socket.send(response.SerializeToString())
        
