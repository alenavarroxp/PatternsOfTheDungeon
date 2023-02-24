#!/usr/bin/python
#-*- coding: utf-8 -*-


from ElementoMapa import ElementoMapa
from Model.Contenedor import Contenedor

class Habitacion(Contenedor):
    
    def __init__(self):
      pass
        
    def entrar(self):
        print('Estas en la habitación: ',self.num)
    
    def esHabitacion(self):
        return True

