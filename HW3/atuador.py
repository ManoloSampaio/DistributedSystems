import pika
import socket
import EnvMsg_pb2
import HAgrpc_pb2_grpc
import HAgrpc_pb2
import grpc
import concurrent.futures

class Gadgets(HAgrpc_pb2_grpc.ActuatorGRPCServicer):
    def __init__(self,Nome_Dispositivo,ambiente_ip,ambiente_port,comands,grpc_port):
        
        self.ON_OFF =True 
        self.nome = Nome_Dispositivo
        self.socket_atuador = socket.socket(socket.AF_INET, 
                                    socket.SOCK_STREAM)
        
        self.socket_atuador.connect((ambiente_ip,
                                     ambiente_port))
        
        self.comand_list =comands
        server = grpc.server(concurrent.futures.ThreadPoolExecutor(max_workers=10))
        HAgrpc_pb2_grpc.add_ActuatorGRPCServicer_to_server(
                                HAgrpc_pb2_grpc.ActuatorGRPCServicer(), server)
        server.add_insecure_port(f'localhost:{grpc_port}')
        msg = EnvMsg_pb2.FromActuator()
        msg.grpc_address = f'localhost:{grpc_port}'
        self.socket_atuador.send(msg.SerializeToString())
        server.start()
    
    def TunrnOff(request):
        self.ON_OFF=False
        msg = HAgrpc_pb2.Response()
        msg.name=self.nome
        msg.result='Is off now'
        return msg
    
    def TunrnOn(request):
        self.ON_OFF=True
        msg = HAgrpc_pb2.Response()
        msg.name=self.nome
        msg.result='Is on now'
        return msg
    
    def SeeComands(request):
        if self.ON_OFF:
            msg = HAgrpc_pb2.Response()
            msg.name=self.nome
            msg.result='Lista de comandos'
            msg.object_comands = self.comand_list
        
        else:
            msg = HAgrpc_pb2.Response()
            msg.name=self.nome
            msg.result='The Actuator is off'
        
        return msg