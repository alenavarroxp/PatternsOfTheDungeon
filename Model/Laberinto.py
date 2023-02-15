#!/usr/bin/python
#-*- coding: utf-8 -*-
from Habitacion import Habitacion
class Laberinto(Habitacion):
    def _init_(self):
        self.habitaciones = list()
    def agregarHabitacion(self,hab):
        self.habitaciones.append(hab)
    "Hacer bien obtenerHabitacion"
    def obtenerHabitacion(self,num):
        return self.habitaciones(num)