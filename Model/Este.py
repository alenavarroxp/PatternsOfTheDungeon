#!/usr/bin/python
#-*- coding: utf-8 -*-

from model.Habitacion import Habitacion
from model.Orientacion import Orientacion


class Este(Orientacion):
    def ponerElemento(self, unEM, unaHab:Habitacion):
        unaHab.este = unEM
    
    def ir(self,alguien):
        contenedor = alguien.posicion
        contenedor.este.entrar(alguien)

    def recorrerEn(self,unBloque,unContenedor):
         if unContenedor.este is not None:
            unContenedor.este.recorrer(unBloque)