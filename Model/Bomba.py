#!/usr/bin/python
#-*- coding: utf-8 -*-

from Decorator import Decorator

class Bomba(Decorator):
    def __init__(self):
        self.activa = False

    def entrar(self):
        if self.activa == True:
            print('La bomba ha explotado')
            self.activa = False
        else:
            self.component.entrar()

    def esBomba(self):
        return True