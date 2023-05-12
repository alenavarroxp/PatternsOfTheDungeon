from src.model.Comando import Comando


class Abrir(Comando):
    
    def ejecutar(self,alguien):
      self.receptor.abrir(alguien)
    
    def esAbrir(self):
        return True
    
    def __str__(self):
       return "Abrir"
    
    def __repr__(self):
       return "Abrir"