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
        if self.IsWorking():
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
                self.ON_OFF = False
                response.result =f'{self.nome} esta OFF' 
        
            if request.request_type == 4:
                response.result = '\n Mudar Volume: Digite vol \n Mudar canal: digite chanel \n Ver volume: digite svol \n Ver Canal: digite schanel \n Desligar: Type off'
                
                response.object_comands[:] =['vol','chanel','svol','schanel','off']
        else:
            response.result=f'{self.nome} em standby, para usar digite on'
            response.object_comands[:] =['on']
            if request.request_type == 3:
                self.ON_OFF = True
                response.result =f'{self.nome} esta ON'
                
        response.name = self.nome
        response.object_status = self.ON_OFF
        response.sensor_ident = 0
        
        self.socket.send(response.SerializeToString())
        
