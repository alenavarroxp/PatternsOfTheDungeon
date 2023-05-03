#!/usr/bin/python
#-*- coding: utf-8 -*-

from model.Habitacion import Habitacion
from model.Orientacion import Orientacion


class Norte(Orientacion):
    def ponerElemento(self, unEM, unaHab:Habitacion):
        unaHab.norte = unEM

    def ir(self,alguien):
        contenedor = alguien.posicion
        contenedor.norte.entrar(alguien)

    def recorrerEn(self,unBloque,unContenedor):
         if unContenedor.norte is not None:
            unContenedor.norte.recorrer(unBloque)