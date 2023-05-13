#!/usr/bin/python
#-*- coding: utf-8 -*-

from time import sleep
from src.model.Modo import Modo
import colorama

class Agresivo(Modo):
    def __init__(self):
        super().__init__()

    def dormir(self):
        sleep(2)

    def esAgresivo(self):
        return True
    
    def __str__(self):
        colorama.init()
        return ""+colorama.Fore.LIGHTYELLOW_EX+"Agresivo"+colorama.Style.RESET_ALL