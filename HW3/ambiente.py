import socket
from _thread import *
import threading 
import time
class Ambiente():
    def __init__(self,server_ip,server_port):
        #self.client_socket = socket.socket(socket.AF_INET, 
                                           #socket.SOCK_STREAM)
        #self.client_socket.connect((server_ip, server_port))
        self.TemperaturaEquilibrio=25
        self.Temperatura=0
        self.Luminosidade=0
        self.UmidadeEquilibrio=50
        self.Umidade=0
    
    def read_message(self):
        
        message=self.client_socket.recv(1024)
        response =app_pb2.Response_APP()
        response.ParseFromString(message)
        return response
        
    def send_message(self,message):
        self.client_socket.send(message)

    def setTemperaturaEquilibrio(self,temperatura):
        self.TemperaturaEquilibrio=temperatura

    def variacaoTemperatura(self):
        self.Temperatura=self.TemperaturaEquilibrio*0.1+self.Temperatura*0.9

    def getTemperatura(self):
        return self.Temperatura

    def setLuminosidade(self,luminosidade):
        self.Luminosidade=luminosidade

    def getLuminosidade(self):
        return self.Luminosidade

    def setUmidadeEquilibrio(self,umidadeEquilibrio):
        self.UmidadeEquilibrio=umidadeEquilibrio

    def variacaoUmidade(self):
        self.Umidade=self.UmidadeEquilibrio*0.1+self.Umidade*0.9

    def getUmidade(self):
        return self.Umidade


def variacaoTemperatura(ambiente):
    while 1:
        ambiente.variacaoTemperatura()
        time.sleep(1)
def variacaoUmidade(ambiente):
    while 1:
        ambiente.variacaoUmidade()
        time.sleep(1)
def printAtributos(ambiente):
    while 1:
        print("Temperatura = ",ambiente.getTemperatura(),"\nUmidade = ",ambiente.getUmidade(),"\nLuminosidade = ",ambiente.getLuminosidade())
        time.sleep(1)


server_ip = '127.0.0.1'
server_port = 65433

ambiente = Ambiente(server_ip,server_port)

print("Simulação do Ambiente iniciada")

t_1 = threading.Thread(target=variacaoTemperatura, args=(ambiente,))

t_2 = threading.Thread(target=variacaoUmidade, args=(ambiente,))

t_3 = threading.Thread(target=printAtributos, args=(ambiente,))

t_1.start()

t_2.start()

t_3.start()