#!/usr/bin/python
#-*- coding: utf-8 -*-
from model.Ente import Ente
class Bicho(Ente):
    def __init__(self):
        super().__init__()
        
    
    def actua(self):
        self.modo.actua(self)
    
    def irA(self,unaOrientacion):
        unaOrientacion.ir(self)
        
    def obtenerOrientacionAleatoria(self):
        return self.posicion.obtenerOrientacionAleatoria()
    
    def esAgresivo(self):
        return self.modo.esAgresivo()
    
    def esPerezoso(self):
        return self.modo.esPerezoso()
    
    def __str__(self):
        return f"Bicho {self.modo}:\n\t Vidas: {self.vidas}\n\t Poder: {self.poder}\n\t Posicion:[\n\t{self.posicion}]"