#!/usr/bin/python
#-*- coding: utf-8 -*-

from Habitacion import Habitacion
from Orientacion import Orientacion


class Sur(Orientacion):
    def ponerElemento(self, unEM, unaHab:Habitacion):
        unaHab.sur = unEM
    
    def ir(self,alguien):
        contenedor = alguien.posicion
        contenedor.sur.entrar(alguien)
    
    def recorrerEn(self,unBloque,unContenedor):
         if unContenedor.sur is not None:
            unContenedor.sur.recorrer(unBloque)