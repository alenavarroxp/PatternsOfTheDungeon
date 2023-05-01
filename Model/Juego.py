#!/usr/bin/python
#-*- coding: utf-8 -*-

from LaberintoFactory import LaberintoFactory
from Laberinto import Laberinto
from Habitacion import Habitacion
from Agresivo import Agresivo
from Armario import Armario
from Bicho import Bicho
from Bomba import Bomba
from Este import Este
from Baul import Baul
from Espada import Espada
from Fuego import Fuego
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
    # Métodos ITERATOR
    def activarBomba(self,unaBomba):
        if isinstance(unaBomba,Bomba):
            unaBomba.activar()

    def activarBombas(self):
        self.laberinto.recorrer(self.activarBomba)

    def desactivarBomba(self,unaBomba):
        if isinstance(unaBomba,Bomba):
            unaBomba.desactivar()

    def desactivarBombas(self):
        self.laberinto.recorrer(self.desactivarBomba)  

    def abrirPuerta(self,unaPuerta):
        if isinstance(unaPuerta,Puerta):
            unaPuerta.abrir()
    def abrirPuertas(self):
        self.laberinto.recorrer(self.abrirPuerta)

    def cerrarPuerta(self,unaPuerta):
        if isinstance(unaPuerta,Puerta):
            unaPuerta.cerrar()
    def cerrarPuertas(self):
        self.laberinto.recorrer(self.cerrarPuerta)
    ##

    def fabricarArmario(self):
        return Armario()
    
    def fabricarArmarioEn(self,unContenedor,num):
        arm = Armario(num)
        arm.ponerEnElemento(self.fabricarNorte(),self.fabricarPared())
        arm.ponerEnElemento(self.fabricarEste(),self.fabricarPared())
        arm.ponerEnElemento(self.fabricarOeste(),self.fabricarPared())
        arm.ponerEnElemento(self.fabricarSur(),self.fabricarPared())
        arm.agregarOrientacion(self.fabricarNorte())
        arm.agregarOrientacion(self.fabricarEste())
        arm.agregarOrientacion(self.fabricarOeste())
        arm.agregarOrientacion(self.fabricarSur())
        puerta = self.fabricarPuerta(arm,unContenedor)
        arm.ponerEnElemento(self.fabricarEste(),puerta)
        unContenedor.agregarHijo(arm)

    def fabricarBaul(self):
        return Baul()
    
    def fabricarBaulEn(self,unContenedor,num,contenido):
        baul = Baul(num)
        baul.ponerEnElemento(self.fabricarNorte(),self.fabricarPared())
        baul.ponerEnElemento(self.fabricarEste(),self.fabricarPared())
        baul.ponerEnElemento(self.fabricarOeste(),self.fabricarPared())
        baul.ponerEnElemento(self.fabricarSur(),self.fabricarPared())
        baul.agregarHijo(contenido)
        baul.agregarOrientacion(self.fabricarNorte())
        baul.agregarOrientacion(self.fabricarEste())
        baul.agregarOrientacion(self.fabricarOeste())
        baul.agregarOrientacion(self.fabricarSur())
        puerta = self.fabricarPuerta(baul,unContenedor)
        baul.ponerEnElemento(self.fabricarEste(),puerta)
        unContenedor.agregarHijo(baul)
        


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
    
    def fabricarEspada(self):
        return Espada()
    
    def fabricarFuego(self):
        return Fuego()
    
    def fabricarHabitacion(self,num):
        hab = Habitacion(num)
        hab.ponerEnElemento(self.fabricarNorte(),self.fabricarPared())
        hab.ponerEnElemento(self.fabricarEste(),self.fabricarPared())
        hab.ponerEnElemento(self.fabricarOeste(),self.fabricarPared())
        hab.ponerEnElemento(self.fabricarSur(),self.fabricarPared())
        hab.agregarOrientacion(self.fabricarNorte())
        hab.agregarOrientacion(self.fabricarEste())
        hab.agregarOrientacion(self.fabricarOeste())
        hab.agregarOrientacion(self.fabricarSur())
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
    
    def fabricarPuertaEstado(self,unaHab:Habitacion,otraHab:Habitacion,estado:bool):
        puerta = Puerta()
        puerta.lado1 = unaHab
        puerta.lado2 = otraHab
        puerta.abierta = estado
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
    
    def laberinto4Hab2baules(self):
        print("\n--- LABERINTO 4 HABITACIONES y 2 BAÚLES --")
        self.laberinto = self.fabricarLaberinto()
        hab1 = self.fabricarHabitacion(1)
        hab2 = self.fabricarHabitacion(2)
        hab3 = self.fabricarHabitacion(3)
        hab4 = self.fabricarHabitacion(4)

        puerta12 = self.fabricarPuertaEstado(hab1,hab2,True)
        puerta13 = self.fabricarPuertaEstado(hab1,hab3,False)
        puerta24 = self.fabricarPuertaEstado(hab2,hab4,True)
        
        bomba = self.fabricarBomba()
        bomba.component = self.fabricarPuerta(hab3,hab4)

        hab1.ponerEnElemento(self.fabricarEste(),puerta12)
        hab2.ponerEnElemento(self.fabricarOeste(),puerta12)

        hab1.ponerEnElemento(self.fabricarSur(),puerta13)
        hab3.ponerEnElemento(self.fabricarNorte(),puerta13)

        hab3.ponerEnElemento(self.fabricarEste(),bomba)
        hab4.ponerEnElemento(self.fabricarOeste(),bomba)

        hab2.ponerEnElemento(self.fabricarSur(),puerta24)
        hab4.ponerEnElemento(self.fabricarNorte(),puerta24)

        hab4.agregarHijo(self.fabricarFuego())
        self.fabricarBaulEn(hab2,2,self.fabricarBomba())
        self.fabricarBaulEn(hab3,3,self.fabricarEspada())

        self.laberinto.agregarHabitacion(hab1)
        self.laberinto.agregarHabitacion(hab2)
        self.laberinto.agregarHabitacion(hab3)
        self.laberinto.agregarHabitacion(hab4)
        print(juego)
        print("------------------------------------------------")

    def laberinto4Hab4Arm4Bombas4BichosAF(self,unAF):
        print("\n--- LABERINTO 4 HABITACIONES, 4 ARMARIOS, 4 BOMBAS y 4 BICHOS (ABSTRACT FACTORY)--")
        self.laberinto = unAF.fabricarLaberinto()
        hab1 = unAF.fabricarHabitacion(1)
        hab2 = unAF.fabricarHabitacion(2)
        hab3 = unAF.fabricarHabitacion(3)
        hab4 = unAF.fabricarHabitacion(4)

        #Unica modificacion para añadir 4 armarios al laberinto
        unAF.fabricarArmarioEn(hab1,1)
        unAF.fabricarArmarioEn(hab2,2)
        unAF.fabricarArmarioEn(hab3,3)
        unAF.fabricarArmarioEn(hab4,4)

        puerta12 = unAF.fabricarPuerta(hab1,hab2)
        puerta13 = unAF.fabricarPuerta(hab1,hab3)
        puerta24 = unAF.fabricarPuerta(hab2,hab4)
        puerta34 = unAF.fabricarPuerta(hab3,hab4)

        hab1.ponerEnElemento(unAF.fabricarSur(),puerta12)
        hab2.ponerEnElemento(unAF.fabricarNorte(),puerta12)

        hab1.ponerEnElemento(unAF.fabricarEste(),puerta13)
        hab3.ponerEnElemento(unAF.fabricarOeste(),puerta13)

        hab3.ponerEnElemento(unAF.fabricarSur(),puerta34)
        hab4.ponerEnElemento(unAF.fabricarNorte(),puerta34)

        hab2.ponerEnElemento(unAF.fabricarEste(),puerta24)
        hab4.ponerEnElemento(unAF.fabricarOeste(),puerta24)

        hab1.agregarHijo(unAF.fabricarBomba())
        hab2.agregarHijo(unAF.fabricarBomba())
        hab3.agregarHijo(unAF.fabricarBomba())
        hab4.agregarHijo(unAF.fabricarBomba())

        b1 = unAF.fabricarBichoAgresivoPosicion(hab1)
        b2 = unAF.fabricarBichoPerezosoPosicion(hab2)
        b3 = unAF.fabricarBichoAgresivoPosicion(hab3)
        b4 = unAF.fabricarBichoPerezosoPosicion(hab4)

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
    

       

