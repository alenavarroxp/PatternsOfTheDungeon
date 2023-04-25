#!/usr/bin/python
#-*- coding: utf-8 -*-

class Bicho():
    def __init__(self):
        self.modo = None
        self.poder = None
        self.vidas = None
        self.posicion = None
    
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