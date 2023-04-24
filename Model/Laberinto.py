#!/usr/bin/python
#-*- coding: utf-8 -*-
from Contenedor import Contenedor
class Laberinto(Contenedor):

    def __init__ (self):
        super().__init__(0)
        self.habitaciones = []

    def agregarHabitacion(self,hab):
        self.habitaciones.append(hab)

    def obtenerHabitacion(self,num):
        return self.habitaciones[num]
    
    def __str__(self):
        cadena = f"Laberinto con {len(self.habitaciones)} habitaciones\n"
        for hab in self.habitaciones:
            cadena += f"  {hab}\n"

        return cadena
    
    def recorrer(self,unBloque):
        print('Recorriendo el laberinto')
        for habitacion in self.habitaciones:
            habitacion.recorrer(unBloque)