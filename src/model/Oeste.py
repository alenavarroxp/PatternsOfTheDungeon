#!/usr/bin/python
#-*- coding: utf-8 -*-

from src.model.Habitacion import Habitacion
from src.model.Orientacion import Orientacion


class Oeste(Orientacion):
    UnicaInstancia = None

    def __new__(cls):
        if cls.UnicaInstancia is None:
            cls.UnicaInstancia = super().__new__(cls)
        return cls.UnicaInstancia

    def aceptarEn(self,unVisitor,unaForma):
        unaForma.oeste.aceptar(unVisitor)
    
    def calcularPosicionDesde(self, unaForma):
        puntoX = unaForma.puntoX - 1
        puntoY = unaForma.puntoY
        unaForma.oeste.calcularPosicionDesde(unaForma,puntoX,puntoY)

    def ponerElemento(self, unEM, unaHab:Habitacion):
        unaHab.oeste = unEM

    def ir(self,alguien):
        contenedor = alguien.posicion.forma
        contenedor.oeste.entrar(alguien)
        alguien.notificar()

    def obtenerComandosDe(self,unaForma):
        return unaForma.oeste.obtenerComandos()
    
    def obtenerElementoEn(self,unContenedor):
        return unContenedor.oeste
    
    def recorrerEn(self,unBloque,unContenedor):
         if unContenedor.oeste is not None:
            unContenedor.oeste.recorrer(unBloque)