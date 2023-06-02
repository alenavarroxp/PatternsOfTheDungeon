
from src.model.Comando import Comando


class Canjear(Comando):
    
    def ejecutar(self,alguien):
        self.receptor.canjearValor(alguien)
        alguien.notificar()
    
    def esCanjear(self):
        return True
    
    def __str__(self):
        return "Canjear "+str(self.receptor)
      
    def __repr__(self):
        return "Canjear "+str(self.receptor)