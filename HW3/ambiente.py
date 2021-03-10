import socket
from _thread import *
import threading 
import time
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
            ambiente.conexoes.append(conexao)
def listen_request(ambiente):
    while 1:
        for conexao in ambiente.conexoes:
            mensagem=conexao.recv(1024)
            with conexao:
                mensagem_decodificada=json.loads(mensagem.decode())
                if mensagem_decodificada[0]=='sensor':
                    if mensagem_decodificada[1]=='temperatura':
                        conexao.send(json.dumps(['pedido aceito',ambiente.Temperatura]).encode())
                    if mensagem_decodificada[1]=='umidade':
                        conexao.send(json.dumps(['pedido aceito',ambiente.Umidade]).encode())
                    if mensagem_decodificada[1]=='luminosidade':
                        conexao.send(json.dumps(['pedido aceito',ambiente.Luminosidade]).encode())
                elif mensagem_decodificada[0]=='atuador':
                    if mensagem_decodificada[1]=='temperatura':
                        ambiente.setTemperaturaEquilibrio(mensagem_decodificada[2])
                        conexao.send(json.dumps('Temperatura configurada para ',mensagem_decodificada[2]).encode())
                    if mensagem_decodificada[1]=='umidade':
                        ambiente.setUmidadeEquilibrio(mensagem_decodificada[2])
                        conexao.send(json.dumps('Umidade configurada para ',mensagem_decodificada[2]).encode())
                    if mensagem_decodificada[1]=='luminosidade':
                        ambiente.setLuminosidade(mensagem_decodificada[2])
                        conexao.send(json.dumps('Luminosidade configurada para ',mensagem_decodificada[2]).encode())


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