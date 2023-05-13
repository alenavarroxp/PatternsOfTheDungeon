from abc import ABC


class Objeto(ABC):
    def __init__(self):
        self.precio = 0
        
    def usarObjeto(self):
        pass

    def esMoneda(self):
        return False
