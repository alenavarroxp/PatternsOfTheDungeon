#!/usr/bin/python
#-*- coding: utf-8 -*-


from ElementoMapa import ElementoMapa

class Habitacion(ElementoMapa):
    def __init__(self):
        self.norte = None
        self.sur = None
        self.este = None
        self.oeste = None
        self.num = None


