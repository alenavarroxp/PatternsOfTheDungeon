#!/usr/bin/python
#-*- coding: utf-8 -*-

class ElementoMapa:
    def __init__(self):
        self.padre = None
       
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

    def esHoja(self):
        return False
    
    def esTunel(self):
        return False
    
    def recorrer(self,unBloque):
        unBloque(self)
    
