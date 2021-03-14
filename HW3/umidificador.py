from atuador import Gadgets
import EnvMsg_pb2
import HAgrpc_pb2
class Umidificador(Gadgets):
    
    def __init__(self,Nome_Dispositivo,umi_value,server_ip,server_port,grpc_port):
        super().__init__(Nome_Dispositivo,server_ip,server_port,grpc_port)
        self.umitificador_set = umi_value
    
    def send_data(self):
        if self.ON_OFF==True:
            msg = EnvMsg_pb2.FromActuator()
            msg.type = 1
            msg.variable = self.umitificador_set
            self.socket_atuador.send(msg.SerializeToString())
    
    def ModStatus(self,request,context):
        self.temperature_set = request.value
        msg = HAgrpc_pb2.Response()
        msg.name=self.nome
        msg.result=f'{self.umitificador_set}'
        return msg