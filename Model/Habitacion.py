#!/usr/bin/python
#-*- coding: utf-8 -*-

from model.Contenedor import Contenedor
from model.Cuadrado import Cuadrado

class Habitacion(Contenedor):
    
    def __init__(self, num):
        super().__init__(num)
        self.forma = Cuadrado()

    def aceptar(self,unVisitor):
        unVisitor.visitarHabitacion(self)
        for hijo in self.hijos:
            hijo.aceptar(unVisitor)
        self.forma.aceptar(unVisitor)

    def entrar(self):
        print('Estas en la habitación: ',self.num)

    def entrar(self,alguien):
        alguien.posicion = self
        print(alguien,' entra en la habitación: ',self.num)
    
    def esHabitacion(self):
        return True
    

    def __str__(self):
        return f"Habitacion {self.num}:\n\t Norte:{self.forma.norte}\n\t Sur:{self.forma.sur}\n\t Este:{self.forma.este}\n\t Oeste:{self.forma.oeste}\n\t {super().__str__()}"