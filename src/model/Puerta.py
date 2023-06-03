#!/usr/bin/python
#-*- coding: utf-8 -*-

from src.model.Entrar import Entrar
from src.model.Abrir import Abrir
from src.model.ElementoMapa import ElementoMapa
from src.model.Cerrar import Cerrar

class Puerta(ElementoMapa):

    def __init__(self):
        super().__init__()
        self.abierta = False
        self.lado1 = None
        self.lado2 = None
        self.visitada = False
        self.dibujada = False
        

    def aceptar(self,unVisitor):
        unVisitor.visitarPuerta(self)
        self.dibujada = True

    def calcularPosicionDesde(self,unContenedor,puntoX,puntoY):
        if self.visitada == True:
            return self
        else:
            self.visitada = True
            if unContenedor.num == self.lado1.num:
                self.lado2.forma.puntoX = puntoX
                self.lado2.forma.puntoY = puntoY
                self.lado2.calcularPosicion()
            else:
                self.lado1.forma.puntoX = puntoX
                self.lado1.forma.puntoY = puntoY
                self.lado1.calcularPosicion()
            

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
            print(alguien,' puede pasar al otro lado')
        else:
            print('La puerta está cerrada.')
            
    # def abrir(self):
    #     self.abierta = True
    #     print('Puerta abierta')

    def abrir(self,alguien):
        self.abierta = True
        if alguien is None:
            print('Puerta abierta')
        else:
            print(alguien,' abre la puerta')
        self.quitarAbrir()

    def quitarAbrir(self):
        for comando in self.comandos:
            if comando.esAbrir():
                self.quitarComando(comando)
                self.agregarComando(Entrar(),self)
                self.agregarComando(Cerrar(),self)

    def cerrar(self,alguien):
        self.abierta = False
        if alguien is None:
            print('Puerta cerrada')
        else:
            print(alguien,' cierra la puerta')
        self.quitarCerrar()
        self.quitarEntrar()
            
    def quitarCerrar(self):
        for comando in self.comandos:
            if comando.esCerrar():
                self.quitarComando(comando)
                self.agregarComando(Abrir(),self)

    def quitarEntrar(self):
        for comando in self.comandos:
            if comando.esEntrar():
                self.quitarComando(comando)
                
    def estaCerrada(self):
        return self.abierta
    
    def esPuerta(self):
        return True
    
    def __str__(self):
        if self.abierta:
            estado = 'Abierta'        
        else:
            estado = 'Cerrada'

        return f"Puerta ({estado}) Comandos:{self.comandos}"



