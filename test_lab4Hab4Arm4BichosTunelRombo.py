import unittest
import os
from colorama import init, Fore, Style
from src.model.Personaje import Personaje
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
        unArchivo = os.path.join(directorio_proyecto, "laberintos/lab4Hab4Arm4BichosTunelRombo.json")
        director = Director()
        director.procesar(unArchivo)
        self.juego = director.obtenerJuego()
        self.personaje = Personaje()
        self.juego.agregarPersonaje(self.personaje)

    def testIniciales(self):
        self.assertEqual(self.juego.laberinto is not None, True)
        self.assertEqual(len(self.juego.laberinto.hijos), 4)

    
    def testPersonaje(self):
            
            print(Fore.MAGENTA+"\nPersonaje:"+ Style.RESET_ALL)
            self.assertEqual(self.personaje is not None, True)
            print("El personaje se ha creado: ",Fore.GREEN+"Correct"+ Style.RESET_ALL)
            self.assertEqual(self.personaje.vidas, 100)
            print("El personaje tiene 100 vidas: ",Fore.GREEN+"Correct"+ Style.RESET_ALL)
            self.assertEqual(self.personaje.poder, 10)
            print("El personaje tiene 10 de poder: ",Fore.GREEN+"Correct"+ Style.RESET_ALL)
            self.assertEqual(self.personaje.dinero,50)
            print("El personaje tiene 50 de dinero: ",Fore.GREEN+"Correct"+ Style.RESET_ALL)
            self.assertEqual(self.personaje.posicion, self.juego.obtenerHabitacion(1))
            print("El personaje esta en la habitacion 1: ",Fore.GREEN+"Correct"+ Style.RESET_ALL)
    
    def testHabitaciones(self):
        hab1 = self.juego.obtenerHabitacion(1)
        print(Fore.MAGENTA+"\nHabitacion 1:"+ Style.RESET_ALL)
        if isinstance(hab1.forma,Rombo):
            print("La forma de la habitación 1 es rombo: ",Fore.GREEN+"Correct"+ Style.RESET_ALL)
            self.assertEqual(hab1.forma.noroeste.esPared(),True)
            print("El noroeste de la habitación 1 es pared: ",Fore.GREEN+"Correct"+ Style.RESET_ALL)
            self.assertEqual(hab1.forma.noreste.esPuerta(),True)
            print("El noreste de la habitación 1 es puerta: ",Fore.GREEN+"Correct"+ Style.RESET_ALL)
            self.assertEqual(hab1.forma.noreste.esPared(),False)
            print("El noreste de la habitación 1 no es pared: ",Fore.GREEN+"Correct"+ Style.RESET_ALL)
            self.assertEqual(hab1.forma.sureste.esPared(),False)
            print("El sureste de la habitación 1 no es pared: ",Fore.GREEN+"Correct"+ Style.RESET_ALL)
            self.assertEqual(hab1.forma.sureste.esPuerta(),True)
            print("El sureste de la habitación 1 es puerta: ",Fore.GREEN+"Correct"+ Style.RESET_ALL)
            self.assertEqual(hab1.forma.suroeste.esPared(),True)
            print("El suroeste de la habitación 1 es pared: ",Fore.GREEN+"Correct"+ Style.RESET_ALL)
        print("\nHabitación 1: ",Fore.GREEN+"Correct"+ Style.RESET_ALL)

        hab2 = self.juego.obtenerHabitacion(2)
        print(Fore.MAGENTA+"\nHabitacion 2:"+ Style.RESET_ALL)
        if isinstance(hab2.forma,Rombo):
            print("La forma de la habitación 2 es rombo: ",Fore.GREEN+"Correct"+ Style.RESET_ALL)
            self.assertEqual(hab2.forma.noroeste.esPared(),False)
            print("El noroeste de la habitación 2 no es pared: ",Fore.GREEN+"Correct"+ Style.RESET_ALL)
            self.assertEqual(hab2.forma.noroeste.esPuerta(),True)
            print("El noroeste de la habitación 2 es puerta: ",Fore.GREEN+"Correct"+ Style.RESET_ALL)
            self.assertEqual(hab2.forma.noreste.esPared(),False)
            print("El noreste de la habitación 2 no es pared: ",Fore.GREEN+"Correct"+ Style.RESET_ALL)
            self.assertEqual(hab2.forma.noreste.esPuerta(),True)
            print("El noreste de la habitación 2 es puerta: ",Fore.GREEN+"Correct"+ Style.RESET_ALL)
            self.assertEqual(hab2.forma.sureste.esPared(),True)
            print("El sureste de la habitación 2 es pared: ",Fore.GREEN+"Correct"+ Style.RESET_ALL)
            self.assertEqual(hab2.forma.suroeste.esPared(),True)
            print("El suroeste de la habitación 2 es pared: ",Fore.GREEN+"Correct"+ Style.RESET_ALL)
        print("\nHabitación 2: ",Fore.GREEN+"Correct"+ Style.RESET_ALL)

        hab3 = self.juego.obtenerHabitacion(3)
        print(Fore.MAGENTA+"\nHabitacion 3:"+ Style.RESET_ALL)
        if isinstance(hab3.forma,Rombo):
            print("La forma de la habitación 3 es rombo: ",Fore.GREEN+"Correct"+ Style.RESET_ALL)
            self.assertEqual(hab3.forma.noroeste.esPared(),True)
            print("El noroeste de la habitación 3 es pared: ",Fore.GREEN+"Correct"+ Style.RESET_ALL)
            self.assertEqual(hab3.forma.noreste.esPared(),True)
            print("El noreste de la habitación 3 es pared: ",Fore.GREEN+"Correct"+ Style.RESET_ALL)
            self.assertEqual(hab3.forma.sureste.esPared(),False)
            print("El sureste de la habitación 3 no es pared: ",Fore.GREEN+"Correct"+ Style.RESET_ALL)
            self.assertEqual(hab3.forma.sureste.esPuerta(),True)
            print("El sureste de la habitación 3 es puerta: ",Fore.GREEN+"Correct"+ Style.RESET_ALL)
            self.assertEqual(hab3.forma.suroeste.esPared(),False)
            print("El suroeste de la habitación 3 no es pared: ",Fore.GREEN+"Correct"+ Style.RESET_ALL)
            self.assertEqual(hab3.forma.suroeste.esPuerta(),True)
            print("El suroeste de la habitación 3 es puerta: ",Fore.GREEN+"Correct"+ Style.RESET_ALL)
        print("\nHabitación 3: ",Fore.GREEN+"Correct"+ Style.RESET_ALL)

        hab4 = self.juego.obtenerHabitacion(4)
        print(Fore.MAGENTA+"\nHabitacion 4:"+ Style.RESET_ALL)
        if isinstance(hab4.forma,Rombo):
            print("La forma de la habitación 4 es rombo: ",Fore.GREEN+"Correct"+ Style.RESET_ALL)
            self.assertEqual(hab4.forma.noroeste.esPared(),False)
            print("El noroeste de la habitación 4 no es pared: ",Fore.GREEN+"Correct"+ Style.RESET_ALL)
            self.assertEqual(hab4.forma.noroeste.esPuerta(),True)
            print("El noroeste de la habitación 4 es puerta: ",Fore.GREEN+"Correct"+ Style.RESET_ALL)
            self.assertEqual(hab4.forma.noreste.esPared(),True)
            print("El noreste de la habitación 4 es pared: ",Fore.GREEN+"Correct"+ Style.RESET_ALL)
            self.assertEqual(hab4.forma.sureste.esPared(),True)
            print("El sureste de la habitación 4 es pared: ",Fore.GREEN+"Correct"+ Style.RESET_ALL)
            self.assertEqual(hab4.forma.suroeste.esPared(),False)
            print("El suroeste de la habitación 4 no es pared: ",Fore.GREEN+"Correct"+ Style.RESET_ALL)
            self.assertEqual(hab4.forma.suroeste.esPuerta(),True)
            print("El suroeste de la habitación 4 es puerta: ",Fore.GREEN+"Correct"+ Style.RESET_ALL)
        print("\nHabitación 4: ",Fore.GREEN+"Correct"+ Style.RESET_ALL)

    def testBichos(self):
        bichoAgresivo = 0
        bichoPerezoso = 0
        print(Fore.MAGENTA+"\nBichos:"+ Style.RESET_ALL)
        self.assertEqual(len(self.juego.bichos), 4)
        print("Hay 4 bichos: ",Fore.GREEN+"Correct"+ Style.RESET_ALL)
        for bicho in self.juego.bichos:
            if bicho.esAgresivo():
                bichoAgresivo+=1
            else:
                bichoPerezoso+=1
        self.assertEqual(bichoAgresivo, 2)
        print("Hay 2 bichos agresivos: ",Fore.GREEN+"Correct"+ Style.RESET_ALL)
        self.assertEqual(bichoPerezoso, 2)
        print("Hay 2 bichos perezosos: ",Fore.GREEN+"Correct"+ Style.RESET_ALL)
        print("\nBichos: ",Fore.GREEN+"Correct"+ Style.RESET_ALL)
        
        bichoAgresivo = self.juego.bichos[0]
        self.assertEqual(bichoAgresivo is not None, True)
        print(Fore.MAGENTA+"\nBicho agresivo:"+ Style.RESET_ALL)
        self.assertEqual(bichoAgresivo.esAgresivo(), True)
        print("El bicho es agresivo: ",Fore.GREEN+"Correct"+ Style.RESET_ALL)

    def testTunel(self):
            print(Fore.MAGENTA+"\nTunel:"+ Style.RESET_ALL)
            tunel = None
            for habitacion in self.juego.laberinto.hijos:
                for hijo in habitacion.hijos:
                    if hijo.esTunel():
                        tunel = hijo
                        break
            self.assertIsNotNone(tunel)
            print("El tunel no es nulo: ",Fore.GREEN+"Correct"+ Style.RESET_ALL)
            self.assertTrue(tunel.esTunel())
            print("El tunel es tunel: ",Fore.GREEN+"Correct"+ Style.RESET_ALL)

    def testArmario(self):
            for habitacion in self.juego.laberinto.hijos:
                for hijo in habitacion.hijos:
                    if hijo.esArmario():
                        print(Fore.MAGENTA+"\nArmario "+str(hijo.num)+":"+ Style.RESET_ALL)
                        self.assertEqual(hijo is not None, True)
                        print("El armario "+str(hijo.num)+" no es nulo: ",Fore.GREEN+"Correct"+ Style.RESET_ALL)
                        self.assertEqual(hijo.esArmario(), True)
                        print("El armario "+str(hijo.num)+" es armario: ",Fore.GREEN+"Correct"+ Style.RESET_ALL)




if __name__ == '__main__':
    unittest.main()
