from src.model.Comando import Comando


class Cerrar(Comando):
    
    def ejecutar(self,alguien):
      self.receptor.cerrar(alguien)
    
    def esCerrar(self):
        return True
    
    def __str__(self):
       return "Cerrar Pt-"+str(self.receptor.lado1.num) + "-"+str(self.receptor.lado2.num)
    
    def __repr__(self):
       return "Cerrar Pt-"+str(self.receptor.lado1.num) + "-"+str(self.receptor.lado2.num)