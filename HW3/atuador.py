import pika
import socket
import EnvMsg_pb2
import HAgrpc_pb2_grpc
import HAgrpc_pb2


class Atuador(HAgrpc_pb2_grpc.ActuatorGRPCServicer):
    def __init__(self,Nome_Dispositivo,ambiente_ip,ambiente_port,grpc_address,
                 comandos,atributo,type_id):
        
        self.ON_OFF =True 
        self.nome = Nome_Dispositivo
        self.socket_atuador = socket.socket(socket.AF_INET, 
                                    socket.SOCK_STREAM)
        
        self.socket_atuador.connect((ambiente_ip,
                                     ambiente_port))
        
        msg = EnvMsg_pb2.FromActuator()
        msg.grpc_address = grpc_address
        msg.object_name = self.nome
        self.lista_comandos = comandos
        self.atributo_atuacao = atributo
        self.type = type_id
        self.socket_atuador.send(msg.SerializeToString())
    
    def send_data(self):
        if self.ON_OFF==True:
            msg = EnvMsg_pb2.FromActuator()
            msg.type = self.type
            msg.variable = self.atributo_atuacao
            self.socket_atuador.send(msg.SerializeToString())    
    
    
    def TunrnOff(self,request,context):
        self.ON_OFF=False
        msg = HAgrpc_pb2.Response()
        msg.name=self.nome
        msg.on_off_status='OFF'
        return msg
    
    def TunrnOn(self,request,context):
        self.ON_OFF=True
        msg = HAgrpc_pb2.Response()
        msg.name=self.nome
        msg.on_off_status='ON'
        return msg
    
    
    def ModStatus(self,request,context):
        self.atributo_atuacao = request.value
        msg = HAgrpc_pb2.Response()
        msg.name=self.nome
        msg.result=self.atributo_atuacao
        return msg
    
    def SeeComands(self,request,context):
        msg = HAgrpc_pb2.Response()
        if self.ON_OFF==True:
            msg.object_comands[:] = self.lista_comandos
            msg.name  = self.nome 
        else:
            msg.object_comands[:] =['on']
            msg.name  = f'{self.nome} esta desligado' 
        return msg
    
    def SeeStatus(self,request,context):
        msg = HAgrpc_pb2.Response()
        msg.name = self.nome
        msg.result = self.atributo_atuacao
        
        return msg