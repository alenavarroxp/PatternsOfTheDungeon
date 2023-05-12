from src.model.Objeto import Objeto


class Mochila(Objeto):
    def __init__(self):
        #Aproximación de flyweight para reducir el uso de memoria
        self.objetos = []

    def agregarObjeto(self, objeto):
        if objeto not in self.objetos:
            objeto.mochila = self
            self.objetos.append(objeto)

    def quitarObjeto(self, objeto):
        if objeto in self.objetos:
            objeto.contador -= 1
            if objeto.contador == 0:
                self.objetos.remove(objeto)

    def abrirMochila(self):
        print("Abriendo mochila...")
        for objeto in self.objetos:
            objeto.usarObjeto()
        

    def __str__(self):
        if len(self.objetos) == 0:
            return "Mochila vacía"
        return f"Mochila: [{self.objetos}]"
