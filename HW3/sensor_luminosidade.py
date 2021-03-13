import json
import socket
from _thread import *
import threading
import time

class sensor_luminosidade():
	def __init__(self,ip_ambiente,porta_ambiente):
		self.ambiente_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.ambiente_socket.connect((ip_ambiente,porta_ambiente))
		self.luminosidade=0

def receber_mensagem(sensor_luminosidade):
	while 1:
		print(2)
		mensagem=sensor_luminosidade.ambiente_socket.recv(1024).decode()
		if mensagem[0]=='pedido aceito':
			sensor_luminosidade.luminosidade=mensagem[1]
			print(mensagem[1])


def enviar_mensagem(sensor_luminosidade):
	while 1:
		sensor_luminosidade.ambiente_socket.send(json.dumps(['sensor','luminosidade']).encode())


ip_ambiente = '127.0.0.1'
porta_ambiente = 65433
sensor_luminosidade=sensor_luminosidade(ip_ambiente,porta_ambiente)

t_1 = threading.Thread(target=receber_mensagem, args=(sensor_luminosidade,))

t_2 = threading.Thread(target=enviar_mensagem, args=(sensor_luminosidade,))


t_2.start()


t_1.start()

