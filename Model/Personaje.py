from model.Ente import Ente
from model.Muerto import Muerto

class Personaje(Ente):
    def __init__(self):
        super().__init__()
        self.nickname = None
    
    def heMuerto(self):
        self.estado = Muerto()
        self.juego.personajeMuere()
    
    def buscarEnemigo(self):
        return self.juego.buscarBicho()
    
    def __str__(self):
        return f"\n\t Nickname: {self.nickname}\n\t Vidas: {self.vidas}\n\t Poder: {self.poder}\n\t Posicion:[\n\t{self.posicion}]\n\t " 