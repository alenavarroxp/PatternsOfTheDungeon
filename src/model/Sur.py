#!/usr/bin/python
#-*- coding: utf-8 -*-

from src.model.Habitacion import Habitacion
from src.model.Orientacion import Orientacion


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
        unaForma.sur.calcularPosicionDesde(unaForma,puntoX,puntoY)

    def ponerElemento(self, unEM, unaHab:Habitacion):
        unaHab.sur = unEM
    
    def ir(self,alguien):
        contenedor = alguien.posicion.forma
        contenedor.sur.entrar(alguien)
        alguien.notificar()
    
    def obtenerComandosDe(self,unaForma):
        return unaForma.sur.obtenerComandos(None)
    
    def obtenerElementoEn(self,unContenedor):
        return unContenedor.sur
    
    def recorrerEn(self,unBloque,unContenedor):
         if unContenedor.sur is not None:
            unContenedor.sur.recorrer(unBloque)