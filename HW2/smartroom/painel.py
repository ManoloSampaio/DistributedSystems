from dispositivo import Gadgets
import gateway_pb2
class Painel(Gadgets):
    def __init__(self,ip_multicast,port_multicast,
                       Nome_Dispositivo,server_ip,server_port):
        super().__init__(ip_multicast,port_multicast,
                       Nome_Dispositivo,server_ip,server_port)
        self.mensagem_lamp = 'Bem Vindo'        
    
    def receive_mensage(self):
        response = gateway_pb2.GadgetsResponse()
        request = gateway_pb2.GatewayRequest()
        request.ParseFromString(self.socket.recv(1024))
        
        if self.ON_OFF:
            if request.request_type ==2:
               self.mensagem_lamp = request.value
               response.result = f'Mensagem atual: {self.mensagem_lamp}'
            if request.request_type==0:
                response.result = f'Mensagem atual: {self.mensagem_lamp}'
            if request.request_type == 3:
                self.ON_OFF = False
                response.result =f'{self.nome} esta off' 
        
            if request.request_type == 4:
                response.result = ' Trocar mensagem: Digite msg, Ver mensagem: Digite smsg, Desligar: Digite off'
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