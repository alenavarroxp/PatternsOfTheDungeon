#!/usr/bin/python
#-*- coding: utf-8 -*-

from ElementoMapa import ElementoMapa

class Pared(ElementoMapa):
    def entrar(self):
        print('Te has chocado con una pared.')

    def esPared(self):
        return True
    
    def ponerEnElemento(self, unaOrientacion, unEM, unaHab):
        unaOrientacion.ponerElemento(self, unaHab)

    def __str__(self):
        return "Pared"