# PLAYGROUND
# while True:
#     juego = Juego()
#     opcion = input("¿Qué opción quieres elegir?\n1. Laberinto 2 habitaciones\n2. EJERCICIO 1: Laberinto 2 habitaciones (Factory Method)\n3. Laberinto 2 habitaciones (FM & Decorator)\n4. Laberinto 4 habitaciones y 4 bichos\n5. Laberinto 4 habitaciones, 4 armarios y 4 bichos\n6. Laberinto 4 habitaciones,4 armarios, 4 bombas y 4 bichos\n7. EJERCICIO 2 Laberinto 4 habitaciones y 2 baúles\n8. Laberinto 4 habitaciones,4 armarios, 4 bombas y 4 bichos (ABSTRACT FACTORY)\n")
#     try:
#         opcion = int(opcion)
#         switch = {
#             1: juego.laberinto2Habitaciones,
#             2: juego.laberinto2HabitacionesFM,
#             3: juego.laberinto2HabitacionesFMDecorator,
#             4: juego.laberinto4Hab4BichosFM,
#             5: juego.laberinto4Hab4Arm4BichosFM,
#             6: juego.laberinto4Hab4Arm4Bombas4BichosFM,
#             7: juego.laberinto4Hab2baules,
#             8: juego.laberinto4Hab4Arm4Bombas4BichosAF
#         }
#         resultado = switch.get(opcion, "\n\nEl carácter ingresado no es correcto.\n\n")
#         if resultado == "\n\nEl carácter ingresado no es correcto.\n\n":
#             print(resultado)
#         else:
#             if opcion == 8:
#                 af = LaberintoFactory()
#                 resultado(af)
#             else:
#                 resultado()
#     except ValueError:
#         print("\n\nNo se admiten letras ni otro carácter fuera del rango.\n\n")

