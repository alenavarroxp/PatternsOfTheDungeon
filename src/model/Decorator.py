#!/usr/bin/python
#-*- coding: utf-8 -*-

from abc import ABC
from src.model.Hoja import Hoja

class Decorator(Hoja,ABC):
    def __init__(self):
        super().__init__()
        self.component = None
