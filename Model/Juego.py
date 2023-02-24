#!/usr/bin/python
#-*- coding: utf-8 -*-
from Laberinto import Laberinto
from Habitacion import Habitacion
from Pared import Pared
from Puerta import Puerta

class Juego:
    def __init__(self):
        self.laberinto = None
        self.bichos = []

    def agregarBicho(self,unBicho):
        self.bichos.append(unBicho)
        
    def fabricarLaberinto(self):
        return Laberinto()
    
    def fabricarHabitacion(self,num):
        hab = Habitacion(num)
        return hab

    def fabricarPared(self):
        return Pared()
    
    def fabricarPuerta(self,unaHab:Habitacion,otraHab:Habitacion):
        puerta = Puerta()
        puerta.lado1 = unaHab
        puerta.lado2 = otraHab
        return puerta
    
    def obtenerHabitacion(self,num):
        return self.laberinto.obtenerHabitacion(num)

    
    def laberinto2HabitacionesFM(self):
        self.laberinto = self.fabricarLaberinto()
        hab1 = self.fabricarHabitacion(1)
        hab2 = self.fabricarHabitacion(2)

        puerta = self.fabricarPuerta(hab1,hab2)
        hab1.norte = self.fabricarPared
        hab1.oeste = self.fabricarPared
        hab1.este = self.fabricarPared

        hab2.sur = self.fabricarPared
        hab2.oeste = self.fabricarPared
        hab2.este = self.fabricarPared

        hab1.sur = puerta
        hab2.norte = puerta

        self.laberinto.agregarHabitacion(hab1)
        self.laberinto.agregarHabitacion(hab2)

    def laberinto2Habitaciones(self):
        self.laberinto = Laberinto()
        hab1 = Habitacion(1)
        hab2 = Habitacion(2)
        
        puerta = Puerta()
        puerta.lado1 = hab1
        puerta.lado2 = hab2

        hab1.sur = puerta
        hab2.norte = puerta

        hab1.norte = Pared()
        hab1.este = Pared()
        hab1.oeste = Pared()

        hab2.sur = Pared()
        hab2.este = Pared()
        hab2.oeste = Pared()

        self.laberinto.agregarHabitacion(hab1)
        self.laberinto.agregarHabitacion(hab2)

  

juego = Juego()
juego.laberinto2Habitaciones()
juego.laberinto

