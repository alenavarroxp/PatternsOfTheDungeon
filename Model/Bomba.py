#!/usr/bin/python
#-*- coding: utf-8 -*-

from model.Decorator import Decorator

class Bomba(Decorator):
    def __init__(self):
        self.activa = False
        
    def aceptar(self,unVisitor):
        unVisitor.visitarBomba(self)

    def entrar(self):
        if self.activa == True:
            print('La bomba ha explotado')
            self.activa = False
        else:
            self.component.entrar()

    def esBomba(self):
        return True
    
    def activar(self):
        self.activa = True
        print('Bomba activada')

    def desactivar(self):
        self.activa = False
        print('Bomba desactivada')
    
    def __str__(self):
        if self.activa:
            estado = 'Activa'
        else:
            estado = 'No activa'
        return f"Bomba ({estado})"
    
    def __repr__(self):
        if self.activa:
            estado = 'Activa'
        else:
            estado = 'No activa'
        return f"Bomba ({estado})"