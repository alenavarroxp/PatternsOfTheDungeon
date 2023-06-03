import unittest
import os
from colorama import init, Fore, Style
from src.model.Afilada import Afilada
from src.model.Cuadrado import Cuadrado
from src.model.Director import Director
from src.model.Juego import Juego

class Test(unittest.TestCase):

    def setUp(self):
        init()
        super().setUp()
        self.juego = Juego()
        ruta_actual = os.path.abspath(__file__)
        directorio_proyecto = os.path.dirname(ruta_actual)
        unArchivo = os.path.join(directorio_proyecto, "laberintos/lab4Hab4Arm3Baul1Tienda4Entes.json")
        director = Director()
        director.procesar(unArchivo)
        self.juego = director.obtenerJuego()

    def testIniciales(self):
        self.assertEqual(self.juego.laberinto is not None, True)
        self.assertEqual(len(self.juego.laberinto.hijos), 4)
    
    def testHabitaciones(self):
        hab1 = self.juego.obtenerHabitacion(1)
        print(Fore.MAGENTA+"\nHabitacion 1:"+ Style.RESET_ALL)
        if isinstance(hab1.forma,Cuadrado):
            print("La forma de la habitación 1 es cuadrado: ",Fore.GREEN+"Correct"+ Style.RESET_ALL)
            self.assertEqual(hab1.forma.norte.esPared(),True)
            print("El norte de la habitación 1 es pared: ",Fore.GREEN+"Correct"+ Style.RESET_ALL) 
            self.assertEqual(hab1.forma.este.esPuerta(),True)
            print("El este de la habitación 1 es puerta: ",Fore.GREEN+"Correct"+ Style.RESET_ALL)
            self.assertEqual(hab1.forma.este.esPared(),False)
            print("El este de la habitación 1 no es pared: ",Fore.GREEN+"Correct"+ Style.RESET_ALL)
            self.assertEqual(hab1.forma.sur.esPared(),False)
            print("El sur de la habitación 1 no es pared: ",Fore.GREEN+"Correct"+ Style.RESET_ALL)
            self.assertEqual(hab1.forma.sur.esPuerta(),True)
            print("El sur de la habitación 1 es puerta: ",Fore.GREEN+"Correct"+ Style.RESET_ALL)
            self.assertEqual(hab1.forma.oeste.esPared(),True)
            print("El oeste de la habitación 1 es pared: ",Fore.GREEN+"Correct"+ Style.RESET_ALL)
        
        print("\nHabitación 1: ",Fore.GREEN+"Correct"+ Style.RESET_ALL)

        hab2 = self.juego.obtenerHabitacion(2)
        print(Fore.MAGENTA+"\nHabitacion 2:"+ Style.RESET_ALL)
        if isinstance(hab2.forma,Cuadrado):
            print("La forma de la habitación 2 es cuadrado: ",Fore.GREEN+"Correct"+ Style.RESET_ALL)
            self.assertEqual(hab2.forma.norte.esPared(),False)
            print("El norte de la habitación 2 no es pared: ",Fore.GREEN+"Correct"+ Style.RESET_ALL)
            self.assertEqual(hab2.forma.norte.esPuerta(),True)
            print("El norte de la habitación 2 es puerta: ",Fore.GREEN+"Correct"+ Style.RESET_ALL)
            self.assertEqual(hab2.forma.este.esPared(),False)
            print("El este de la habitación 2 no es pared: ",Fore.GREEN+"Correct"+ Style.RESET_ALL)
            self.assertEqual(hab2.forma.este.esPuerta(),True)
            print("El este de la habitación 2 es puerta: ",Fore.GREEN+"Correct"+ Style.RESET_ALL)
            self.assertEqual(hab2.forma.sur.esPared(),True)
            print("El sur de la habitación 2 es pared: ",Fore.GREEN+"Correct"+ Style.RESET_ALL)
            self.assertEqual(hab2.forma.oeste.esPared(),True)
            print("El oeste de la habitación 2 es pared: ",Fore.GREEN+"Correct"+ Style.RESET_ALL)

        print("\nHabitación 2: ",Fore.GREEN+"Correct"+ Style.RESET_ALL)

        hab3 = self.juego.obtenerHabitacion(3)
        print(Fore.MAGENTA+"\nHabitacion 3:"+ Style.RESET_ALL)
        if isinstance(hab3.forma,Cuadrado):
            print("La forma de la habitación 3 es cuadrado: ",Fore.GREEN+"Correct"+ Style.RESET_ALL)
            self.assertEqual(hab3.forma.norte.esPared(),True)
            print("El norte de la habitación 3 es pared: ",Fore.GREEN+"Correct"+ Style.RESET_ALL)
            self.assertEqual(hab3.forma.este.esPared(),True)    
            print("El este de la habitación 3 es pared: ",Fore.GREEN+"Correct"+ Style.RESET_ALL)
            self.assertEqual(hab3.forma.sur.esPared(),False)
            print("El sur de la habitación 3 no es pared: ",Fore.GREEN+"Correct"+ Style.RESET_ALL)
            self.assertEqual(hab3.forma.sur.esPuerta(),True)
            print("El sur de la habitación 3 es puerta: ",Fore.GREEN+"Correct"+ Style.RESET_ALL)
            self.assertEqual(hab3.forma.oeste.esPared(),False)
            print("El oeste de la habitación 3 no es pared: ",Fore.GREEN+"Correct"+ Style.RESET_ALL)
            self.assertEqual(hab3.forma.oeste.esPuerta(),True)
            print("El oeste de la habitación 3 es puerta: ",Fore.GREEN+"Correct"+ Style.RESET_ALL)

        print("\nHabitación 3: ",Fore.GREEN+"Correct"+ Style.RESET_ALL)

        hab4 = self.juego.obtenerHabitacion(4)
        print(Fore.MAGENTA+"\nHabitacion 4:"+ Style.RESET_ALL)
        if isinstance(hab4.forma,Cuadrado):
            self.assertEqual(hab4.forma.norte.esPared(),False)
            print("El norte de la habitación 4 no es pared: ",Fore.GREEN+"Correct"+ Style.RESET_ALL)
            self.assertEqual(hab4.forma.norte.esPuerta(),True)
            print("El norte de la habitación 4 es puerta: ",Fore.GREEN+"Correct"+ Style.RESET_ALL)
            self.assertEqual(hab4.forma.este.esPared(),True)
            print("El este de la habitación 4 es pared: ",Fore.GREEN+"Correct"+ Style.RESET_ALL)
            self.assertEqual(hab4.forma.sur.esPared(),True)
            print("El sur de la habitación 4 es pared: ",Fore.GREEN+"Correct"+ Style.RESET_ALL)
            self.assertEqual(hab4.forma.oeste.esPared(),False)
            print("El oeste de la habitación 4 no es pared: ",Fore.GREEN+"Correct"+ Style.RESET_ALL)
            self.assertEqual(hab4.forma.oeste.esPuerta(),True)
            print("El oeste de la habitación 4 es puerta: ",Fore.GREEN+"Correct"+ Style.RESET_ALL)
        
        print("\nHabitación 4: ",Fore.GREEN+"Correct"+ Style.RESET_ALL)

    def testBichos(self):
        bichoPerezoso = 0
        print(Fore.MAGENTA+"\nBichos:"+ Style.RESET_ALL)
        self.assertEqual(len(self.juego.bichos), 2)
        print("Hay 2 bichos: ",Fore.GREEN+"Correct"+ Style.RESET_ALL)
        for bicho in self.juego.bichos:
            if bicho.esPerezoso():
                bichoPerezoso+=1
        self.assertEqual(bichoPerezoso, 2)
        print("Hay 2 bichos perezosos: ",Fore.GREEN+"Correct"+ Style.RESET_ALL)
        print("\nBichos: ",Fore.GREEN+"Correct"+ Style.RESET_ALL)
    
    def testHechiceros(self):
        hechiceroMago = 0
        hechiceroBrujo = 0
        print(Fore.MAGENTA+"\nHechiceros:"+ Style.RESET_ALL)
        self.assertEqual(len(self.juego.hechiceros), 2)
        print("Hay 2 hechiceros: ",Fore.GREEN+"Correct"+ Style.RESET_ALL)
        for hechicero in self.juego.hechiceros:
            if hechicero.esMago():
                hechiceroMago+=1
            if hechicero.esBrujo():
                hechiceroBrujo+=1
        self.assertEqual(hechiceroMago, 1)
        print("Hay 1 hechicero mago: ",Fore.GREEN+"Correct"+ Style.RESET_ALL)
        self.assertEqual(hechiceroBrujo, 1)
        print("Hay 1 hechicero brujo: ",Fore.GREEN+"Correct"+ Style.RESET_ALL)
        print("\nHechiceros: ",Fore.GREEN+"Correct"+ Style.RESET_ALL)
        

    def testArmario(self):
            for habitacion in self.juego.laberinto.hijos:
                for hijo in habitacion.hijos:
                    if hijo.esArmario():
                        print(Fore.MAGENTA+"\nArmario "+str(hijo.num)+":"+ Style.RESET_ALL)
                        self.assertEqual(hijo is not None, True)
                        print("El armario "+str(hijo.num)+" no es nulo: ",Fore.GREEN+"Correct"+ Style.RESET_ALL)
                        self.assertEqual(hijo.esArmario(), True)
                        print("El armario "+str(hijo.num)+" es armario: ",Fore.GREEN+"Correct"+ Style.RESET_ALL)

    def testBaul(self):
            for habitacion in self.juego.laberinto.hijos:
                for hijo in habitacion.hijos:
                    if hijo.esBaul():
                        print(Fore.MAGENTA+"\nBaul "+str(hijo.num)+":"+ Style.RESET_ALL)
                        self.assertEqual(hijo is not None, True)
                        print("El baul "+str(hijo.num)+" no es nulo: ",Fore.GREEN+"Correct"+ Style.RESET_ALL)
                        self.assertEqual(hijo.esBaul(), True)
                        print("El baul "+str(hijo.num)+" es baul: ",Fore.GREEN+"Correct"+ Style.RESET_ALL)
                        for contenido in hijo.hijos:
                            if contenido.esEspada():
                                print(Fore.MAGENTA+"\n"+str(contenido)+":"+ Style.RESET_ALL)
                                self.assertEqual(contenido is not None, True)
                                print("La espada "+str(contenido)+" no es nula: ",Fore.GREEN+"Correct"+ Style.RESET_ALL)
                                self.assertEqual(contenido.esEspada(), True)
                                print("La espada "+str(contenido)+" es espada: ",Fore.GREEN+"Correct"+ Style.RESET_ALL)
                                self.assertEqual(isinstance(contenido.estado,Afilada),True)
                                print("La espada "+str(contenido)+" es afilada: ",Fore.GREEN+"Correct"+ Style.RESET_ALL)
                                self.assertEqual(contenido.padre,hijo)
                                print("El padre de la espada "+str(contenido)+" es el baul "+str(hijo.num)+": ",Fore.GREEN+"Correct"+ Style.RESET_ALL)
                            if contenido.esMochila():
                                print(Fore.MAGENTA+"\n"+str(contenido)+":"+ Style.RESET_ALL)
                                self.assertEqual(contenido is not None, True)
                                print("La mochila "+str(contenido)+" no es nula: ",Fore.GREEN+"Correct"+ Style.RESET_ALL)
                                self.assertEqual(contenido.esMochila(), True)
                                print("La mochila "+str(contenido)+" es mochila: ",Fore.GREEN+"Correct"+ Style.RESET_ALL)
                                self.assertEqual(contenido.padre,hijo)
                                print("El padre de la mochila "+str(contenido)+" es el baul "+str(hijo.num)+": ",Fore.GREEN+"Correct"+ Style.RESET_ALL)
                            if contenido.esMoneda():
                                print(Fore.MAGENTA+"\n"+str(contenido)+":"+ Style.RESET_ALL)
                                self.assertEqual(contenido is not None, True)
                                print("La moneda "+str(contenido)+" no es nula: ",Fore.GREEN+"Correct"+ Style.RESET_ALL)
                                self.assertEqual(contenido.esMoneda(), True)
                                print("La moneda "+str(contenido)+" es moneda: ",Fore.GREEN+"Correct"+ Style.RESET_ALL)
                                self.assertEqual(contenido.padre,hijo)
                                print("El padre de la moneda "+str(contenido)+" es el baul "+str(hijo.num)+": ",Fore.GREEN+"Correct"+ Style.RESET_ALL)

    def testBomba(self):
            for habitacion in self.juego.laberinto.hijos:
                for hijo in habitacion.hijos:
                    if hijo.esBomba():
                        print(Fore.MAGENTA+"\n"+str(hijo)+":"+ Style.RESET_ALL)
                        self.assertEqual(hijo is not None, True)
                        print("La bomba "+str(hijo)+" no es nula: ",Fore.GREEN+"Correct"+ Style.RESET_ALL)
                        self.assertEqual(hijo.esBomba(), True)
                        print("La bomba "+str(hijo)+" es bomba: ",Fore.GREEN+"Correct"+ Style.RESET_ALL)
                        self.assertEqual(hijo.activa,False)
                        print("La bomba "+str(hijo)+" no está activa: ",Fore.GREEN+"Correct"+ Style.RESET_ALL)
                        self.assertEqual(hijo.padre,habitacion)
                        print("El padre de la bomba "+str(hijo)+" es la habitacion "+str(habitacion.num)+": ",Fore.GREEN+"Correct"+ Style.RESET_ALL)

    def testEspada(self):
            for habitacion in self.juego.laberinto.hijos:
                for hijo in habitacion.hijos:
                    if hijo.esEspada():
                        print(Fore.MAGENTA+"\n"+str(hijo)+":"+ Style.RESET_ALL)
                        self.assertEqual(hijo is not None, True)
                        print("La espada "+str(hijo)+" no es nula: ",Fore.GREEN+"Correct"+ Style.RESET_ALL)
                        self.assertEqual(hijo.esEspada(), True)
                        print("La espada "+str(hijo)+" es espada: ",Fore.GREEN+"Correct"+ Style.RESET_ALL)
                        self.assertEqual(isinstance(hijo.estado,Afilada),True)
                        print("La espada "+str(hijo)+" es afilada: ",Fore.GREEN+"Correct"+ Style.RESET_ALL)
                        self.assertEqual(hijo.padre,habitacion)
                        print("El padre de la espada "+str(hijo)+" es la habitacion "+str(habitacion.num)+": ",Fore.GREEN+"Correct"+ Style.RESET_ALL)
    
    def testMochila(self):
            for habitacion in self.juego.laberinto.hijos:
                for hijo in habitacion.hijos:
                    if hijo.esMochila():
                        print(Fore.MAGENTA+"\n"+str(hijo)+":"+ Style.RESET_ALL)
                        self.assertEqual(hijo is not None, True)
                        print("La mochila "+str(hijo)+" no es nula: ",Fore.GREEN+"Correct"+ Style.RESET_ALL)
                        self.assertEqual(hijo.esMochila(), True)
                        print("La mochila "+str(hijo)+" es mochila: ",Fore.GREEN+"Correct"+ Style.RESET_ALL)
                        self.assertEqual(hijo.padre,habitacion)
                        print("El padre de la mochila "+str(hijo)+" es la habitacion "+str(habitacion.num)+": ",Fore.GREEN+"Correct"+ Style.RESET_ALL)

    def testMoneda(self):
            for habitacion in self.juego.laberinto.hijos:
                for hijo in habitacion.hijos:
                    if hijo.esMoneda():
                        print(Fore.MAGENTA+"\n"+str(hijo)+":"+ Style.RESET_ALL)
                        self.assertEqual(hijo is not None, True)
                        print("La moneda "+str(hijo)+" no es nula: ",Fore.GREEN+"Correct"+ Style.RESET_ALL)
                        self.assertEqual(hijo.esMoneda(), True)
                        print("La moneda "+str(hijo)+" es moneda: ",Fore.GREEN+"Correct"+ Style.RESET_ALL)
                        self.assertEqual(hijo.padre,habitacion)
                        print("El padre de la moneda "+str(hijo)+" es la habitacion "+str(habitacion.num)+": ",Fore.GREEN+"Correct"+ Style.RESET_ALL)
    
    def testTienda(self):
            for habitacion in self.juego.laberinto.hijos:
                for hijo in habitacion.hijos:
                    if hijo.esTienda():
                        print(Fore.MAGENTA+"\n"+str(hijo)+":"+ Style.RESET_ALL)
                        self.assertEqual(hijo is not None, True)
                        print("La tienda "+str(hijo)+" no es nula: ",Fore.GREEN+"Correct"+ Style.RESET_ALL)
                        self.assertEqual(hijo.esTienda(), True)
                        print("La tienda "+str(hijo)+" es tienda: ",Fore.GREEN+"Correct"+ Style.RESET_ALL)
                        self.assertEqual(hijo.padre,habitacion)
                        print("El padre de la tienda "+str(hijo)+" es la habitacion "+str(habitacion.num)+": ",Fore.GREEN+"Correct"+ Style.RESET_ALL)
                        for contenido in hijo.hijos:
                           if contenido.esEspada():
                                print(Fore.MAGENTA+"\n"+str(contenido)+":"+ Style.RESET_ALL)
                                self.assertEqual(contenido is not None, True)
                                print("La espada "+str(contenido)+" no es nula: ",Fore.GREEN+"Correct"+ Style.RESET_ALL)
                                self.assertEqual(contenido.esEspada(), True)
                                print("La espada "+str(contenido)+" es espada: ",Fore.GREEN+"Correct"+ Style.RESET_ALL)
                                self.assertEqual(isinstance(contenido.estado,Afilada),True)
                                print("La espada "+str(contenido)+" es afilada: ",Fore.GREEN+"Correct"+ Style.RESET_ALL)
                                self.assertEqual(contenido.padre,hijo)
                                print("El padre de la espada "+str(contenido)+" es la tienda "+str(hijo.num)+": ",Fore.GREEN+"Correct"+ Style.RESET_ALL)
                        


if __name__ == '__main__':
    unittest.main()
