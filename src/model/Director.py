#!/usr/bin/python
#-*- coding: utf-8 -*-

import json
from src.model.LaberintoRomboBuilder import LaberintoRomboBuilder
from src.model.LaberintoBuilder import LaberintoBuilder


class Director():
    def __init__(self):
        self.dict = None
        self.builder = None
    
    def iniBuilder(self):
        if self.dict['forma'] == 'cuadrado':
            self.builder = LaberintoBuilder()
        if self.dict['forma'] == 'rombo':
            self.builder = LaberintoRomboBuilder()
    def obtenerJuego(self):
        return self.builder.juego
    
    def crearJuego(self):
        self.builder.fabricarJuego()
        for bicho in self.dict['bichos']:
            if bicho['modo'] == 'agresivo':
                self.builder.juego.agregarBicho(self.builder.fabricarBichoAgresivoPosicion(bicho['posicion']))
            else:
                self.builder.juego.agregarBicho(self.builder.fabricarBichoPerezosoPosicion(bicho['posicion']))

    def crearLaberinto(self):
        self.builder.fabricarLaberinto()
        for laberinto in self.dict['laberinto']:
            self.crearLaberintoRecursivo(laberinto, 'root')
        for puerta in self.dict['puertas']:
            self.builder.fabricarPuertaBuilder(puerta[0], puerta[1], puerta[2], puerta[3])

    def crearLaberintoRecursivo(self, laberinto, root):
        if laberinto['tipo'] == 'habitacion':
            tmp1 = self.builder.fabricarHabitacion(laberinto['num'])
        elif laberinto['tipo'] == 'armario':
            tmp1 = self.builder.fabricarArmarioEn(root)
        elif laberinto['tipo'] == 'tunel':
            tmp1 = self.builder.fabricarTunelEn(root)
        elif laberinto['tipo'] == 'baul':
            tmp1 = self.builder.fabricarBaul(laberinto['num'])
        elif laberinto['tipo'] == 'bomba':
            tmp1 = self.builder.fabricarBombaEn(root)
        
        hijos = laberinto.get('hijos', [])
        for hijo in hijos:
            self.crearLaberintoRecursivo(hijo, tmp1)

    def leerConfig(self,ruta):
        with open(ruta,'r') as f:
            self.dict = json.load(f)

    def procesar(self,ruta):
        self.leerConfig(ruta)
        self.iniBuilder()
        self.crearLaberinto()
        self.crearJuego()
        