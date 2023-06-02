import unittest
import os
from colorama import init, Fore, Style
from src.model.Afilada import Afilada
from src.model.Cuadrado import Cuadrado
from src.model.Rombo import Rombo
from src.model.Director import Director
from src.model.Juego import Juego

class Test(unittest.TestCase):

    def setUp(self):
        init()
        super().setUp()
        self.juego = Juego()
        ruta_actual = os.path.abspath(__file__)
        directorio_proyecto = os.path.dirname(ruta_actual)
        unArchivo = os.path.join(directorio_proyecto, "laberintos/lab4Hab4Arm4HechicerosTunel.json")
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

    def testHechiceros(self):
        hechiceroMago = 0
        hechiceroBrujo = 0
        print(Fore.MAGENTA+"\nHechiceros:"+ Style.RESET_ALL)
        self.assertEqual(len(self.juego.hechiceros), 4)
        print("Hay 4 hechiceros: ",Fore.GREEN+"Correct"+ Style.RESET_ALL)
        for hechicero in self.juego.hechiceros:
            if hechicero.esMago():
                hechiceroMago+=1
            else:
                hechiceroBrujo+=1
        self.assertEqual(hechiceroMago, 2)
        print("Hay 2 magos: ",Fore.GREEN+"Correct"+ Style.RESET_ALL)
        self.assertEqual(hechiceroBrujo, 2)
        print("Hay 2 brujos: ",Fore.GREEN+"Correct"+ Style.RESET_ALL)

    def testArmarios(self):
        for habitacion in self.juego.laberinto.hijos:
            for hijo in self.juego.laberinto.hijos[habitacion.num-1].hijos:
                if hijo.esArmario():
                    print(Fore.MAGENTA+"\nArmario "+str(hijo.num)+":"+ Style.RESET_ALL)
                    self.assertEqual(hijo is not None, True)
                    print("El armario "+str(hijo.num)+" no es nulo: ",Fore.GREEN+"Correct"+ Style.RESET_ALL)
                    self.assertEqual(hijo.esArmario(), True)
                    print("El armario "+str(hijo.num)+" es armario: ",Fore.GREEN+"Correct"+ Style.RESET_ALL)
                elif hijo.esBaul():
                    print(Fore.MAGENTA+"\nBaul "+str(hijo.num)+":"+ Style.RESET_ALL)
                    self.assertEqual(hijo is not None, True)
                    print("El baul "+str(hijo.num)+" no es nulo: ",Fore.GREEN+"Correct"+ Style.RESET_ALL)
                    self.assertEqual(hijo.esBaul(), True)
                    print("El baul "+str(hijo.num)+" es baul: ",Fore.GREEN+"Correct"+ Style.RESET_ALL)
                    for hijo in hijo.hijos:
                        if hijo.esEspada():
                            print(Fore.MAGENTA+"\nEspada:"+ Style.RESET_ALL)
                            self.assertEqual(hijo.esEspada(), True)
                            print("La espada "+str(hijo)+" es espada: ",Fore.GREEN+"Correct"+ Style.RESET_ALL)
                            self.assertTrue(isinstance(hijo.estado, Afilada))
                            print("La espada "+str(hijo)+" esta afilada: ",Fore.GREEN+"Correct"+ Style.RESET_ALL)

                elif hijo.esTunel():
                    print(Fore.MAGENTA+"\nTunel:"+ Style.RESET_ALL)
                    self.assertEqual(hijo is not None, True)
                    print("El tunel no es nulo: ",Fore.GREEN+"Correct"+ Style.RESET_ALL)
                    self.assertEqual(hijo.esTunel(), True)
                    print("El tunel es tunel: ",Fore.GREEN+"Correct"+ Style.RESET_ALL)

        

if __name__ == '__main__':
    unittest.main()