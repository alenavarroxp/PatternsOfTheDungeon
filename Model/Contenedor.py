#!/usr/bin/python
#-*- coding: utf-8 -*-

from ElementoMapa import ElementoMapa


class Contenedor(ElementoMapa):
    def __init__(self,num):
        super().__init__()
        self.hijos = []
        self.norte = None
        self.este = None
        self.oeste = None
        self.sur = None
        self.num = num

    def agregarHijo(self,unHijo):
        unHijo.padre = self
        self.hijos.append(unHijo)

    def ponerEnElemento(self,unaOrientacion,unEM):
        unaOrientacion.ponerElemento(self,unEM)

    def __str__(self):
        cadena = "Hijos: "
        if len(self.hijos) == 0:
            cadena += "Sin Hijos"
        else:
            for hijo in self.hijos:
                cadena += str(hijo) +". "

        return cadena
