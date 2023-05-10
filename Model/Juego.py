#!/usr/bin/python
#-*- coding: utf-8 -*-
import copy
import threading
from model.Cuadrado import Cuadrado
from model.Forma import Forma
from model.Laberinto import Laberinto
from model.Habitacion import Habitacion
from model.Agresivo import Agresivo
from model.Armario import Armario
from model.Bicho import Bicho
from model.Bomba import Bomba
from model.Este import Este
from model.Baul import Baul
from model.Espada import Espada
from model.Fuego import Fuego
from model.Moneda import Moneda
from model.Norte import Norte
from model.Oeste import Oeste
from model.Perezoso import Perezoso
from model.Sur import Sur
from model.Pared import Pared
from model.Puerta import Puerta


class Juego:
    def __init__(self):
        self.laberinto = None
        self.bichos = []
        self.personaje = None
        self.prototipo = None
        self.hilos = dict()
    
    def __str__(self):
        infoBicho = ""
        for bicho in self.bichos:
            infoBicho += f"  {bicho}\n"
        personaje= ""
        if self.personaje is None:
            return f"Juego:\n Personaje: No hay personaje\n {self.laberinto}\n Hay {len(self.bichos)} bichos en el laberinto:\n {infoBicho}"
        else:
            return f"Juego:\n Personaje: {self.personaje}\n {self.laberinto}\n Hay {len(self.bichos)} bichos en el laberinto:\n {infoBicho}"

    def __repr__(self):
        infoBicho = ""
        for bicho in self.bichos:
            infoBicho += f"  {bicho}\n"
        return f"Juego:\n {self.personaje}\n{self.laberinto}\n Hay {len(self.bichos)} bichos en el laberinto:\n {infoBicho}"
    # Gestión de los hilos#
    def agregarHiloDe(self,unHilo,unBicho):
        self.hilos[unBicho] = unHilo

    def lanzarBichos(self):
        for bicho in self.bichos:
            self.lanzarHilo(bicho)

    def lanzarHilo(self, unBicho):
        hilo = threading.Thread(target=lambda: self.hiloBicho(unBicho))
        self.agregarHiloDe(hilo, unBicho)
        hilo.start()
        
    def hiloBicho(self, unBicho):
        while unBicho.estaVivo():
            unBicho.actua()

    def terminarBichos(self):
        for bicho in self.bichos:
            self.terminarHilo(bicho)
    
    def terminarHilo(self,unBicho):
        unBicho.heMuerto()
        

    def todosMuertos(self):
        result = None
        for bicho in self.bichos:
            if bicho.estaVivo():
                result = bicho
        if result is None:
            return True
        result = None
        return False
    ##
    def agregarBicho(self,unBicho):
        self.bichos.append(unBicho)
        unBicho.juego = self

    def agregarPersonaje(self,unPersonaje):
        self.personaje = unPersonaje
        self.personaje.juego = self
        self.personaje.vidas = 100
        self.laberinto.entrar(self.personaje)
    
    def clonarLaberinto(self):
        self.prototipo = copy.deepcopy(self)
        return self.prototipo.laberinto
    
    # Métodos ITERATOR
    def activarBomba(self,unaBomba):
        if unaBomba.esBomba():
            unaBomba.activar()

    def activarBombas(self):
        self.laberinto.recorrer(self.activarBomba)

    def desactivarBomba(self,unaBomba):
        if unaBomba.esBomba():
            unaBomba.desactivar()

    def desactivarBombas(self):
        self.laberinto.recorrer(self.desactivarBomba)  

    def abrirPuerta(self,unaPuerta):
        if unaPuerta.esPuerta():
            unaPuerta.abrir()
        
    def abrirPuertas(self):
        self.laberinto.recorrer(self.abrirPuerta)

    def cerrarPuerta(self,unaPuerta):
        if unaPuerta.esPuerta():
            unaPuerta.cerrar()
    def cerrarPuertas(self):
        self.laberinto.recorrer(self.cerrarPuerta)

    ##
    def buscarBicho(self):
        pos = self.personaje.posicion
        for bicho in self.bichos:
            if bicho.estaVivo and bicho.posicion == pos:
                return bicho
        return None
    
    def buscarPersonaje(self,unBicho):
        if self.personaje is not None:
            pos = self.personaje.posicion
            if unBicho.posicion == pos:
                return self.personaje
        return None
    
    def muereBicho(self):
        if self.todosMuertos():
            if self.personaje is not None:
                print("Fin del juego. Gana el personaje.")
            else:
                print("Fin del juego. Han ganado los bichos.")

    def personajeMuere(self):
        print("Fin del juego.",self.personaje.nickname," ha muerto.")
        self.personaje = None
        self.terminarBichos()
    
   
    ##

    def fabricarArmario(self):
        return Armario()
    
    def fabricarArmarioEn(self,unContenedor,num):
        arm = Armario(num)
        arm.forma = self.fabricarForma()
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
        baul.forma = self.fabricarForma()
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
        baul.ponerEnElemento(self.fabricarNorte(),puerta)
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
    
    def fabricarForma(self):
        return Cuadrado()
    
    def fabricarHabitacion(self,num):
        hab = Habitacion(num)
        hab.forma = self.fabricarForma()
        hab.forma.num = num
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
    
    def fabricarMoneda(self,valor):
        return Moneda(valor)
   
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

        hab1.forma.sur = puerta
        hab2.forma.norte = puerta

        hab1.forma.norte = Pared()
        hab1.forma.este = Pared()
        hab1.forma.oeste = Pared()

        hab2.forma.sur = Pared()
        hab2.forma.este = Pared()
        hab2.forma.oeste = Pared()

        self.laberinto.agregarHabitacion(hab1)
        self.laberinto.agregarHabitacion(hab2)
    
        print("------------------------------------------------")


    def laberinto2HabitacionesFM(self):
        print("\n--- LABERINTO 2 HABITACIONES (FACTORY METHOD) --")
        self.laberinto = self.fabricarLaberinto()
        hab1 = self.fabricarHabitacion(1)
        hab2 = self.fabricarHabitacion(2)

        puerta = self.fabricarPuerta(hab1,hab2)
        hab1.forma.norte = self.fabricarPared()
        hab1.forma.oeste = self.fabricarPared()
        hab1.forma.este = self.fabricarPared()

        hab2.forma.sur = self.fabricarPared()
        hab2.forma.oeste = self.fabricarPared()
        hab2.forma.este = self.fabricarPared()

        hab1.forma.sur = puerta
        hab2.forma.norte = puerta

        self.laberinto.agregarHabitacion(hab1)
        self.laberinto.agregarHabitacion(hab2)
    
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

        hab1.forma.norte = bomba1
        hab1.forma.oeste = self.fabricarPared()
        hab1.forma.este = self.fabricarPared()

        hab2.forma.sur = bomba2
        hab2.forma.oeste = self.fabricarPared()
        hab2.forma.este = self.fabricarPared()

        hab1.forma.sur = puerta
        hab2.forma.norte = puerta

        self.laberinto.agregarHabitacion(hab1)
        self.laberinto.agregarHabitacion(hab2)
    
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
    
        print("------------------------------------------------")




