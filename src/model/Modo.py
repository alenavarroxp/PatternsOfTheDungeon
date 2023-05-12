#!/usr/bin/python
#-*- coding: utf-8 -*-
from time import sleep
class Modo():
    def __init__(self):
        pass
    
    def actua(self, bicho):
        self.dormir()
        self.caminar(bicho)
        self.ataca(bicho)
    
    def dormir(self):
        print("Bicho duerme")
        sleep(2)
        
    def caminar(self, bicho):
        print("Bicho camina")
        orientacion = bicho.obtenerOrientacionAleatoria()
        bicho.irA(orientacion)
    
    def ataca(self,bicho):
        bicho.atacar()
        
    def esAgresivo(self):
        return False
    
    def esPerezoso(self):
        return False