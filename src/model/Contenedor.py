#!/usr/bin/python
#-*- coding: utf-8 -*-

import random
from src.model.ElementoMapa import ElementoMapa
from src.model.Bomba import Bomba


class Contenedor(ElementoMapa):
    def __init__(self):
        super().__init__()
        self.hijos = []
        self.norte = None
        self.este = None
        self.oeste = None
        self.sur = None
        self.forma = None
        
        

    def __init__(self,num):
        super().__init__()
        self.hijos = []
        self.orientaciones = []
        self.norte = None
        self.este = None
        self.oeste = None
        self.sur = None
        self.forma = None
        self.num = num

    def obtenerComandos(self, alguien):
        lista = []
        for hijo in self.hijos:
            lista.extend(hijo.obtenerComandos(alguien))
        lista.extend(self.forma.obtenerComandos())
        return lista

    def agregarObjeto(self,objeto):
        self.hijos.append(objeto)
        print(objeto,"agregado a",self)

    def agregarHijo(self,unHijo):
        unHijo.padre = self
        self.hijos.append(unHijo)

    def agregarOrientacion(self,unaOrientacion):
        self.forma.agregarOrientacion(unaOrientacion)

    def calcularPosicion(self):
        self.forma.calcularPosicion()

    def ponerEnElemento(self,unaOrientacion,unEM):
        self.forma.ponerElementoEn(unaOrientacion,unEM)

    def obtenerOrientacionAleatoria(self):
        num_aleatorio = self.obtenerNumeroAleatorio(len(self.forma.orientaciones))
        return self.forma.orientaciones[num_aleatorio - 1]
    
    def obtenerNumeroAleatorio(self, lenOris):
        numRandom = random.Random()
        resultado = 1 + int(numRandom.random() * lenOris)
        return resultado
    
    def obtenerElemento(self,unaOrientacion):
        return self.forma.obtenerElemento(unaOrientacion)

    def __str__(self):
        cadena = "Hijos: "
        if len(self.hijos) == 0:
            cadena += "Sin Hijos"
        else:
            for hijo in self.hijos:
                cadena += str(hijo) +". "
        return cadena

    def recorrer(self, unBloque):
        unBloque(self)
        for hijo in self.hijos:
            hijo.recorrer(unBloque)
        self.forma.recorrer(unBloque)

      
    
       