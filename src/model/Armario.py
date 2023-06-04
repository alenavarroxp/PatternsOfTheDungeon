#!/usr/bin/python
#-*- coding: utf-8 -*-


from src.model.Contenedor import Contenedor


class Armario(Contenedor):
    def __init__(self, num):
        super().__init__(num)
    
    def aceptar(self,unVisitor):
        unVisitor.visitarArmario(self)
        for hijo in self.hijos:
            hijo.aceptar(unVisitor)
        self.forma.aceptar(unVisitor)
    
    def obtenerComandos(self,alguien):
        lista = []
        if alguien.posicion is self:
            lista = self.forma.obtenerComandos()
            for objeto in self.hijos:
                lista.append(objeto.comandos[0])
        else: 
            
            lista = self.forma.obtenerComandos()
        
        return lista
        
    def entrar(self):
        print('Estas en el armario',self.num)

    def entrar(self,alguien):
        print(alguien,' entra en el armario: ',self.num)
    
    def esArmario(self):
        return True
    
    def __str__(self):
        return f"Armario: {self.num}"