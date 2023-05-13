from src.model.Inventario import Inventario
from src.model.Ente import Ente
from src.model.Mochila import Mochila
from src.model.Muerto import Muerto

class Personaje(Ente):
    def __init__(self):
        super().__init__()
        self.nickname = None
        self.inventario = Inventario()
        self.dinero = 0

    def cogerObjeto(self,objeto):
        self.inventario.agregarObjeto(objeto)
    
    def soltarObjeto(self,objeto):
        self.inventario.quitarObjeto(objeto)

    def abrirInventario(self):
        self.inventario.abrirInventario()
    
    def heMuerto(self):
        self.estado = Muerto()
        self.juego.personajeMuere()
    
    def buscarEnemigo(self):
        return self.juego.buscarBicho()
    
    def __str__(self):
        return f"\n\t Nickname: {self.nickname}\n\t Vidas: {self.vidas}\n\t Poder: {self.poder}\n\t Dinero: {self.dinero}\n\t Posicion:[\n\t{self.posicion}]\n\t {self.inventario}\n\t" 