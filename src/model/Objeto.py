from abc import ABC
from src.model.ElementoMapa import ElementoMapa


class Objeto(ElementoMapa, ABC):
    def __init__(self):
        self.precio = 0
        self.comandos = []

    def agregarComando(self,unComando,puerta):
        self.comandos.append(unComando)
        unComando.receptor = puerta
    
    def quitarComando(self,unComando):
        self.comandos.remove(unComando)

    def obtenerComandos(self,alguien):
        return self.comandos
        
    def usarObjeto(self,alguien):
        pass

    def esMoneda(self):
        return False
    
    def esMochila(self):
        return False
    
    def esEspada(self):
        return False
