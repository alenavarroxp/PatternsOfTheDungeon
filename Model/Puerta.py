#!/usr/bin/python
#-*- coding: utf-8 -*-

from model.ElementoMapa import ElementoMapa

class Puerta(ElementoMapa):
    def __init__(self):
        self.abierta = False
        self.lado1 = None
        self.lado2 = None

    def entrar(self):
        if self.abierta == True:
            print('Puedes pasar.')
        else:
            print('La puerta está cerrada.')

    def entrar(self,alguien):
        if self.abierta == True:
            if self.lado1 == alguien.posicion:
                self.lado2.entrar(alguien)
                alguien.posicion = self.lado2
            else:
                self.lado1.entrar(alguien)
                alguien.posicion = self.lado1
            print('Bicho puede pasar al otro lado') #Puedo poner alguien en vez de 'Bicho'
        else:
            print('La puerta está cerrada.')
            
    def abrir(self):
        self.abierta = True
        print('Puerta abierta')

    def cerrar(self):
        self.abierta = False
        print('Puerta cerrada')

    def estaCerrada(self):
        return self.abierta
    
    def esPuerta(self):
        return True
    
    def __str__(self):
        if self.abierta:
            estado = 'Abierta'        
        else:
            estado = 'Cerrada'

        return f"Puerta ({estado})"



