from src.model.Mochila import Mochila
from src.model.Comando import Comando


class Usar(Comando):
    
    def ejecutar(self,alguien):
        if isinstance(self.receptor,Mochila):
            self.receptor.abrirMochila(alguien)
        else:
            self.receptor.usarObjeto(alguien)
            alguien.objetoUsado = self.receptor
        alguien.notificar()
    
    def esUsar(self):
        return True
    
    def __str__(self):
        return "Usar "+str(self.receptor)
      
    def __repr__(self):
        return "Usar "+str(self.receptor)