from calcserver import Server

calc = Server('localhost',12000)

print("Servidor escutando")

while True:
    
    message,client_address= calc.listen_user()
    response = calc.operation(message)
    print(response)
    calc.send_mensage(response,client_address)
    