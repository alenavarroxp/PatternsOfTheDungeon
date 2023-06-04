from src.model.Objeto import Objeto


class Mochila(Objeto):
    def __init__(self):
        #Aproximación de flyweight para reducir el uso de memoria
        super().__init__()
        self.objetos = []

    def esMochila(self):
        return True

    def aceptar(self, unVisitor):
        unVisitor.visitarMochila(self)

    def agregarObjeto(self, objeto):
        if objeto not in self.objetos:
            objeto.mochila = self
            self.objetos.append(objeto)

    def quitarObjeto(self, objeto):
        if objeto in self.objetos:
                self.objetos.remove(objeto)

    def abrirMochila(self,alguien):
        print("Abriendo mochila...")
        for objeto in self.objetos[:]:
            self.quitarObjeto(objeto)
            alguien.inventario.agregarObjeto(objeto)
            
            
        
       

    def recorrer(self,unBloque):
        print('Recorriendo mochila')

    def __str__(self):
        if len(self.objetos) == 0:
            return f"Mochila vacía {self.precio}€"
        return f"Mochila cargada {self.precio}€"
    
    def __repr__(self):
        if len(self.objetos) == 0:
            return f"Mochila vacía {self.precio}€"
        return f"Mochila cargada {self.precio}€"
