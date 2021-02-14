import socket
from calc_client import Client

client = Client('localhost',12000)	
print("UDP Calculadora")

while True:
	
	print('Digite +: para somar dois números: x+y')
	print('Digite -: para subtrair dois números: x-y')  
	print('Digite /: para dividir dois números: x/y')
	print('Digite *: para multiplicar dois números: x*y')
	
	operation = input()
	if operation in client.operations:
		index = client.operations.index(operation)
		x=input("Digite x: ")
		y=input("Digite y: ")
		print(client.send_mensage(x,y,index))
	else:
		print('Operacao nao encontrada')