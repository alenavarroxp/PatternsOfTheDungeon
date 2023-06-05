from src.model.Inventario import Inventario
from src.model.Ente import Ente
from src.model.Mochila import Mochila
from src.model.Muerto import Muerto

class Personaje(Ente):
    def __init__(self):
        super().__init__()
        self.nickname = None
        self.inventario = Inventario()
        self.dinero = 50
        self.objetoUsado = None

    def esPersonaje(self):
        return True

    def obtenerComandos(self,alguien):
        return self.posicion.obtenerComandos(alguien)
    
    def cogerObjeto(self,objeto):
        self.inventario.agregarObjeto(objeto)
        self.notificar()
    
    def soltarObjeto(self,objeto):
        self.inventario.quitarObjeto(objeto)
        self.notificar()

    def abrirInventario(self):
        self.inventario.abrirInventario()
        self.notificar()
    
    def heMuerto(self):
        self.estado = Muerto()
        self.juego.personajeMuere()
    
    def buscarEnemigo(self):
        return self.juego.buscarBicho()
    
    def buscarBrujo (self):
        return self.juego.buscarBrujo()
    
    def __str__(self):
        return f"\n\t Nickname: {self.nickname}\n\t Vidas: {self.vidas}\n\t Poder: {self.poder}\n\t Dinero: {self.dinero}\n\t Posicion:[\n\t{self.posicion}]\n\t {self.inventario}\n\t" 