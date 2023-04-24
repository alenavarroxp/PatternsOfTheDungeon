#!/usr/bin/python
#-*- coding: utf-8 -*-

from ElementoMapa import ElementoMapa
from Bomba import Bomba


class Contenedor(ElementoMapa):
    def __init__(self):
        super().__init__()
        self.hijos = []
        self.norte = None
        self.este = None
        self.oeste = None
        self.sur = None
        

    def __init__(self,num):
        super().__init__()
        self.hijos = []
        self.norte = None
        self.este = None
        self.oeste = None
        self.sur = None
        self.num = num

    def agregarHijo(self,unHijo):
        unHijo.padre = self
        self.hijos.append(unHijo)

    def ponerEnElemento(self,unaOrientacion,unEM):
        unaOrientacion.ponerElemento(self,unEM)

    def __str__(self):
        cadena = "Hijos: "
        if len(self.hijos) == 0:
            cadena += "Sin Hijos"
        else:
            for hijo in self.hijos:
                cadena += str(hijo) +". "

        return cadena
    
    def cambiar_estado_orientaciones(self, estado):
        if isinstance(self.norte, Bomba):
            if not estado:
                self.norte.activar()
            else:
                self.norte.desactivar()
        if isinstance(self.este, Bomba):
            if not estado:
                self.este.activar()
            else:
                self.este.desactivar()
        if isinstance(self.oeste, Bomba):
            if not estado:
                self.oeste.activar()
            else:
                self.oeste.desactivar()
        if isinstance(self.sur, Bomba):
            if not estado:
                self.sur.activar()
            else:
                self.sur.desactivar()


    def recorrer(self, unBloque):
        unBloque(self)
        for hijo in self.hijos:
            hijo.recorrer(unBloque)
        estado_actual = super().get_bool()
        super().set_bool(not estado_actual)
        self.cambiar_estado_orientaciones(estado_actual)

      
    
       