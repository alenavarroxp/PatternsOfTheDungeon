#!/usr/bin/python
#-*- coding: utf-8 -*-

from abc import ABC
from ElementoMapa import ElementoMapa

class Decorator(ElementoMapa,ABC):
    def __init__(self):
        self.component = None
