from ambiente import Ambiente
import time
from _thread import *
import threading
import EnvMsg_pb2

def send_data(ambiente):
    while True:
        time.sleep(2.5)
        ambiente.sendtemp()
        ambiente.sendumid()
        ambiente.sendlum()

def add_sensor(ambiente):
    while True:
        connection,address=ambiente.ambiente_socket_sensor.accept()
        mensagem=connection.recv(1024)
        
        msg = EnvMsg_pb2.FromSensor()
        msg.ParseFromString(mensagem)
        ambiente.sensor_dict[f'{msg.type}'].append(connection)
        communicate_HA(ambiente,msg,1)

def communicate_HA(ambiente,msg,type):
    if type==1:        
        msg_response=EnvMsg_pb2.ToHomeAssitent()
        msg_response.queue_name = msg.queue_name
        msg_response.type =0
        ambiente.ambiente_HA_socket.send(msg_response.SerializeToString())
    
    if type==2:
        msg_response=EnvMsg_pb2.ToHomeAssitent()
        msg_response.grpc_address = msg.grpc_address
        msg_response.type = 1
        ambiente.ambiente_HA_socket.send(msg_response.SerializeToString())
        
def add_atuadores(ambiente):    
    while True:
        connection,address=ambiente.ambiente_socket_atuador.accept()
        mensagem=connection.recv(1024)
        msg = EnvMsg_pb2.FromActuator()
        msg.ParseFromString(mensagem)
        communicate_HA(ambiente,msg,2)
        start_new_thread(listen_atuadores,(ambiente,connection))

def listen_atuadores(ambiente,connection):
    while True:
        ambiente.read_message(connection)

def comportamento_natural(ambiente):
    while True:
        time.sleep(3)
        ambiente.variacaoTemperatura()
        ambiente.variacaoUmidade()
        print(ambiente.temperatura)
        
ambiente=Ambiente('localhost',50000,30,20,50)
ambiente.ambiente_socket_sensor.bind(('localhost',50000))
ambiente.ambiente_socket_sensor.listen(1)

ambiente.ambiente_socket_atuador.bind(('localhost',52000))
ambiente.ambiente_socket_atuador.listen(1)

ambiente.ambiente_HA_socket.connect((('localhost',63000)))

t_1 = threading.Thread(target = send_data,args=(ambiente,))
t_2 = threading.Thread(target = add_sensor,args=(ambiente,))
t_3 = threading.Thread(target = add_atuadores,args=(ambiente,))
t_4 = threading.Thread(target = comportamento_natural,args=(ambiente,))

t_1.start()
t_2.start()
t_3.start()
t_4.start()