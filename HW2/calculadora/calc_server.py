from calculadora import Calculadora
import socket

calc = Calculadora()
mode = True
server= socket.socket(family=socket.AF_INET,type=socket.SOCK_DGRAM)   
server.bind(('192.168.0.36',12000)) 
while mode:
    print("Servidor escutando")
    mensagen_bytes,ip_client = server.recvfrom(4080)
    mensagem = mensagen_bytes.decode()
    number_list = mensagem.split('+')
    number = int(number_list[0])+int(number_list[1])      
    mensagen_envio = f'{number}'
    print(ip_client)
    server.sendto(mensagen_envio.encode(),(ip_client,12000))
    