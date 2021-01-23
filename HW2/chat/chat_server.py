from chat_sala import ChatRoom
class ChatServer():
    def __init__(self):
        self.server_room = ChatRoom()
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.listen(1)
    def receber_client(self):
        connection, client_address = self.server_socket.accept()
    def receber_mensagem(self):
        connection, client_address = self.server_socket.accept()
    def enviar_mensage(self):