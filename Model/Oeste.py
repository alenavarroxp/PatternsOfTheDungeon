#!/usr/bin/python
#-*- coding: utf-8 -*-

from Habitacion import Habitacion
from Orientacion import Orientacion


class Oeste(Orientacion):
    def ponerElemento(self, unEM, unaHab:Habitacion):
        unaHab.oeste = unEM

    def ir(self,alguien):
        contenedor = alguien.posicion
        contenedor.oeste.entrar(alguien)

    def recorrerEn(self,unBloque,unContenedor):
         if unContenedor.oeste is not None:
            unContenedor.oeste.recorrer(unBloque)