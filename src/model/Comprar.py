
from src.model.Comando import Comando


class Comprar(Comando):
    
    def ejecutar(self,alguien):
        alguien.posicion.enteCompraObjeto(alguien,self.receptor)
        alguien.notificar()
    
    def esComprar(self):
        return True
    
    def __str__(self):
        return "Comprar "+str(self.receptor)
      
    def __repr__(self):
        return "Comprar "+str(self.receptor)