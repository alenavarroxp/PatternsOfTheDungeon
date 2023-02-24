#!/usr/bin/python
#-*- coding: utf-8 -*-


from Model.Contenedor import Contenedor


class Armario(Contenedor):
    def entrar(self):
        print('Estas en el armario',self.num)