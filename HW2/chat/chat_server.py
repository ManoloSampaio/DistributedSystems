import json
import socket
from _thread import *

class ChatServer():
    """
    Server Class. This class is related to the Server of the chat app.
    It contains the methods to send receive mensages and also list the users.
    """
    def __init__(self):
        """
        Initialization of the server,
        1. Server_socket is the socket of the server.
        2. Connection_vector is the vector that 
        contains the sockets associated with each different client. 
        """
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connection_vector = []
        self.nicknames = []
        
    def send_mensage(self,mensagem):
        """
        Methods associated with send the mensage
        for all clients.
        Args:
            mensagem (encoded string): 
        """
        for connection in self.connection_vector:
            connection.send(mensagem)
    
    def list_nicknames(self,connection):
        """
        List the nicknames for the user that asks for it.

        Returns:
            [type]: [description]
        """
        connection.send(json.dumps(
                        {'mensagem':str(self.nicknames),
                        'nickname':'Server'}
                        ).encode())
    
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
    
    def verify_mensage(self,connection,mensagem):
        """[summary]

        Args:
            connection ([type]): [description]
            mensagem ([type]): [description]

        Returns:
            [type]: [description]
        """
        msg=eval(mensagem.decode())['mensagem']
        
        if msg=='/USUARIOS':
            self.list_nicknames(connection)
            return 0
        
        if msg=='/SAIR':
            connection.send(json.dumps({
                            'mensagem':'Você foi desconectado da sala de chat',
                            'nickname':'Server'}).encode())
            
            nickname = self.remove_user(connection)
            
            self.send_mensage(json.dumps({
                                'mensagem':f'{nickname} saiu do chat',
                                'nickname':'Server'}).encode())
            return 2
        
        return 1
             
    