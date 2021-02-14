from calcserver import Server

calc = Server('localhost',12000)

print("Servidor escutando")

while True:
    
    message,client_address= calc.listen_user()
    response = calc.operation(message)
    calc.send_message(response,client_address)



    
    

    