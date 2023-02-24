#!/usr/bin/python
#-*- coding: utf-8 -*-

from Model.Habitacion import Habitacion
from Model.Orientacion import Orientacion


class Oeste(Orientacion):
    def ponerElemento(self, unEM, unaHab:Habitacion):
        unaHab.oeste = unEM