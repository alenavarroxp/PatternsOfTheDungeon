from src.model.Comando import Comando


class Activar(Comando):
    
    def ejecutar(self,alguien):
      self.receptor.activar(alguien)
    
    def esActivar(self):
        return True
    
    def __str__(self):
       return "Activar "+str(self.receptor)
    
    def __repr__(self):
       return "Activar "+str(self.receptor)