from dispositivo import Gadgets
import gateway_pb2

class ArCodicionado(Gadgets):
    
    def __init__(self,ip_multicast,port_multicast,
                       Nome_Dispositivo,server_ip,server_port):
        super().__init__(ip_multicast,port_multicast,
                       Nome_Dispositivo,server_ip,server_port)
        
        self.temperature_set = 20
        self.temperature_sensor = 25
    
    def change_temperature(self):
        if self.temperature_sensor>self.temperature_set:
            self.temperature_sensor = self.temperature_sensor-0.1
        if self.temperature_sensor<self.temperature_set:
            self.temperature_sensor = self.temperature_sensor+0.1
    
    def receive_mensage(self):
        response = gateway_pb2.GadgetsResponse()
        request = gateway_pb2.GatewayRequest()
        request.ParseFromString(self.socket.recv(1024))
        if request.request_type == 2:
            if request.aux =='temp':
                self.temperature_set = float(request.value)
                response.result =f'Setted Temperature: {self.temperature_set}'
                    
        if request.request_type == 0:
            if request.aux =='sstemp':
                response.result =f'Setted Temperature:{self.temperature_set}'
        
        if request.request_type==1:
            response.result = f'Room Temperature: {self.temperature_sensor}'
        
        if request.request_type == 3:
            self.ON_OFF = 'OFF'
            response.result =f'{self.ON_OFF}' 
        
        if request.request_type == 5:
            response.result = '\n CHANGE Temperature: Type temp \n SEE Set Temperature: Type sstemp \n SEE Room Temperature: Type sensor \n TURN OFF TV: Type off'
        
        response.name = self.nome
        response.sensor_ident = 0
        self.socket.send(response.SerializeToString())