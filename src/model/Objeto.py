from abc import ABC


class Objeto(ABC):
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
        
    def usarObjeto(self):
        pass

    def esMoneda(self):
        return False
