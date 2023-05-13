#!/usr/bin/python
#-*- coding: utf-8 -*-

from time import sleep

import colorama
from src.model.Modo import Modo


class Perezoso(Modo):
    def __init__(self):
        super().__init__()

    def dormir(self):
        sleep(4)
        
    def esPerezoso(self):
        return True
    
    def __str__(self):
        colorama.init()
        return ""+colorama.Fore.BLUE+"Perezoso"+colorama.Style.RESET_ALL