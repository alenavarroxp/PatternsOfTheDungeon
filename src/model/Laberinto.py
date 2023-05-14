#!/usr/bin/python
#-*- coding: utf-8 -*-
from src.model.Contenedor import Contenedor
class Laberinto(Contenedor):

    def __init__ (self):
        super().__init__(1)
        
    def aceptar(self,unVisitor):
        print("Visitando al laberinto:")
        for hijo in self.hijos:
            hijo.aceptar(unVisitor)
            
    def agregarHabitacion(self,hab):
        self.agregarHijo(hab)

    def obtenerHabitacion(self,num):
        return self.hijos[num-1]
    
    def __str__(self):
        cadena = f"Laberinto con {len(self.hijos)} habitaciones\n"
        for hab in self.hijos:
            cadena += f"  {hab}\n"
        return cadena
    
    def entrar(self,alguien):
        hab1 = self.obtenerHabitacion(1)
        hab1.entrar(alguien)
        
    def recorrer(self,unBloque):
        print('Recorriendo el laberinto:'+str(self.num))
        for habitacion in self.hijos:
            habitacion.recorrer(unBloque)