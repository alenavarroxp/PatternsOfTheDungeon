from src.model.Comando import Comando


class Abrir(Comando):
    
    def ejecutar(self,alguien):
      self.receptor.abrir(alguien)
    
    def esAbrir(self):
        return True
    
    def __str__(self):
       return "Abrir Pt-"+str(self.receptor.lado1.num) + "-"+str(self.receptor.lado2.num)
    
    def __repr__(self):
       return "Abrir Pt-"+str(self.receptor.lado1.num) + "-"+str(self.receptor.lado2.num)