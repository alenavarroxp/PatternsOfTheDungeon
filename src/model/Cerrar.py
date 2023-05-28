from src.model.Tienda import Tienda
from src.model.Armario import Armario
from src.model.Baul import Baul
from src.model.Habitacion import Habitacion
from src.model.Comando import Comando


class Cerrar(Comando):
    
    def ejecutar(self,alguien):
      self.receptor.cerrar(alguien)
    
    def esCerrar(self):
        return True
    
    def __str__(self):
        if self.receptor.lado1 is not None and isinstance(self.receptor.lado1,Habitacion):
          return "Cerrar Pt-"+str(self.receptor.lado1.num) + "-"+str(self.receptor.lado2.num)+" (Habitacion)"
        elif isinstance(self.receptor.lado1,Armario):
            return "Cerrar Pt-"+str(self.receptor.lado1.num) + "-"+str(self.receptor.lado2.num)+" (Armario)"
        elif isinstance(self.receptor.lado1,Baul):
            return "Cerrar Pt-"+str(self.receptor.lado1.num) + "-"+str(self.receptor.lado2.num)+" (Baúl)"
        elif isinstance(self.receptor.lado1,Tienda):
            return "Cerrar Pt-"+str(self.receptor.lado1.num) + "-"+str(self.receptor.lado2.num)+" (Tienda)"
        else:
          return "Cerrar Pt-"+str(self.receptor.lado1.num) + "-"+str(self.receptor.lado2.num)
    
    def __repr__(self):
        if self.receptor.lado1 is not None and isinstance(self.receptor.lado1,Habitacion):
          return "Cerrar Pt-"+str(self.receptor.lado1.num) + "-"+str(self.receptor.lado2.num)+" (Habitacion)"
        elif isinstance(self.receptor.lado1,Armario):
            return "Cerrar Pt-"+str(self.receptor.lado1.num) + "-"+str(self.receptor.lado2.num)+" (Armario)"
        elif isinstance(self.receptor.lado1,Baul):
            return "Cerrar Pt-"+str(self.receptor.lado1.num) + "-"+str(self.receptor.lado2.num)+" (Baúl)"
        elif isinstance(self.receptor.lado1,Tienda):
            return "Cerrar Pt-"+str(self.receptor.lado1.num) + "-"+str(self.receptor.lado2.num)+" (Tienda)"
        else:
          return "Cerrar Pt-"+str(self.receptor.lado1.num) + "-"+str(self.receptor.lado2.num)