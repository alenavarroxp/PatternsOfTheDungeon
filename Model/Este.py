#!/usr/bin/python
#-*- coding: utf-8 -*-

from Habitacion import Habitacion
from Orientacion import Orientacion


class Este(Orientacion):
    def ponerElemento(self, unEM, unaHab:Habitacion):
        unaHab.este = unEM