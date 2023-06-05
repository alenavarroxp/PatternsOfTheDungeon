from src.model.Brujo import Brujo
from src.model.Mago import Mago
from src.model.Ente import Ente
from src.model.Muerto import Muerto


class Hechicero(Ente):
    def __init__(self):
        super().__init__()
    
    def esEnemigo(self):
        return True

    def conjura(self):
        self.estado.conjura(self)

    def buscarEnemigo(self):
        return self.juego.buscarPersonaje(self)
    
    def estaVivo(self):
        return self.estado.estaVivo()
    
    def heMuerto(self):
        self.estado = Muerto()
        print(self, " ha muerto")
        if isinstance(self.modohechicero,Brujo):
            self.juego.muereHechicero(self)
       

    def puedeConjurar(self):
        self.modohechicero.conjura(self)

    def quitarVidas(self, num):
        self.vidas -= num

    def irA(self, unaOrientacion):
        unaOrientacion.ir(self)

    def obtenerOrientacionAleatoria(self):
        return self.posicion.obtenerOrientacionAleatoria()
    
    def esMago(self):
        return self.modohechicero.esMago()

    def esBrujo(self):
        return self.modohechicero.esBrujo()
    
    def __str__(self):
        return f"Hechicero {self.modohechicero}:\n\t Vidas: {self.vidas}\n\t Poder: {self.poder}\n\t Posicion:[\n\t{self.posicion}]"

    