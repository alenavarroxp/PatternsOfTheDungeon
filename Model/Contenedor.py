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
        unHijo.padre = self
        self.hijos.append(unHijo)

    def ponerEnElemento(self,unaOrientacion,unEM):
        unaOrientacion.ponerElemento(self)
