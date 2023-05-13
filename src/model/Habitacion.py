#!/usr/bin/python
#-*- coding: utf-8 -*-

from src.model.Contenedor import Contenedor
from src.model.Cuadrado import Cuadrado
import colorama as colarama
class Habitacion(Contenedor):
    
    def __init__(self, num):
        super().__init__(num)
        self.forma = Cuadrado()

    def aceptar(self,unVisitor):
        unVisitor.visitarHabitacion(self)
        for hijo in self.hijos:
            hijo.aceptar(unVisitor)
        self.forma.aceptar(unVisitor)

    def entrar(self):
        print('Estas en la habitación: ',self.num)

    def entrar(self,alguien):
        alguien.posicion = self
        print(alguien,' entra en la habitación: ',self.num)
    
    def esHabitacion(self):
        return True
    
    def agregarTienda(self,tienda):
        super().agregarHijo(tienda)
        self.agregarHijo(tienda)
    

    def __str__(self):
        colarama.init()
       # Definir los colores
        color_num = colarama.Fore.LIGHTBLUE_EX
        color_texto = colarama.Fore.MAGENTA

        # Formatear las variables
        num_formatted = f"{color_num}{self.num}{colarama.Style.RESET_ALL}"

        # Construir la cadena de salida
        output = f"{color_texto}Habitacion {num_formatted}:\n"
        output += f"\t Norte: {self.forma.norte}\n"
        output += f"\t Sur: {self.forma.sur}\n"
        output += f"\t Este: {self.forma.este}\n"
        output += f"\t Oeste: {self.forma.oeste}\n"
        output += f"\t {super().__str__()}{colarama.Style.RESET_ALL}"

        return output