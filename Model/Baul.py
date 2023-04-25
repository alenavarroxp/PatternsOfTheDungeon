#!/usr/bin/python
#-*- coding: utf-8 -*-


from Contenedor import Contenedor


class Baul(Contenedor):
    def __init__(self, num):
        super().__init__(num)
        

    def entrar(self):
        print('Estas en el baul',self.num)
    def entrar(self,alguien):
        print(alguien,' entra en el baúl: ',self.num)
    
    def esBaul(self):
        return True
    
    def __str__(self):
        return f"Baul: {self.num} {super().__str__()}"