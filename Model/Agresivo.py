#!/usr/bin/python
#-*- coding: utf-8 -*-

from Modo import Modo


class Agresivo(Modo):
    def __init__(self):
        super().__init__()

    def esAgresivo(self):
        return True
    
    def __str__(self):
        return "Agresivo"