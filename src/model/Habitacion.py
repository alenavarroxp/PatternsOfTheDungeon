#!/usr/bin/python
#-*- coding: utf-8 -*-

from src.model.Contenedor import Contenedor
from src.model.Cuadrado import Cuadrado
from src.model.Rombo import Rombo
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
        if isinstance(self.forma, Cuadrado):
            output += f"\t Norte: {self.forma.norte}\n"
            output += f"\t Sur: {self.forma.sur}\n"
            output += f"\t Este: {self.forma.este}\n"
            output += f"\t Oeste: {self.forma.oeste}\n"
            output += f"\t {super().__str__()}{colarama.Style.RESET_ALL}"
        if isinstance(self.forma, Rombo):
            output += f"\t Noroeste: {self.forma.noroeste}\n"
            output += f"\t Noreste: {self.forma.noreste}\n"
            output += f"\t Suroeste: {self.forma.suroeste}\n"
            output += f"\t Sureste: {self.forma.sureste}\n"
            output += f"\t {super().__str__()}{colarama.Style.RESET_ALL}"
        return output