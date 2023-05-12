#!/usr/bin/python
#-*- coding: utf-8 -*-

from src.model.ElementoMapa import ElementoMapa

class Pared(ElementoMapa):
    def entrar(self):
        print('Te has chocado con una pared.')
    
    def aceptar(self,unVisitor):
        unVisitor.visitarPared(self)

    def calcularPosicionDesde(self,unaForma,puntoX,puntoY):
        pass


    def entrar(self,alguien):
        print(alguien,' se ha chocado con una pared.')

    def esPared(self):
        return True
    
    def ponerEnElemento(self, unaOrientacion, unEM, unaHab):
        unaOrientacion.ponerElemento(self, unaHab)

    def __str__(self):
        return "Pared"