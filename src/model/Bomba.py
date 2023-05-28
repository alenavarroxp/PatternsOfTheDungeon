#!/usr/bin/python
#-*- coding: utf-8 -*-

from src.model.Activar import Activar
from src.model.Desactivar import Desactivar
from src.model.Decorator import Decorator

class Bomba(Decorator):
    def __init__(self):
        super().__init__()
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
    
    def activar(self,alguien):
        self.activa = True
        if alguien is None:
            print('Bomba activada')
        else: 
            print(alguien," activa la bomba")
        self.quitarActivar()

    def quitarActivar(self):
        for comando in self.comandos:
            if comando.esActivar():
                self.quitarComando(comando)
                self.agregarComando(Desactivar(),self)

    def desactivar(self,alguien):
        self.activa = False
        if alguien is None:
            print('Bomba desactivada')
        else:
            print(alguien,' desactiva la bomba')
        self.quitarDesactivar()

    def quitarDesactivar(self):
        for comando in self.comandos:
            if comando.esDesactivar():
                self.quitarComando(comando)
                self.agregarComando(Activar(),self)
    
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