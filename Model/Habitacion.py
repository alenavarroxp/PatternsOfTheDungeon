#!/usr/bin/python
#-*- coding: utf-8 -*-


from ElementoMapa import ElementoMapa

class Habitacion(ElementoMapa):
    
    def __init__(self):
        self.norte = None
        self.sur = None
        self.este = None
        self.oeste = None
        self.num = None
        

    def __init__(self,num):
        super().__init__()
        self.num = num
    
    def entrar(self):
        print('Estas en la habitación: ',self.num)
    

