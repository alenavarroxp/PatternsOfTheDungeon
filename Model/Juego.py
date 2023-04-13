#!/usr/bin/python
#-*- coding: utf-8 -*-
from Laberinto import Laberinto
from Habitacion import Habitacion
from Agresivo import Agresivo
from Armario import Armario
from Bicho import Bicho
from Bomba import Bomba
from Este import Este
from Norte import Norte
from Oeste import Oeste
from Perezoso import Perezoso
from Sur import Sur
from Pared import Pared
from Puerta import Puerta

class Juego:
    def __init__(self):
        self.laberinto = None
        self.bichos = []
    
    def __str__(self):
        infoBicho = ""
        for bicho in self.bichos:
            infoBicho += f"  {bicho}\n"
        return f"Juego:\n {self.laberinto}\n Hay {len(self.bichos)} bichos en el laberinto:\n {infoBicho}"

    def __repr__(self):
        infoBicho = ""
        for bicho in self.bichos:
            infoBicho += f"  {bicho}\n"
        return f"Juego:\n {self.laberinto}\n Hay {len(self.bichos)} bichos en el laberinto:\n {infoBicho}"

    def agregarBicho(self,unBicho):
        self.bichos.append(unBicho)
    
    def fabricarArmario(self):
        return Armario()
    
    def fabricarArmarioEn(self,unContenedor,num):
        arm = Armario(num)
        arm.ponerEnElemento(self.fabricarNorte(),self.fabricarPared())
        arm.ponerEnElemento(self.fabricarEste(),self.fabricarPared())
        arm.ponerEnElemento(self.fabricarOeste(),self.fabricarPared())
        arm.ponerEnElemento(self.fabricarSur(),self.fabricarPared())
        unContenedor.agregarHijo(arm)

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
     
    def fabricarBichoPerezoso(self):
        bicho = Bicho()
        bicho.modo = self.fabricarModoPerezoso()
        bicho.vidas = 10
        bicho.poder = 10
        return bicho
    
    def fabricarBichoPerezosoPosicion(self,unaHabitacion):
        bicho = Bicho()
        bicho.modo = self.fabricarModoPerezoso()
        bicho.vidas = 10
        bicho.poder = 10
        bicho.posicion = unaHabitacion
        return bicho
    
    def fabricarBomba(self):
        return Bomba()
    
    def fabricarEste(self):
        return Este()
    
    def fabricarHabitacion(self,num):
        hab = Habitacion(num)
        hab.ponerEnElemento(self.fabricarNorte(),self.fabricarPared())
        hab.ponerEnElemento(self.fabricarEste(),self.fabricarPared())
        hab.ponerEnElemento(self.fabricarOeste(),self.fabricarPared())
        hab.ponerEnElemento(self.fabricarSur(),self.fabricarPared())
        return hab
    
    def fabricarLaberinto(self):
        return Laberinto()
    
    def fabricarModoAgresivo(self):
        return Agresivo()
    
    def fabricarModoPerezoso(self):
        return Perezoso()
   
    def fabricarNorte(self):
        return Norte()
 
    def fabricarOeste(self):
        return Oeste()
    
    def fabricarPared(self):
        return Pared()
    
    def fabricarPuerta(self,unaHab:Habitacion,otraHab:Habitacion):
        puerta = Puerta()
        puerta.lado1 = unaHab
        puerta.lado2 = otraHab
        return puerta
    
    def fabricarSur(self):
        return Sur()

    def laberinto2Habitaciones(self):
        
        print("\n--- LABERINTO 2 HABITACIONES --")
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
        print(juego)
        print("------------------------------------------------")


    def laberinto2HabitacionesFM(self):
        print("\n--- LABERINTO 2 HABITACIONES (FACTORY METHOD) --")
        self.laberinto = self.fabricarLaberinto()
        hab1 = self.fabricarHabitacion(1)
        hab2 = self.fabricarHabitacion(2)

        puerta = self.fabricarPuerta(hab1,hab2)
        hab1.norte = self.fabricarPared()
        hab1.oeste = self.fabricarPared()
        hab1.este = self.fabricarPared()

        hab2.sur = self.fabricarPared()
        hab2.oeste = self.fabricarPared()
        hab2.este = self.fabricarPared()

        hab1.sur = puerta
        hab2.norte = puerta

        self.laberinto.agregarHabitacion(hab1)
        self.laberinto.agregarHabitacion(hab2)
        print(juego)
        print("------------------------------------------------")
    
    def laberinto2HabitacionesFMDecorator(self):
        print("\n--- LABERINTO 2 HABITACIONES (FM & DECORATOR) --")
        self.laberinto = self.fabricarLaberinto()
        hab1 = self.fabricarHabitacion(1)
        hab2 = self.fabricarHabitacion(2)
        puerta = self.fabricarPuerta(hab1,hab2)
        bomba1 = self.fabricarBomba()
        bomba1.component = self.fabricarPared()
        bomba2 = self.fabricarBomba()
        bomba2.component = self.fabricarPared()

        hab1.norte = bomba1
        hab1.oeste = self.fabricarPared()
        hab1.este = self.fabricarPared()

        hab2.sur = bomba2
        hab2.oeste = self.fabricarPared()
        hab2.este = self.fabricarPared()

        hab1.sur = puerta
        hab2.norte = puerta

        self.laberinto.agregarHabitacion(hab1)
        self.laberinto.agregarHabitacion(hab2)
        print(juego)
        print("------------------------------------------------")

    def laberinto4Hab4Arm4BichosFM(self):
        print("\n--- LABERINTO 4 HABITACIONES, 4 ARMARIOS y 4 BICHOS --")
        self.laberinto = self.fabricarLaberinto()
        hab1 = self.fabricarHabitacion(1)
        hab2 = self.fabricarHabitacion(2)
        hab3 = self.fabricarHabitacion(3)
        hab4 = self.fabricarHabitacion(4)

        #Unica modificacion para añadir 4 armarios al laberinto
        self.fabricarArmarioEn(hab1,1)
        self.fabricarArmarioEn(hab2,2)
        self.fabricarArmarioEn(hab3,3)
        self.fabricarArmarioEn(hab4,4)

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
        print(juego)
        print("------------------------------------------------")
    
    def laberinto4Hab4Arm4Bombas4BichosFM(self):
        print("\n--- LABERINTO 4 HABITACIONES, 4 ARMARIOS, 4 BOMBAS y 4 BICHOS --")
        self.laberinto = self.fabricarLaberinto()
        hab1 = self.fabricarHabitacion(1)
        hab2 = self.fabricarHabitacion(2)
        hab3 = self.fabricarHabitacion(3)
        hab4 = self.fabricarHabitacion(4)

        #Unica modificacion para añadir 4 armarios al laberinto
        self.fabricarArmarioEn(hab1,1)
        self.fabricarArmarioEn(hab2,2)
        self.fabricarArmarioEn(hab3,3)
        self.fabricarArmarioEn(hab4,4)

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

        hab1.agregarHijo(self.fabricarBomba())
        hab2.agregarHijo(self.fabricarBomba())
        hab3.agregarHijo(self.fabricarBomba())
        hab4.agregarHijo(self.fabricarBomba())

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
        print(juego)
        print("------------------------------------------------")

    def laberinto4Hab4BichosFM(self):
        print("\n--- LABERINTO 4 HABITACIONES y 4 BICHOS --")
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
        print(juego)
        print("------------------------------------------------")

    def obtenerHabitacion(self,num):
        return self.laberinto.obtenerHabitacion(num)
    
  
       

# PLAYGROUND
while True:
    juego = Juego()
    opcion = input("¿Qué opción quieres elegir?\n1. Laberinto 2 habitaciones\n2. Laberinto 2 habitaciones (Factory Method)\n3. Laberinto 2 habitaciones (FM & Decorator)\n4. Laberinto 4 habitaciones y 4 bichos\n5. Laberinto 4 habitaciones, 4 armarios y 4 bichos\n6. Laberinto 4 habitaciones,4 armarios, 4 bombas y 4 bichos\n\n")
    try:
        opcion = int(opcion)
        switch = {
            1: juego.laberinto2Habitaciones,
            2: juego.laberinto2HabitacionesFM,
            3: juego.laberinto2HabitacionesFMDecorator,
            4: juego.laberinto4Hab4BichosFM,
            5: juego.laberinto4Hab4Arm4BichosFM,
            6: juego.laberinto4Hab4Arm4Bombas4BichosFM
        }
        resultado = switch.get(opcion, "\n\nEl carácter ingresado no es correcto.\n\n")
        if resultado == "\n\nEl carácter ingresado no es correcto.\n\n":
            print(resultado)
        else:
            resultado()
    except ValueError:
        print("\n\nNo se admiten letras ni otro carácter fuera del rango.\n\n")


