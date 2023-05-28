#!/usr/bin/python
#-*- coding: utf-8 -*-

from src.model.Habitacion import Habitacion
from src.model.Orientacion import Orientacion


class Este(Orientacion):
    UnicaInstancia = None

    def __new__(cls):
        if cls.UnicaInstancia is None:
            cls.UnicaInstancia = super().__new__(cls)
        return cls.UnicaInstancia

    def aceptarEn(self,unVisitor,unaForma):
        unaForma.este.aceptar(unVisitor)
    
    def calcularPosicionDesde(self, unaForma):
        puntoX = unaForma.puntoX + 1
        puntoY = unaForma.puntoY
        unaForma.este.calcularPosicionDesde(unaForma,puntoX,puntoY)

    def ponerElemento(self, unEM, unaHab:Habitacion):
        unaHab.este = unEM
    
    def ir(self,alguien):
        contenedor = alguien.posicion.forma
        contenedor.este.entrar(alguien)
        alguien.notificar()

    def obtenerComandosDe(self,unaForma):
        return unaForma.este.obtenerComandos(None)

    def obtenerElementoEn(self,unContenedor):
        return unContenedor.este
    
    def recorrerEn(self,unBloque,unContenedor):
         if unContenedor.este is not None:
            unContenedor.este.recorrer(unBloque)