#!/usr/bin/python
#-*- coding: utf-8 -*-
from Habitacion import Habitacion
class Laberinto():

    def __init__ (self):
        self.habitaciones = []

    def agregarHabitacion(self,hab):
        self.habitaciones.append(hab)

    
    def obtenerHabitacion(self,num):
        return self.habitaciones[num]
