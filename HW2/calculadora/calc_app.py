import socket
from calc_client import CalcClient

calc = CalcClient()	
print("UDP Calc Manolo")

while True:
	print('Digite 1: para somar dois números: x+y')
	print('Digite 2: para subtrair dois números: x-y')  
	print('Digite 3: para dividir dois números: x/y')
	print('Digite 4: para multiplicar dois números: x*y')

	number = input()
	calc.send_mensage(f'{number}')
	x=input("Digite x: ")
	y=input("Digite y: ")
	print(calc.send_mensage(f'{x},{y}'))

	
  
	