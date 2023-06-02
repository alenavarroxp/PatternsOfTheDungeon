from src.model.Tunel import Tunel
from src.model.Tienda import Tienda
from src.model.Armario import Armario
from src.model.Baul import Baul
from src.model.Habitacion import Habitacion
from src.model.Comando import Comando


class Entrar(Comando):
    
    def ejecutar(self,alguien):
        self.receptor.entrar(alguien)
        alguien.notificar()
    
    def esEntrar(self):
        return True
    
    def __str__(self):
        if not isinstance(self.receptor,Tunel):
            if self.receptor.lado1 is not None and isinstance(self.receptor.lado1,Habitacion):
                return "Entrar Pt-"+str(self.receptor.lado1.num) + "-"+str(self.receptor.lado2.num)+" (Habitacion)"
            elif isinstance(self.receptor.lado1,Armario):
                return "Entrar Pt-"+str(self.receptor.lado1.num) + "-"+str(self.receptor.lado2.num)+" (Armario)"
            elif isinstance(self.receptor.lado1,Baul):
                return "Entrar Pt-"+str(self.receptor.lado1.num) + "-"+str(self.receptor.lado2.num)+" (Baúl)"
            elif isinstance(self.receptor.lado1,Tienda):
                return "Entrar Pt-"+str(self.receptor.lado1.num) + "-"+str(self.receptor.lado2.num)+" (Tienda)"
            else:
                return "Entrar Pt-"+str(self.receptor.lado1.num) + "-"+str(self.receptor.lado2.num)
        else:
            return "Entrar "+str(self.receptor)
    
    def __repr__(self):
        if not isinstance(self.receptor,Tunel):
            if self.receptor.lado1 is not None and isinstance(self.receptor.lado1,Habitacion):
                return "Entrar Pt-"+str(self.receptor.lado1.num) + "-"+str(self.receptor.lado2.num)+" (Habitacion)"
            elif isinstance(self.receptor.lado1,Armario):
                return "Entrar Pt-"+str(self.receptor.lado1.num) + "-"+str(self.receptor.lado2.num)+" (Armario)"
            elif isinstance(self.receptor.lado1,Baul):
                return "Entrar Pt-"+str(self.receptor.lado1.num) + "-"+str(self.receptor.lado2.num)+" (Baúl)"
            elif isinstance(self.receptor.lado1,Tienda):
                return "Entrar Pt-"+str(self.receptor.lado1.num) + "-"+str(self.receptor.lado2.num)+" (Tienda)"
            else:
                return "Entrar Pt-"+str(self.receptor.lado1.num) + "-"+str(self.receptor.lado2.num)
        else:
            return "Entrar "+str(self.receptor)