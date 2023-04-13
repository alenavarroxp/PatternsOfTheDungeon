#!/usr/bin/python
#-*- coding: utf-8 -*-

from Modo import Modo


class Perezoso(Modo):
    def __init__(self):
        super().__init__()

    def esPerezoso(self):
        return True
    
    def __str__(self):
        return "Perezoso"