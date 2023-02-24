#!/usr/bin/python
#-*- coding: utf-8 -*-

from Model.Modo import Modo


class Perezoso(Modo):
    def __init__(self):
        super().__init__()

    def esPerezoso(self):
        return True