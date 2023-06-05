#!/usr/bin/python
#-*- coding: utf-8 -*-

from src.model.Habitacion import Habitacion
from src.model.Orientacion import Orientacion


class Norte(Orientacion):
    UnicaInstancia = None

    def __new__(cls):
        if cls.UnicaInstancia is None:
            cls.UnicaInstancia = super().__new__(cls)
        return cls.UnicaInstancia

    def aceptarEn(self,unVisitor,unaForma):
        unaForma.norte.aceptar(unVisitor)
    
    def calcularPosicionDesde(self, unaForma):
        puntoX = unaForma.puntoX
        puntoY = unaForma.puntoY - 1
        unaForma.norte.calcularPosicionDesde(unaForma,puntoX,puntoY)

    def ponerElemento(self, unEM, unaHab:Habitacion):
        unaHab.norte = unEM

    def ir(self,alguien):
        contenedor = alguien.posicion.forma
        contenedor.norte.entrar(alguien)

    def obtenerElementoEn(self,unContenedor):
        return unContenedor.norte
    
    def obtenerComandosDe(self,unaForma):
        return unaForma.norte.obtenerComandos(None)
    
    def recorrerEn(self,unBloque,unContenedor):
         if unContenedor.norte is not None:
            unContenedor.norte.recorrer(unBloque)