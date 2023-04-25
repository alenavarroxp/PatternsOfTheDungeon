#!/usr/bin/python
#-*- coding: utf-8 -*-

from Habitacion import Habitacion
from Orientacion import Orientacion


class Norte(Orientacion):
    def ponerElemento(self, unEM, unaHab:Habitacion):
        unaHab.norte = unEM

    def recorrerEn(self,unBloque,unContenedor):
         if unContenedor.norte is not None:
            unContenedor.norte.recorrer(unBloque)