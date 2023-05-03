#!/usr/bin/python
#-*- coding: utf-8 -*-

from abc import ABC
from model.Hoja import Hoja

class Decorator(Hoja,ABC):
    def __init__(self):
        self.component = None
