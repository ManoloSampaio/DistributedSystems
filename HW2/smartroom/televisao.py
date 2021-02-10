from dispositivo import Gadgets

class Televisao(Gadgets):
    
    def __init__(self,ip_multicast,port_multicast,
                       Nome_Dispositivo,server_ip,server_port):
        super().__init__(ip_multicast,port_multicast,
                       Nome_Dispositivo,server_ip,server_port)
        self.canal = 0
        self.volume = 0
    
    def set_volume(self,volume):
        self.volume = self.volume+volume
        return self.volume
    
    def set_canal(self,canal_number):
        self.canal = canal_number
    
    def see_canal(self):
        return self.canal
    