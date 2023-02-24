#!/usr/bin/python
#-*- coding: utf-8 -*-

from Model.ElementoMapa import ElementoMapa


class Contenedor(ElementoMapa):
    def __init__(self):
        self.hijos = []
        self.norte = None
        self.este = None
        self.oeste = None
        self.sur = None
        self.num = None

    def agregarHijo(self,unHijo):
        self.hijos.append(unHijo)
        #Falta lo del padre

    def ponerEnElemento(self,unaOrientacion,unEM):
        unaOrientacion.ponerElemento(self)
