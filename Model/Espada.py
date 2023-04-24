#!/usr/bin/python
#-*- coding: utf-8 -*-

from Decorator import Decorator

class Espada(Decorator):
    def __init__(self):
        self.estado = True

    def esEspada(self):
        return True
    
    def __str__(self):
        if self.estado:
            estado = 'Afilada'
        else:
            estado = 'Rota'
        return f"Espada ({estado})"