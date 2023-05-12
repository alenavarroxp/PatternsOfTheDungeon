#!/usr/bin/python
#-*- coding: utf-8 -*-

from time import sleep
from src.model.Modo import Modo


class Agresivo(Modo):
    def __init__(self):
        super().__init__()

    def dormir(self):
        sleep(2)

    def esAgresivo(self):
        return True
    
    def __str__(self):
        return "Agresivo"