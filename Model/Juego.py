#!/usr/bin/python
#-*- coding: utf-8 -*-
from Laberinto import Laberinto
from Habitacion import Habitacion
from Model.Agresivo import Agresivo
from Model.Armario import Armario
from Model.Bicho import Bicho
from Model.Bomba import Bomba
from Model.Este import Este
from Model.Norte import Norte
from Model.Oeste import Oeste
from Model.Perezoso import Perezoso
from Model.Sur import Sur
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
        hab.ponerEnElemento(self.fabricarNorte(),self.fabricarPared())
        hab.ponerEnElemento(self.fabricarEste(),self.fabricarPared())
        hab.ponerEnElemento(self.fabricarOeste(),self.fabricarPared())
        hab.ponerEnElemento(self.fabricarSur(),self.fabricarPared())
        return hab

    def fabricarArmarioEn(self,unContenedor):
        arm = Armario()
        unNum = unContenedor.hijos.size()
        arm.ponerEnElemento(self.fabricarNorte(),self.fabricarPared())
        arm.ponerEnElemento(self.fabricarEste(),self.fabricarPared())
        arm.ponerEnElemento(self.fabricarOeste(),self.fabricarPared())
        arm.ponerEnElemento(self.fabricarSur(),self.fabricarPared())
        unContenedor.agregarHijo(arm)
    
    def fabricarModoAgresivo(self):
        return Agresivo()
    
    def fabricarBichoAgresivo(self):
        bicho = Bicho()
        bicho.modo = self.fabricarModoAgresivo()
        bicho.vidas = 10
        bicho.poder = 10
        return bicho
    
    def fabricarBichoAgresivoPosicion(self,unaHabitacion):
        bicho = Bicho()
        bicho.modo = self.fabricarModoAgresivo()
        bicho.vidas = 10
        bicho.poder = 10
        bicho.posicion = unaHabitacion
        return bicho
    
    def fabricarModoPerezoso(self):
        return Perezoso()
    
    def fabricarBichoPerezoso(self):
        bicho = Bicho()
        bicho.modo = self.fabricarModoPerezoso()
        bicho.vidas = 10
        bicho.poder = 10
        return bicho
    
    def fabricarBichoPerezosoPosicion(self,unaHabitacion):
        bicho = Bicho()
        bicho.modo = self.fabricarModoAgresivo
        bicho.vidas = 10
        bicho.poder = 10
        bicho.posicion = unaHabitacion
        return bicho
    
    def fabricarBomba(self):
        return Bomba()
    
    def fabricarEste(self):
        return Este()
    
    def fabricarOeste(self):
        return Oeste()
    
    def fabricarSur(self):
        return Sur()
    
    def fabricarNorte(self):
        return Norte()
    
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

    def laberinto4Hab4BichosFM(self):
        self.laberinto = self.fabricarLaberinto()
        hab1 = self.fabricarHabitacion(1)
        hab2 = self.fabricarHabitacion(2)
        hab3 = self.fabricarHabitacion(3)
        hab4 = self.fabricarHabitacion(4)

        puerta12 = self.fabricarPuerta(hab1,hab2)
        puerta13 = self.fabricarPuerta(hab1,hab3)
        puerta24 = self.fabricarPuerta(hab2,hab4)
        puerta34 = self.fabricarPuerta(hab3,hab4)

        hab1.ponerEnElemento(self.fabricarSur(),puerta12)
        hab2.ponerEnElemento(self.fabricarNorte(),puerta12)

        hab1.ponerEnElemento(self.fabricarEste(),puerta13)
        hab3.ponerEnElemento(self.fabricarOeste(),puerta13)

        hab3.ponerEnElemento(self.fabricarSur(),puerta34)
        hab4.ponerEnElemento(self.fabricarNorte(),puerta34)

        hab2.ponerEnElemento(self.fabricarEste(),puerta24)
        hab4.ponerEnElemento(self.fabricarOeste(),puerta24)

        b1 = self.fabricarBichoAgresivoPosicion(hab1)
        b2 = self.fabricarBichoPerezosoPosicion(hab2)
        b3 = self.fabricarBichoAgresivoPosicion(hab3)
        b4 = self.fabricarBichoPerezosoPosicion(hab4)

        self.agregarBicho(b1)
        self.agregarBicho(b2)
        self.agregarBicho(b3)
        self.agregarBicho(b4)

        self.laberinto.agregarHabitacion(hab1)
        self.laberinto.agregarHabitacion(hab2)
        self.laberinto.agregarHabitacion(hab3)
        self.laberinto.agregarHabitacion(hab4)

    def laberinto4Hab4Arm4BichosFM(self):
        self.laberinto = self.fabricarLaberinto()
        hab1 = self.fabricarHabitacion(1)
        hab2 = self.fabricarHabitacion(2)
        hab3 = self.fabricarHabitacion(3)
        hab4 = self.fabricarHabitacion(4)

        #Unica modificacion para añadir 4 armarios al laberinto
        self.fabricarArmarioEn(hab1)
        self.fabricarArmarioEn(hab2)
        self.fabricarArmarioEn(hab3)
        self.fabricarArmarioEn(hab4)

        puerta12 = self.fabricarPuerta(hab1,hab2)
        puerta13 = self.fabricarPuerta(hab1,hab3)
        puerta24 = self.fabricarPuerta(hab2,hab4)
        puerta34 = self.fabricarPuerta(hab3,hab4)

        hab1.ponerEnElemento(self.fabricarSur(),puerta12)
        hab2.ponerEnElemento(self.fabricarNorte(),puerta12)

        hab1.ponerEnElemento(self.fabricarEste(),puerta13)
        hab3.ponerEnElemento(self.fabricarOeste(),puerta13)

        hab3.ponerEnElemento(self.fabricarSur(),puerta34)
        hab4.ponerEnElemento(self.fabricarNorte(),puerta34)

        hab2.ponerEnElemento(self.fabricarEste(),puerta24)
        hab4.ponerEnElemento(self.fabricarOeste(),puerta24)

        b1 = self.fabricarBichoAgresivoPosicion(hab1)
        b2 = self.fabricarBichoPerezosoPosicion(hab2)
        b3 = self.fabricarBichoAgresivoPosicion(hab3)
        b4 = self.fabricarBichoPerezosoPosicion(hab4)

        self.agregarBicho(b1)
        self.agregarBicho(b2)
        self.agregarBicho(b3)
        self.agregarBicho(b4)

        self.laberinto.agregarHabitacion(hab1)
        self.laberinto.agregarHabitacion(hab2)
        self.laberinto.agregarHabitacion(hab3)
        self.laberinto.agregarHabitacion(hab4)
        

juego = Juego()
juego.laberinto2Habitaciones()
juego.laberinto

