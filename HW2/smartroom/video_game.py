from dispositivo import Gadgets
class VideoGame(Gadgets):
    def __init__(self):
        super.__init__()
        self.ligado = False
        self.jogo = 'Nenhum'
        
    def definir_jogo(self,jogo_para_jogar):
        self.jogo = jogo_para_jogar
    