#!/usr/bin/python
#-*- coding: utf-8 -*-

from model.Habitacion import Habitacion
from model.Orientacion import Orientacion


class Este(Orientacion):
    UnicaInstancia = None

    def __new__(cls):
        if cls.UnicaInstancia is None:
            cls.UnicaInstancia = super().__new__(cls)
        return cls.UnicaInstancia

    def ponerElemento(self, unEM, unaHab:Habitacion):
        unaHab.este = unEM
    
    def ir(self,alguien):
        contenedor = alguien.posicion.forma
        contenedor.este.entrar(alguien)

    def obtenerElementoEn(self,unContenedor):
        return unContenedor.este
    
    def recorrerEn(self,unBloque,unContenedor):
         if unContenedor.este is not None:
            unContenedor.este.recorrer(unBloque)