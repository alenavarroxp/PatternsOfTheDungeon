#!/usr/bin/python
#-*- coding: utf-8 -*-

from src.model.Afilada import Afilada
from src.model.Objeto import Objeto
class Espada(Objeto):
    def __init__(self):
        super().__init__()
        self.modo = Afilada()
    
    def aceptar(self, unVisitor):
        unVisitor.visitarEspada(self)

    def esEspada(self):
        return True
    
    def recorrer(self,unBloque):
        print('Recorriendo espada')

    def __str__(self):
        return f"Espada ({self.modo}) {self.precio}€"
    
    def __repr__(self):
        return f"Espada ({self.modo}) {self.precio}€"