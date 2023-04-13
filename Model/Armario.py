#!/usr/bin/python
#-*- coding: utf-8 -*-


from Contenedor import Contenedor


class Armario(Contenedor):
    def __init__(self, num):
        super().__init__(num)

    def entrar(self):
        print('Estas en el armario',self.num)

    def __str__(self):
        return f"Armario: {self.num}"