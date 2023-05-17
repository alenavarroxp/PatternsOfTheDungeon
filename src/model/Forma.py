class Forma():
    def __init__(self):
        self.orientaciones = []
        self.puntoX = 0
        self.puntoY = 0
        self.extentX = 0 
        self.extentY = 0

    def obtenerComandos(self):
        lista = []
        for orientacion in self.orientaciones:
            lista.extend(orientacion.obtenerComandosDe(self))
        return lista
    
    def aceptar(self,unVisitor):
        for orientacion in self.orientaciones:
            orientacion.aceptarEn(unVisitor,self)

    def calcularPosicion(self):
        for orientacion in self.orientaciones:
            orientacion.calcularPosicionDesde(self)

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