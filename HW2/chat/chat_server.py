#from chat_sala import ChatRoom
import json
import socket
from _thread import *

class ChatServer():
    """[summary]
    """
    def __init__(self):
        """
        
        """
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connection_vector = []
        self.nicknames = []
        
    def send_mensage(self,mensagem):
        """[summary]

        Args:
            mensagem ([type]): [description]
        """
        for connection in self.connection_vector:
            connection.send(mensagem)
    
    def list_nicknames(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        return self.nicknames
    
    def remove_user(self,connection_user):
        """[summary]

        Args:
            connection_user ([type]): [description]

        Returns:
            [type]: [description]
        """
        for i in range(len(self.connection_vector)):
            if self.connection_vector[i]==connection_user:
                self.connection_vector.pop(i)
                nickname = self.nicknames.pop(i)
                return nickname
    
    def verify_mensage(connection,mensagem):
        """[summary]

        Args:
            connection ([type]): [description]
            mensagem ([type]): [description]

        Returns:
            [type]: [description]
        """
        msg=eval(mensagem.decode())['mensagem']
        if msg=='/USUARIOS':
            connection.send(json.dumps({'mensagem':str(server.list_nicknames()),
                            'nickname':'Server'}).encode())
            return 0
        if msg=='/SAIR':
            connection.send(json.dumps({
                                'mensagem':'SAIU',
                                'nickname':'Server'}).encode())
            nickname = self.remove_user(connection)
            print(nickname)
            server.send_mensage(json.dumps({
                                'mensagem':f'{nickname} saiu do chat',
                                'nickname':'Server'}).encode())
            return 2
        
        return 1
             
    