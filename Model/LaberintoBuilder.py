from model.Agresivo import Agresivo
from model.Armario import Armario
from model.Baul import Baul
from model.Bicho import Bicho
from model.Bomba import Bomba
from model.Espada import Espada
from model.Este import Este
from model.Fuego import Fuego
from model.Habitacion import Habitacion
from model.Juego import Juego
from model.Laberinto import Laberinto
from model.Norte import Norte
from model.Oeste import Oeste
from model.Pared import Pared
from model.Perezoso import Perezoso
from model.Puerta import Puerta
from model.Sur import Sur

class LaberintoBuilder():
    def __init__(self):
        self.juego = None
        self.laberinto = None

    def obtenerJuego(self):
        return self.juego
    
    def fabricarJuego(self):
       self.juego = Juego()
       self.juego.laberinto = self.laberinto
       return self.juego
    
    def fabricarLaberinto(self):
        self.laberinto = Laberinto()
        return self.laberinto

    
    def fabricarArmario(self,num):
        return Armario(num)
    
    def fabricarArmarioEn(self,unContenedor,num):
        arm = Armario(num)
        arm.ponerEnElemento(self.fabricarNorte(),self.fabricarPared())
        arm.ponerEnElemento(self.fabricarEste(),self.fabricarPared())
        arm.ponerEnElemento(self.fabricarOeste(),self.fabricarPared())
        arm.ponerEnElemento(self.fabricarSur(),self.fabricarPared())
        arm.agregarOrientacion(self.fabricarNorte())
        arm.agregarOrientacion(self.fabricarEste())
        arm.agregarOrientacion(self.fabricarOeste())
        arm.agregarOrientacion(self.fabricarSur())
        puerta = self.fabricarPuerta(arm,unContenedor)
        arm.ponerEnElemento(self.fabricarEste(),puerta)
        unContenedor.agregarHijo(arm)

    def fabricarBaul(self,num):
        return Baul(num)
    
    def fabricarBaulEn(self,unContenedor,num,contenido):
        baul = Baul(num)
        baul.ponerEnElemento(self.fabricarNorte(),self.fabricarPared())
        baul.ponerEnElemento(self.fabricarEste(),self.fabricarPared())
        baul.ponerEnElemento(self.fabricarOeste(),self.fabricarPared())
        baul.ponerEnElemento(self.fabricarSur(),self.fabricarPared())
        baul.agregarHijo(contenido)
        baul.agregarOrientacion(self.fabricarNorte())
        baul.agregarOrientacion(self.fabricarEste())
        baul.agregarOrientacion(self.fabricarOeste())
        baul.agregarOrientacion(self.fabricarSur())
        puerta = self.fabricarPuerta(baul,unContenedor)
        baul.ponerEnElemento(self.fabricarEste(),puerta)
        unContenedor.agregarHijo(baul)
        


    def fabricarBichoAgresivo(self):
        bicho = Bicho()
        bicho.modo = self.fabricarModoAgresivo()
        bicho.vidas = 10
        bicho.poder = 10
        return bicho
    
    def fabricarBichoAgresivoPosicion(self,unaHabitacion):
        bicho = Bicho()
        bicho.modo = self.fabricarModoAgresivo()
        bicho.vidas = 10
        bicho.poder = 10
        bicho.posicion = self.juego.obtenerHabitacion(unaHabitacion)
        return bicho
     
    def fabricarBichoPerezoso(self):
        bicho = Bicho()
        bicho.modo = self.fabricarModoPerezoso()
        bicho.vidas = 10
        bicho.poder = 10
        return bicho
    
    def fabricarBichoPerezosoPosicion(self,unaHabitacion):
        bicho = Bicho()
        bicho.modo = self.fabricarModoPerezoso()
        bicho.vidas = 10
        bicho.poder = 10
        bicho.posicion = self.juego.obtenerHabitacion(unaHabitacion)
        return bicho
    
    def fabricarBomba(self):
        return Bomba()
    
    def fabricarBombaEn(self,unContenedor):
        unContenedor.agregarHijo(self.fabricarBomba())

    def fabricarEste(self):
        return Este()
    
    def fabricarEspada(self):
        return Espada()
    
    def fabricarFuego(self):
        return Fuego()
    
    def fabricarHabitacion(self,num):
        hab = Habitacion(num)
        hab.ponerEnElemento(self.fabricarNorte(),self.fabricarPared())
        hab.ponerEnElemento(self.fabricarEste(),self.fabricarPared())
        hab.ponerEnElemento(self.fabricarOeste(),self.fabricarPared())
        hab.ponerEnElemento(self.fabricarSur(),self.fabricarPared())
        hab.agregarOrientacion(self.fabricarNorte())
        hab.agregarOrientacion(self.fabricarEste())
        hab.agregarOrientacion(self.fabricarOeste())
        hab.agregarOrientacion(self.fabricarSur())
        self.laberinto.agregarHabitacion(hab)
        return hab
    
    def fabricarLaberinto(self):
        self.laberinto = Laberinto()
        return self.laberinto
    
    def fabricarModoAgresivo(self):
        return Agresivo()
    
    def fabricarModoPerezoso(self):
        return Perezoso()
   
    def fabricarNorte(self):
        return Norte()
 
    def fabricarOeste(self):
        return Oeste()
    
    def fabricarPared(self):
        return Pared()
    
    def fabricarPuerta(self,unaHab:Habitacion,otraHab:Habitacion):
        puerta = Puerta()
        puerta.lado1 = unaHab
        puerta.lado2 = otraHab
        return puerta
    
    def fabricarPuertaBuilder(self,num1, ori1, num2, ori2):
        hab1 = self.laberinto.obtenerHabitacion(num1)
        hab2 = self.laberinto.obtenerHabitacion(num2)
        juegoaux = Juego()
        cadena1 = getattr(juegoaux,'fabricar' + ori1)()
        cadena2 = getattr(juegoaux,'fabricar' + ori2)()
        puerta = self.fabricarPuerta(hab1, hab2)
        hab1.ponerEnElemento(cadena1, puerta)
        hab2.ponerEnElemento(cadena2, puerta)
    
    def fabricarPuertaEstado(self,unaHab:Habitacion,otraHab:Habitacion,estado:bool):
        puerta = Puerta()
        puerta.lado1 = unaHab
        puerta.lado2 = otraHab
        puerta.abierta = estado
        return puerta
    
    def fabricarSur(self):
        return Sur()