#!/usr/bin/python
#-*- coding: utf-8 -*-

class ElementoMapa:
    def __init__(self):
        self.padre = None
        self.bool = False

    def get_bool(self):
        return self.bool
    
    def set_bool(self,bool):
        self.bool = bool

    def entrar(self):
        pass

    def entrar(self,alguien):
        pass
    
    def esArmario(self):
        return False
    
    def esBaul(self):
        return False

    def esBomba(self):
        return False
    
    def esHabitacion(self):
        return False
    
    def esPared(self):
        return False
    
    def esPuerta(self):
        return False
    
    def recorrer(self,unBloque):
        unBloque(self)
    
