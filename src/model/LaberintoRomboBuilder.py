from src.model.Armario import Armario
from src.model.Habitacion import Habitacion
from src.model.Noreste import Noreste
from src.model.Noroeste import Noroeste
from src.model.Rombo import Rombo
from src.model.Sureste import Sureste
from src.model.Suroeste import Suroeste
from src.model.LaberintoBuilder import LaberintoBuilder


class LaberintoRomboBuilder(LaberintoBuilder):
        def __init__(self):
            super().__init__()
        
        def fabricarNoroeste(self):
                return Noroeste()
        
        def fabricarNoreste(self):
                return Noreste()
        
        def fabricarSuroeste(self):
                return Suroeste()
        
        def fabricarSureste(self):
                return Sureste()
        
        def fabricarForma(self):
                return Rombo()
        
        def fabricarArmarioEn(self,unContenedor):
                num = unContenedor.num
                armario = self.fabricarArmario(num)
                armario.forma = self.fabricarForma()

                armario.ponerEnElemento(self.fabricarNoroeste(),self.fabricarPared(armario))
                armario.ponerEnElemento(self.fabricarNoreste(),self.fabricarPared(armario))
                armario.ponerEnElemento(self.fabricarSuroeste(),self.fabricarPared(armario))
                armario.ponerEnElemento(self.fabricarSureste(),self.fabricarPared(armario))
                armario.agregarOrientacion(self.fabricarNoroeste())
                armario.agregarOrientacion(self.fabricarNoreste())
                armario.agregarOrientacion(self.fabricarSuroeste())
                armario.agregarOrientacion(self.fabricarSureste())

                puerta = self.fabricarPuerta(armario,unContenedor)
                armario.ponerEnElemento(self.fabricarNoreste(),puerta)
                unContenedor.agregarHijo(armario)
                return armario
        
        def fabricarHabitacion(self,unNum):
                hab = Habitacion(unNum)
                hab.forma = self.fabricarForma()
                hab.forma.num = unNum
                hab.ponerEnElemento(self.fabricarNoroeste(),self.fabricarPared(hab))
                hab.ponerEnElemento(self.fabricarNoreste(),self.fabricarPared(hab))
                hab.ponerEnElemento(self.fabricarSuroeste(),self.fabricarPared(hab))
                hab.ponerEnElemento(self.fabricarSureste(),self.fabricarPared(hab))

                hab.agregarOrientacion(self.fabricarNoroeste())
                hab.agregarOrientacion(self.fabricarNoreste())
                hab.agregarOrientacion(self.fabricarSuroeste())
                hab.agregarOrientacion(self.fabricarSureste())

                self.laberinto.agregarHabitacion(hab)
                return hab
        