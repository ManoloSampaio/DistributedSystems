from chat_client import ChatClient
from _thread import *
import threading 
import time

def listen_mensage(client):
    while True:
        mensage =client.rec_mensage()
        print("User: "+eval(mensage)['nickname']+" Mensagem: "+eval(mensage)['mensagem'])
        if eval(mensage)['mensagem']=='SAIU':
            break
    
def send_mensage(client):
    while True:    
        mensagem=input('')
        client.send_mensage(mensagem)
        if mensagem=='/SAIR':
            break

nickname =input('Digite o seu nickname: ')
server_ip = '127.0.0.1'
server_port = 65432
client = ChatClient(nickname,server_ip,server_port)
#start_new_thread(listen_mensage,(client,))

print("Conectando com o servidor")

t_1 = threading.Thread(target=send_mensage, args=(client,))
t_2 = threading.Thread(target=listen_mensage, args=(client,))

t_1.start()

t_2.start()

    


    
    
       
    