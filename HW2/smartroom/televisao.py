from dispositivo import Gadgets

class Televisao(Gadgets):
    
    def __init__(self):
        super.__init__()
        self.canal = 0
        self.volume = 0
    
    def set_volume(self,volume):
        self.volume = self.volume+1
        return self.volume
    
    def set_canal(self,canal_number):
        self.canal = canal_number
    
    def see_canal(self):
        return self.canal
    