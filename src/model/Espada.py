#!/usr/bin/python
#-*- coding: utf-8 -*-

from src.model.Objeto import Objeto
class Espada(Objeto):
    def __init__(self):
        super().__init__()
        self.estado = True

    def obtenerComandos(self):
        pass
    
    def esEspada(self):
        return True
    
    def recorrer(self,unBloque):
        print('Recorriendo espada')

    def __str__(self):
        if self.estado:
            estado = 'Afilada'
        else:
            estado = 'Rota'
        return f"Espada ({estado}) Precio: {self.precio}"
    
    def __repr__(self):
        if self.estado:
            estado = 'Afilada'
        else:
            estado = 'Rota'
        return f"Espada ({estado}) Precio: {self.precio}"