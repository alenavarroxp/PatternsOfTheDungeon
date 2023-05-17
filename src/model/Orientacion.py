#!/usr/bin/python
#-*- coding: utf-8 -*-

from abc import ABC


class Orientacion(ABC):
    def __init__(self):
        pass
    
    def calcularPosicionDesde(self,unaForma):
        pass
    
    def recorrerEn(self,unBloque,unContenedor):
        pass
    
    def ir(self,alguien):
        pass

    def ponerElemento(self,unEM,unaForma):
        pass

    def obtenerComandosDe(self,unaForma):
        pass

    def obtenerElementoEn(self,unContenedor):
        pass

