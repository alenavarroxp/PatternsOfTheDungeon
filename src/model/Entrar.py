from src.model.Comando import Comando


class Entrar(Comando):
    
    def ejecutar(self,alguien):
      self.receptor.entrar(alguien)
    
    def esEntrar(self):
        return True
    
    def __str__(self):
       return "Entrar Pt-"+str(self.receptor.lado1.num) + "-"+str(self.receptor.lado2.num)
    
    def __repr__(self):
       return "Entrar Pt-"+str(self.receptor.lado1.num) + "-"+str(self.receptor.lado2.num)