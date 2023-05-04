#!/usr/bin/python
#-*- coding: utf-8 -*-

from model.Habitacion import Habitacion
from model.Orientacion import Orientacion


class Sur(Orientacion):
    UnicaInstancia = None

    def __new__(cls):
        if cls.UnicaInstancia is None:
            cls.UnicaInstancia = super().__new__(cls)
        return cls.UnicaInstancia
    
    def aceptarEn(self,unVisitor,unaForma):
        unaForma.sur.aceptar(unVisitor)

    def calcularPosicionDesde(self, unaForma):
        puntoX = unaForma.puntoX
        puntoY = unaForma.puntoY + 1
        unaForma.norte.calcularPosicionDesde(unaForma,puntoX,puntoY)

    def ponerElemento(self, unEM, unaHab:Habitacion):
        unaHab.sur = unEM
    
    def ir(self,alguien):
        contenedor = alguien.posicion.forma
        contenedor.sur.entrar(alguien)
    
    def obtenerElementoEn(self,unContenedor):
        return unContenedor.sur
    
    def recorrerEn(self,unBloque,unContenedor):
         if unContenedor.sur is not None:
            unContenedor.sur.recorrer(unBloque)