from calcclient import Client

client = Client('localhost',12000)	
print("UDP Calculadora")

while True:
	
	print('Digite +: para somar dois números: x+y')
	print('Digite -: para subtrair dois números: x-y')  
	print('Digite /: para dividir dois números: x/y')
	print('Digite *: para multiplicar dois números: x*y')
	print("Digite /SAIR para sair")
 
	operation = input()
	
	if operation in client.operations:
		index = client.operations.index(operation)
		x=input("Digite x: ")
		y=input("Digite y: ")
		print(f"{x}{client.operations[index]}{y} = ",
		client.send_message(x,y,index))
	else:
		if operation=='/SAIR':
			break
		else:
			print("Comando nao encontrado")  

