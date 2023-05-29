from src.model.Comando import Comando


class Coger(Comando):

    def ejecutar(self,alguien):
      alguien.inventario.agregarObjeto(self.receptor)
      for hijo in self.receptor.padre.hijos:
          if hijo == self.receptor:
              self.receptor.padre.hijos.remove(hijo)
              break
      alguien.notificar()
    
    def esCoger(self):
        return True
     
    def __str__(self):
        return "Coger " + str(self.receptor)

    def __repr__(self):
        return "Coger " + str(self.receptor)