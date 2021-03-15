import socket
from _thread import *
import threading 
import time
import EnvMsg_pb2
class Ambiente():
    def __init__(self,server_ip,server_port,temp,lum,umidade):
        self.ambiente_socket_sensor = socket.socket(socket.AF_INET, 
                                           socket.SOCK_STREAM)
        self.ambiente_socket_atuador = socket.socket(socket.AF_INET, 
                                           socket.SOCK_STREAM)
        self.ambiente_HA_socket = socket.socket(socket.AF_INET, 
                                           socket.SOCK_STREAM)
        self.temperatura_equilibrio=25
        self.temperatura=temp
        self.luminosidade=lum
        self.umidade_equilibrio=50
        self.umidade=umidade
        
        self.temp_sensors =[]
        self.umidade_sensors =[]
        self.lum_sensors = [] 
        self.sensor_dict ={'0':self.umidade_sensors,
                           '1':self.temp_sensors,
                           '2':self.lum_sensors}
        self.sensor_queue_name = []
    
    def read_message(self,connection):
        msg = EnvMsg_pb2.FromActuator()
        msg.ParseFromString(connection.recv(1024))
        
        if msg.type==0:
            self.umidade=self.umidade*0.8+0.2*msg.variable
            
        if msg.type==1:
            self.temperatura=self.temperatura*0.9+0.1*msg.variable
        
        if msg.type==2:
            self.luminosidade=msg.variable
        
    def sendumid(self):
        if len(self.sensor_dict['0'])!=0:    
            for sensor in self.sensor_dict['0']:
                msg=EnvMsg_pb2.ToSensor()
                msg.variable = self.umidade
                sensor.send(msg.SerializeToString())
                
                
    def sendtemp(self):
        if len(self.sensor_dict['1'])!=0:
            for sensor in self.sensor_dict['1']:
                msg=EnvMsg_pb2.ToSensor()
                msg.variable = self.temperatura
                sensor.send(msg.SerializeToString())

    def sendlum(self):
        if len(self.sensor_dict['2'])!=0:
            for sensor in self.sensor_dict['2']:
                msg=EnvMsg_pb2.ToSensor()
                msg.variable = self.luminosidade
                sensor.send(msg.SerializeToString())
'''
import json

class Ambiente():
    def __init__(self,server_ip,server_port):
        self.ambiente_socket = socket.socket(socket.AF_INET, 
                                           socket.SOCK_STREAM)
        self.ambiente_socket.bind((server_ip, server_port))
        self.ambiente_socket.listen()
        self.conexoes=[]
        self.TemperaturaEquilibrio=25
        self.Temperatura=0
        self.Luminosidade=0
        self.UmidadeEquilibrio=50
        self.Umidade=0

    def setTemperaturaEquilibrio(self,temperatura):
        self.TemperaturaEquilibrio=temperatura

    def variacaoTemperatura(self):
        self.Temperatura=self.TemperaturaEquilibrio*0.1+self.Temperatura*0.9

    def setLuminosidade(self,luminosidade):
        self.Luminosidade=luminosidade

    def setUmidadeEquilibrio(self,umidadeEquilibrio):
        self.UmidadeEquilibrio=umidadeEquilibrio

    def variacaoUmidade(self):
        self.Umidade=self.UmidadeEquilibrio*0.1+self.Umidade*0.9


def variacaoTemperatura(ambiente):
    while 1:
        ambiente.variacaoTemperatura()
        time.sleep(1)
def variacaoUmidade(ambiente):
    while 1:
        ambiente.variacaoUmidade()
        time.sleep(1)
def add_conexoes(ambiente):
    while 1:
        conexao,addr = ambiente.ambiente_socket.accept()
        if conexao:
            print('Achou')
            ambiente.conexoes.append(conexao)
def listen_request(ambiente):
    while 1:
        for conexao in ambiente.conexoes:
            mensagem=conexao.recv(1024).decode()
            mensagem_vetor=json.loads(mensagem)
            if mensagem[0]=='sensor':
                if mensagem[1]=='temperatura':
                    conexao.send(json.dumps(['pedido aceito',ambiente.Temperatura]).encode())
                if mensagem[1]=='umidade':
                    conexao.send(json.dumps(['pedido aceito',ambiente.Umidade]).encode())
                if mensagem[1]=='luminosidade':
                    conexao.send(json.dumps(['pedido aceito',ambiente.Luminosidade]).encode())
            elif mensagem[0]=='atuador':
                if mensagem[1]=='temperatura':
                    ambiente.setTemperaturaEquilibrio(mensagem[2])
                    conexao.send(json.dumps('Temperatura configurada para ',mensagem[2]).encode())
                if mensagem[1]=='umidade':
                    ambiente.setUmidadeEquilibrio(mensagem[2])
                    conexao.send(json.dumps('Umidade configurada para ',mensagem[2]).encode())
                if mensagem[1]=='luminosidade':
                    ambiente.setLuminosidade(mensagem[2])
                    conexao.send(json.dumps('Luminosidade configurada para ',mensagem[2]).encode())


server_ip = '127.0.0.1'
server_port = 65433

ambiente = Ambiente(server_ip,server_port)

print("Simulação do Ambiente iniciada")

t_1 = threading.Thread(target=variacaoTemperatura, args=(ambiente,))

t_2 = threading.Thread(target=variacaoUmidade, args=(ambiente,))

t_3 = threading.Thread(target=add_conexoes, args=(ambiente,))

t_4 = threading.Thread(target=listen_request, args=(ambiente,))

t_1.start()

t_2.start()

t_3.start()

t_4.start()
>>>>>>> b3c244f6a12da9452e91c20fe3409b925f85120c
'''
