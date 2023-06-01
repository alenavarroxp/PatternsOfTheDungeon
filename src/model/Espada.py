#!/usr/bin/python
#-*- coding: utf-8 -*-

from src.model.Usar import Usar
from src.model.Afilada import Afilada
from src.model.Objeto import Objeto
class Espada(Objeto):
    def __init__(self):
        super().__init__()
        self.estado = Afilada()
        self.poder = 0
    
    def aceptar(self, unVisitor):
        unVisitor.visitarEspada(self)

    def esEspada(self):
        return True
    
    def usarObjeto(self,alguien):
        self.estado.usarObjeto(alguien,self)
        for comando in self.comandos:
            if comando.esUsar():
                self.quitarUsar(comando)
        for objeto in alguien.inventario.objetos:
            if objeto is not self:
                if not any(comando.esUsar() for comando in objeto.comandos):
                    objeto.agregarComando(Usar(),objeto)

                    
                
        alguien.notificar()
    
    def quitarUsar(self,comando):
        self.quitarComando(comando)

    def recorrer(self,unBloque):
        print('Recorriendo espada')

    def __str__(self):
        for comando in self.comandos:
            if comando.esComprar():
                return f"Espada ({self.estado}) {self.precio}€"
            if comando.esCoger():
                return f"Espada {self.poder} poder"
            if comando.esUsar():
                return f"Espada {self.poder} poder"
        return f"Espada ({self.estado})"
    
    def __repr__(self):
        return f"Espada ({self.estado}) {self.precio}€"