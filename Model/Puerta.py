#!/usr/bin/python
#-*- coding: utf-8 -*-

from ElementoMapa import ElementoMapa

class Puerta(ElementoMapa):
    def __init__(self):
        self.abierta = False
        self.lado1 = None
        self.lado2 = None
    def entrar(self):
        if self.abierta == True:
            print('Puedes pasar.')
        else:
            print('La puerta está cerrada.')



