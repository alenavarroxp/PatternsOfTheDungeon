#!/usr/bin/python
#-*- coding: utf-8 -*-
from src.model.Ente import Ente
from src.model.Muerto import Muerto
class Bicho(Ente):
    def __init__(self):
        super().__init__()
        
    
    def actua(self):
        self.estado.actua(self)

    def buscarEnemigo(self):
        return self.juego.buscarPersonaje(self)
    
    def estaVivo(self):
        return self.estado.estaVivo()
    
    def heMuerto(self):
        self.estado= Muerto()
        print(self, " ha muerto")
        self.juego.muereBicho()

    def puedeActuar(self):
        self.modo.actua(self)

    def quitarVidas(self,num):
        self.vidas -= num
        
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