from chat_client import ChatClient

while(True):
    input_mensage = input('Digite /ENTRAR para entrar no chat')
    if input_mensage=='/ENTRAR':
       nick_name =input('Digite o seu nickname')
       server_ip = input('Digite o IP do server')
       server_port = input('Digite a porta')
       client = ChatClient(nickname,server_ip,server_port)
    