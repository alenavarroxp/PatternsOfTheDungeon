#!/usr/bin/python
#-*- coding: utf-8 -*-

from Model.Habitacion import Habitacion
from Model.Orientacion import Orientacion


class Sur(Orientacion):
    def ponerElemento(self, unEM, unaHab:Habitacion):
        unaHab.sur = unEM