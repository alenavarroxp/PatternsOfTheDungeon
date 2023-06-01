from src.model.Comando import Comando


class Usar(Comando):
    
    def ejecutar(self,alguien):
        self.receptor.usarObjeto(alguien)
        alguien.notificar()
    
    def esUsar(self):
        return True
    
    def __str__(self):
        return "Usar "+str(self.receptor)
      
    def __repr__(self):
        return "Usar "+str(self.receptor)