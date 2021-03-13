from atuador import Gadgets
import EnvMsg_pb2
class ArCodicionado(Gadgets):
    
    def __init__(self,Nome_Dispositivo,server_ip,server_port,grpc_port):
        super().__init__(Nome_Dispositivo,server_ip,server_port,
                         ['temp','sstemp','sensor','off'],grpc_port)
        
        self.temperature_set = 20
    
    def send_temperature(self):
        if self.ON_OFF==True:
            msg = EnvMsg_pb2.FromActuator()
            msg.type = 1
            msg.variable = self.temperature_set
            self.socket_atuador.send(msg.SerializeToString())

    def receive_message(self):
        response = gateway_pb2.GadgetsResponse()
        request = gateway_pb2.GatewayRequest()
        request.ParseFromString(self.socket.recv(1024))
        
        if self.IsWorking():
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
                self.ON_OFF=False
                response.result =f'{self.nome} Esta: OFF'
                
            if request.request_type == 4:
                response.result = '\n Modifique Temperatura: Digite temp \n Modifique Temperatura: Digite sstemp \n Veja Temperatura da sala: Digite sensor \n Desligue o Ar: Digite off'
                response.object_comands[:] =['temp','sstemp','sensor','off']
        else:
            response.result=f'{self.nome} em standby, para usar digite on'
            response.object_comands[:] =['on']
            if request.request_type == 3:
                self.ON_OFF=True
                response.result =f'{self.nome} Esta: ON'
        
        response.name = self.nome
        response.object_status = self.ON_OFF
        response.sensor_ident = 0
        response.client_ident=request.client_ident
        
        self.socket.send(response.SerializeToString())