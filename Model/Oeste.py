#!/usr/bin/python
#-*- coding: utf-8 -*-

from model.Habitacion import Habitacion
from model.Orientacion import Orientacion


class Oeste(Orientacion):
    UnicaInstancia = None

    def __new__(cls):
        if cls.UnicaInstancia is None:
            cls.UnicaInstancia = super().__new__(cls)
        return cls.UnicaInstancia

    def ponerElemento(self, unEM, unaHab:Habitacion):
        unaHab.oeste = unEM

    def ir(self,alguien):
        contenedor = alguien.posicion.forma
        contenedor.oeste.entrar(alguien)

    def obtenerElementoEn(self,unContenedor):
        return unContenedor.oeste
    
    def recorrerEn(self,unBloque,unContenedor):
         if unContenedor.oeste is not None:
            unContenedor.oeste.recorrer(unBloque)