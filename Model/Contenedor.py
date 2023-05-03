#!/usr/bin/python
#-*- coding: utf-8 -*-

import random
from model.ElementoMapa import ElementoMapa
from model.Bomba import Bomba


class Contenedor(ElementoMapa):
    def __init__(self):
        super().__init__()
        self.hijos = []
        self.orientaciones = []
        self.norte = None
        self.este = None
        self.oeste = None
        self.sur = None
        

    def __init__(self,num):
        super().__init__()
        self.hijos = []
        self.orientaciones = []
        self.norte = None
        self.este = None
        self.oeste = None
        self.sur = None
        self.num = num

    def agregarHijo(self,unHijo):
        unHijo.padre = self
        self.hijos.append(unHijo)

    def agregarOrientacion(self,unaOrientacion):
        self.orientaciones.append(unaOrientacion)

    def ponerEnElemento(self,unaOrientacion,unEM):
        unaOrientacion.ponerElemento(unEM,self)

    def obtenerOrientacionAleatoria(self):
        num_aleatorio = self.obtenerNumeroAleatorio(len(self.orientaciones))
        return self.orientaciones[num_aleatorio - 1]
    
    def obtenerNumeroAleatorio(self, lenOris):
        numRandom = random.Random()
        resultado = 1 + int(numRandom.random() * lenOris)
        return resultado

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
        for orientacion in self.orientaciones:
            orientacion.recorrerEn(unBloque,self)
       

      
    
       