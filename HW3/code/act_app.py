import time
import grpc
import concurrent.futures
from _thread import *
import threading 
import HAgrpc_pb2_grpc
from atuador import Atuador

def server(obj,grpc_port):
    server = grpc.server(concurrent.futures.ThreadPoolExecutor(max_workers=1))
    HAgrpc_pb2_grpc.add_ActuatorGRPCServicer_to_server(obj, server)
    server.add_insecure_port(f'[::]:{grpc_port}')
    server.start()
    server.wait_for_termination()

def send_data(obj):
    while True:
        time.sleep(2.5)
        obj.send_data()

dict_1 = {1:'Nivel de umidificacao: ',2:'Temperatura desejada: ',3: 'Potencia de iluminacao: '}
dict_2 = {1:['umi','sumi','off'],2:['temp','stemp','off'],3:['light','slight','off']}
comand = int(input('\nDigite 1: Umidificador\nDigite 2: Regulador de Temperatura\nDigite 3: Fornecedor de luz\n'))


try:
    atributo = float(input(f'{dict_1[comand]}'))
    lista_comandos = dict_2[comand]
    grpc_port = (input('Port GRPC: '))
    Nome_Dispositivo = input('Nome Dispositivo: ')
except:
    print('Atributo no identificado')
obj = Atuador(Nome_Dispositivo,'localhost',52000,
              grpc_port,lista_comandos,atributo,comand-1)
    

t_1 = threading.Thread(target = send_data,args=(obj,))      
t_2 = threading.Thread(target = server,args=(obj,grpc_port))

t_1.start()
t_2.start()
