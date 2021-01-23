class Calculadora():
    def __init__(self):
        self.server= socket.socket(family=socket.AF_INET,type=socket.SOCK_DGRAM)   
        self.server.bind(('',12000))
        self.ip_client ='0'
    
    def recieve_numbers(self):
        mensagen_bytes,ip_client = server.recvfrom(1024)
        mensagem = mensagen_bytes.decode()
        self.ip_client = ip_client
        number_list = mensagem.split(',')
        x = int(number_list[0])
        y = int(number_list[1])
        return x,y
    def recieve_operation(self):
        mensagen_bytes,ip_client = server.recvfrom(1024)
        mensagem = mensagen_bytes.decode()
        self.server.sendto(''.encode(),ip_client)
        return int(mensagem)
    
    def soma(self):
        x,y = self.recieve_numbers()
        number = x+y
        mensagen_envio = f"{x}+{y}: "+str(f'{number}')
        self.server.sendto(mensagen_envio.encode(),self.ip_client)
    
    def subtracao(self):
        x,y=self.recieve_numbers()      
        number = x-y
        mensagen_envio = f"{x}-{y}: "+str(f'{number}')
        self.server.sendto(mensagen_envio.encode(),self.ip_client)
    
    def divisao(self):
        x,y=self.recieve_numbers() 
        number = x/y      
        mensagen_envio = f"{x}/{y}: "+str(f'{number}')
        self.server.sendto(mensagen_envio.encode(),self.ip_client)
    
    def multiplicacao(self):
        x,y = self.recieve_numbers()
        number = x*y      
        mensagen_envio = f"{x}*{y}: "+str(f'{number}')
        self.server.sendto(mensagen_envio.encode(),self.ip_client)
        
    