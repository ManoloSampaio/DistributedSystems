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
            self.umidade=self.umidade+0.5*msg.variable
            
        if msg.type==1:
            if self.temperatura<msg.variable:
                self.temperatura=self.temperatura+0.5
            if self.temperatura>msg.variable:
                self.temperatura=self.temperatura-0.5
        
        if msg.type==2:
            if msg.value>0:
                self.luminosidade=self.luminosidade+msg.variable
            if msg.value<0:
                self.luminosidade=self.luminosidade-msg.variable
        
        
    def variacaoTemperatura(self):
        self.temperatura=(self.temperatura_equilibrio*0.1
                          +self.temperatura*0.9)
    
    def variacaoUmidade(self):
        self.umidade=(self.umidade_equilibrio*0.1
                      +self.umidade*0.9)
        
    def sendumid(self):
        if len(self.sensor_dict['0'])!=0:    
            for sensor in self.umidade_sensors:
                msg=EnvMsg_pb2.ToSensor()
                msg.variable = self.umidade
                sensor.send(msg.SerializeToString())
                
                
    def sendtemp(self):
        if len(self.sensor_dict['1'])!=0:
            for sensor in self.temp_sensors:
                msg=EnvMsg_pb2.ToSensor()
                msg.variable = self.temperatura
                sensor.send(msg.SerializeToString())

    def sendlum(self):
        if len(self.sensor_dict['2'])!=0:
            for sensor in self.lum_sensor:
                msg=EnvMsg_pb2.ToSensor()
                msg.variable = self.luminosidade
                sensor.send(msg.SerializeToString())