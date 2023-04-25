#!/usr/bin/python
#-*- coding: utf-8 -*-

from Contenedor import Contenedor

class Habitacion(Contenedor):
    
    def __init__(self, num):
        super().__init__(num)
        
    def entrar(self):
        print('Estas en la habitación: ',self.num)

    def entrar(self,alguien):
        print('Bicho entra en la habitación: ',self.num) #puedo poner alguien en vez de 'Bicho'
    
    def esHabitacion(self):
        return True
    
    def ponerEnElemento(self, unaOrientacion, unEM):
        unaOrientacion.ponerElemento(unEM, self)

    def __str__(self):
        return f"Habitacion {self.num}:\n\t Norte:{self.norte}\n\t Sur:{self.sur}\n\t Este:{self.este}\n\t Oeste:{self.oeste}\n\t {super().__str__()}"