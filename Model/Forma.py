class Forma():
    def __init__(self):
        self.orientaciones = []
    
    def agregarOrientacion(self,unaOrientacion):
        self.orientaciones.append(unaOrientacion)
    
    def obtenerElemento(self,unaOrientacion):
        return unaOrientacion.obtenerElementoEn(self)
    
    def ponerElementoEn(self,unaOrientacion,unEM):
        unaOrientacion.ponerElemento(unEM,self)

    def recorrer(self,unBloque):
        for orientacion in self.orientaciones:
            orientacion.recorrerEn(unBloque,self)

    def __str__(self):
        return f'Forma: {self.orientaciones}'
    def __repr__(self):
        return f'Forma: {self.orientaciones}'