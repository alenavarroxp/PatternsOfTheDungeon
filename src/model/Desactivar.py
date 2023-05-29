from src.model.Comando import Comando


class Desactivar(Comando):
    
    def ejecutar(self,alguien):
      self.receptor.desactivar(alguien)
      alguien.notificar()
    
    def esDesactivar(self):
        return True
    
    def __str__(self):
       return "Desactivar "+str(self.receptor)
    
    def __repr__(self):
       return "Desactivar "+str(self.receptor)