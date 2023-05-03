#!/usr/bin/python
#-*- coding: utf-8 -*-

from model.Habitacion import Habitacion
from model.Orientacion import Orientacion


class Sur(Orientacion):
    UnicaInstancia = None

    def __new__(cls):
        if cls.UnicaInstancia is None:
            cls.UnicaInstancia = super().__new__(cls)
        return cls.UnicaInstancia
    
    def ponerElemento(self, unEM, unaHab:Habitacion):
        unaHab.sur = unEM
    
    def ir(self,alguien):
        contenedor = alguien.posicion
        contenedor.sur.entrar(alguien)
    
    def recorrerEn(self,unBloque,unContenedor):
         if unContenedor.sur is not None:
            unContenedor.sur.recorrer(unBloque)