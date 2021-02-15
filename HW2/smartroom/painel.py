from dispositivo import Gadgets
import gateway_pb2
class Painel(Gadgets):
    def __init__(self,ip_multicast,port_multicast,
                       Nome_Dispositivo,server_ip,server_port):
        super().__init__(ip_multicast,port_multicast,
                       Nome_Dispositivo,server_ip,server_port)
        
        self.message_lamp = 'Bem Vindo'        
    
    def receive_message(self):
        response = gateway_pb2.GadgetsResponse()
        request = gateway_pb2.GatewayRequest()
        request.ParseFromString(self.socket.recv(1024))
        
        if self.ON_OFF:
            if request.request_type ==2:
               self.messagem_lamp = request.value
               response.result = f'messagem atual: {self.message_lamp}'
            if request.request_type==0:
                response.result = f'messagem atual: {self.message_lamp}'
            if request.request_type == 3:
                self.ON_OFF = False
                response.result =f'{self.nome} esta off' 
        
            if request.request_type == 4:
                response.result = ' Trocar messagem: Digite msg, Ver messagem: Digite smsg, Desligar: Digite off'
                response.object_comands[:] =['msg','smsg','off']
        else:
            response.result=f'{self.nome} em standby, para ativar digite on'
            response.object_comands[:] =['on']
            
            if request.request_type == 3:
                self.ON_OFF=True
                response.result =f'{self.nome} Esta: ON'
        
        response.name = self.nome
        response.object_status = self.ON_OFF
        response.sensor_ident = 0
        response.client_ident=request.client_ident
        
        
        self.socket.send(response.SerializeToString())