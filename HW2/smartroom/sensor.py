from dispositivo import Gadgets
class Lampada(Gadgets):
    def __init__(self):
        super().__init__(ip_multicast,port_multicast,
                       Nome_Dispositivo,server_ip,server_port)
        
        self.temperature_sensor = 25    
    
    def receive_mensage(self):
        response = gateway_pb2.GadgetsResponse()
        request = gateway_pb2.GatewayRequest()
        request.ParseFromString(self.socket.recv(1024))
        
        
        if request.request_type == 3:
            self.ON_OFF = False
            response.result =f'{self.nome} esta off' 
        
        if request.request_type == 4:
            response.result = ' Desligar: Digite off'
        
        response.name = self.nome
        response.status = self.ON_OFF
        response.sensor_ident = 0
        
        self.socket.send(response.SerializeToString())