#     activado = False
#     abierto = False
#     while True:
#         if activado:
#             if abierto:
#                 operacion = input("¿Qué quieres hacer?\n1. Desactivar Bombas\n2. Cerrar Puertas\n3. Bicho actua\n4. Salir\n")
#             else:
#                 operacion = input("¿Qué quieres hacer?\n1. Desactivar Bombas\n2. Abrir Puertas\n3. Bicho actua\n4. Salir\n")
#         else:
#             if abierto:
#                 operacion = input("¿Qué quieres hacer?\n1. Activar Bombas\n2. Cerrar Puertas\n3. Bicho actua\n4. Salir\n")
#             else:
#                 operacion = input("¿Qué quieres hacer?\n1. Activar Bombas\n2. Abrir Puertas\n3. Bicho actua\n4. Salir\n")

#         try:
#             operacion = int(operacion)
#             if operacion == 1:
#                 if activado:
#                     juego.desactivarBombas()
#                     activado = False
#                 else:
#                     juego.activarBombas()
#                     activado = True
#                 print(juego)
#             elif operacion == 2:
#                 if abierto:
#                     juego.cerrarPuertas()
#                     abierto = False
#                 else:
#                     juego.abrirPuertas()
#                     abierto = True
#                 print(juego)
#             elif operacion == 3:
#                 while True:
#                     if len(juego.bichos) == 0:
#                         print("\n\nNo hay bichos en el laberinto.\n\n")
#                         break
#                     else:
#                         numero = input("¿Qué bicho quieres que actúe?\n1. Bicho1\n2. Bicho2\n3. Bicho3\n4. Bicho4\n")
#                         juego.bichos[int(numero)-1].actua()
#                         break
#                 print('\n',juego)
#             elif operacion == 4:
#                 break
#             else:
#                 print("\n\nOpción no válida.\n\n")
#         except ValueError:
#             print("\n\nNo se admiten letras ni otro carácter fuera del rango.\n\n")



