#!/usr/bin/python
#-*- coding: utf-8 -*-

from Model.Modo import Modo


class Agresivo(Modo):
    def __init__(self):
        super().__init__()

    def esAgresivo(self):
        return True