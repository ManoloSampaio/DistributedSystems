from dispositivo import Gadgets
class Lampada(Gadgets):
    def __init__(self):
        super().__init__()
        
        self.brilho = 0
        self.cor_dict = {'0':'branca','1':'vermelha',
                         '2':'azul','3':'green'}
        self.color='branca'
    
    def select_color(self,cor_code):
        self.color =self.color_dict[cor_code]
    
    def define_brilho(self,brilho_set):
        self.brilho = brilho_set