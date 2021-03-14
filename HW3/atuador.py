import pika
import socket
import EnvMsg_pb2
import HAgrpc_pb2_grpc
import HAgrpc_pb2


class Gadgets(HAgrpc_pb2_grpc.ActuatorGRPCServicer):
    def __init__(self,Nome_Dispositivo,ambiente_ip,ambiente_port,grpc_address):
        
        self.ON_OFF =True 
        self.nome = Nome_Dispositivo
        self.socket_atuador = socket.socket(socket.AF_INET, 
                                    socket.SOCK_STREAM)
        
        self.socket_atuador.connect((ambiente_ip,
                                     ambiente_port))
        
        msg = EnvMsg_pb2.FromActuator()
        msg.grpc_address = grpc_address
        msg.object_name = self.nome
        self.socket_atuador.send(msg.SerializeToString())
        
    def TunrnOff(self,request,context):
        self.ON_OFF=False
        msg = HAgrpc_pb2.Response()
        msg.name=self.nome
        msg.result='Is off now'
        return msg
    
    def TunrnOn(self,request,context):
        self.ON_OFF=True
        msg = HAgrpc_pb2.Response()
        msg.name=self.nome
        msg.result='Is on now'
        return msg