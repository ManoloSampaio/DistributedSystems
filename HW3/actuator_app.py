from lamp import Lampada
from umidificador import Umidificador
from arcon import ArCodicionado
import time
import grpc
import concurrent.futures
from _thread import *
import threading 
import HAgrpc_pb2_grpc


def Server(obj,grpc_port):
    server = grpc.server(concurrent.futures.ThreadPoolExecutor(max_workers=10))
    HAgrpc_pb2_grpc.add_ActuatorGRPCServicer_to_server(obj, server)
    server.add_insecure_port(f'[::]:{port}')
    server.start()
    server.wait_for_termination()

def send_data(obj):
    while True:
        time.sleep(3)
        obj.send_data()


comand = str(input('Which kind of actuator do you want to use:\n1: Ilumination\n2:Umidificador\n3:Temperature Regulator'))
grpc_port = str(input('Port Grpc'))
Nome_Dispositivo = input('Nome Dispositivo')

if command  == 1:
    lamp_value = float(input('Initial value for light power'))    
    obj = Lampada(Nome_Dispositivo,lamp_value,'localhost',52000,grpc_port)
if command == 2:
    umi_value = float(input('Initial value for umi'))
    obj = Umidificador(Nome_Dispositivo,umi_value,'localhost',52000,grpc_port)
if command == 3:
    temp = float(input('Initial Temperature Set'))
    obj = Umidificador(Nome_Dispositivo,temp,'localhost',52000,grpc_port)

try:
    t_1 = threading.Thread(target = send_data,args=(obj,))      
    t_2 = threading.Thread(target = Server,args=(obj,grpc_port))

    t_1.start()
    t_2.start()

except:
    print("Alguma Falha")