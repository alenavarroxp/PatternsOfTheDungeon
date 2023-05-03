#!/usr/bin/python
#-*- coding: utf-8 -*-

from model.Decorator import Decorator

class Fuego(Decorator):
    def __init__(self):
        self.activo = True

    def esFuego(self):
        return True
    
    def __str__(self):
        if self.activo:
            estado = 'Activo'
        else:
            estado = 'No activo'
        return f"Fuego ({estado})"