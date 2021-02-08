from gateway import Gateway
from _thread import *
import threading 
import app_pb2

def add_app_users(gateway):
    while True:
        connection,adress=gateway.server_socket.accept()
        start_new_thread(listen_app_users,(connection,))

def listen_app_users(connection):
    while True:
        mensagem=connection.recv(1024)
        user_request = app_pb2.Request()
        user_request.ParseFromString(mensagem)
        ## User Request has as gtype and rtype
        ## rtype= request type
        ## gtype= which object the user wants to interact



print("Adicionando Users:")
gateway = Gateway('127.0.0.1','60000')

gateway.server_socket.bind(('127.0.0.1',65432))
gateway.server_socket.listen(1)

t_1 = threading.Thread(target = add_app_users(gateway))

t_1.start()
            