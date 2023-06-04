from src.model.Mochila import Mochila
from src.model.Comando import Comando


class Soltar(Comando):
    
    def ejecutar(self,alguien):
        alguien.inventario.soltarObjeto(self.receptor,alguien)
    
    def esSoltar(self):
        return True
    
    def __str__(self):
        return "Soltar "+str(self.receptor)
      
    def __repr__(self):
        return "Soltar "+str(self.receptor)