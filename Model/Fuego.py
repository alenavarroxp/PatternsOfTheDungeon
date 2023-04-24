#!/usr/bin/python
#-*- coding: utf-8 -*-

from Decorator import Decorator

class Fuego(Decorator):
    def __init__(self):
        self.estado = True

    def esFuego(self):
        return True
    
    def __str__(self):
        if self.estado:
            estado = 'Activo'
        else:
            estado = 'No activo'
        return f"Fuego ({estado})"