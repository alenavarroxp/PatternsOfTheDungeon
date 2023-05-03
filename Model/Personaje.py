from model.Ente import Ente

class Personaje(Ente):
    def __init__(self):
        super().__init__()
        self.nickname = None
    
    def __str__(self):
        return f"Personaje:\n\t Nickname: {self.nickname}\n\t Vidas: {self.vidas}\n\t Poder: {self.poder}\n\t Posicion:[\n\t{self.posicion}]\n\t " 