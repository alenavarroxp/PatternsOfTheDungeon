from src.model.Director import Director
from src.model.Juego import Juego
from src.model.LaberintoFactory import LaberintoFactory
from src.model.Personaje import Personaje


while True:
    metodo = input("¿Quieres usar el builder para crear el laberinto?\n1. Sí\n2. No\n")
    metodo = int(metodo)
    if metodo == 1:
        opcion1 = input("¿Qué JSON quieres elegir para crear el laberinto?\n1. Laberinto 2 habitaciones (VERTICAL)\n2. Laberinto 2 habitacion (HORIZONTAL)\n3. Laberinto 2 habitaciones y 2 armarios\n4. Laberinto 2 habitaciones y 2 bichos\n5. Laberinto 2 habitaciones y tunel\n6. Laberinto 4 habitaciones,4 armarios\n7. Laberinto 4 habitaciones, 4 armarios y 4 bichos\n8. Laberinto 4 habitaciones, 4 armarios, 4 bichos y tunel\n")
        opcion1 = int(opcion1)
        switch = {
            1: 'laberintos/lab2HabVertical.json',
            2: 'laberintos/lab2HabHorizontal.json',
            3: 'laberintos/lab2Hab2Arm.json',
            4: 'laberintos/lab2Hab2Bichos.json',
            5: 'laberintos/lab2HabTunel.json',
            6: 'laberintos/lab4Hab4Arm.json',
            7: 'laberintos/lab4Hab4Arm4Bichos.json',
            8: 'laberintos/lab4Hab4Arm4BichosTunel.json'
        }
        unArchivo = switch.get(opcion1, "\n\nEl carácter ingresado no es correcto.\n\n")
        director = Director()
        director.procesar(unArchivo)
        juego = director.builder.juego
        print(juego)
    else:
        juego = Juego()
        opcion = input("¿Qué opción quieres elegir?\n1. Laberinto 2 habitaciones\n2. EJERCICIO 1: Laberinto 2 habitaciones (Factory Method)\n3. Laberinto 2 habitaciones (FM & Decorator)\n4. Laberinto 4 habitaciones y 4 bichos\n5. Laberinto 4 habitaciones, 4 armarios y 4 bichos\n6. Laberinto 4 habitaciones,4 armarios, 4 bombas y 4 bichos\n7. EJERCICIO 2 Laberinto 4 habitaciones y 2 baúles\n8. Laberinto 4 habitaciones,4 armarios, 4 bombas y 4 bichos (ABSTRACT FACTORY)\n")
        try:
            opcion = int(opcion)
            switch = {
                1: juego.laberinto2Habitaciones,
                2: juego.laberinto2HabitacionesFM,
                3: juego.laberinto2HabitacionesFMDecorator,
                4: juego.laberinto4Hab4BichosFM,
                5: juego.laberinto4Hab4Arm4BichosFM,
                6: juego.laberinto4Hab4Arm4Bombas4BichosFM,
                7: juego.laberinto4Hab2baules,
                8: juego.laberinto4Hab4Arm4Bombas4BichosAF
            }
            resultado = switch.get(opcion, "\n\nEl carácter ingresado no es correcto.\n\n")
            if resultado == "\n\nEl carácter ingresado no es correcto.\n\n":
                print(resultado)
            else:
                if opcion == 8:
                    af = LaberintoFactory()
                    resultado(af)
                    print(juego)
                    print("------------------------------------------------")
                else:
                    resultado()
                    print(juego)
                    print("------------------------------------------------")
        except ValueError:
            print("\n\nNo se admiten letras ni otro carácter fuera del rango.\n\n")
    activado = False
    abierto = False
    while True:
        if activado:
            if abierto:
                operacion = input("¿Qué quieres hacer?\n1. Desactivar Bombas\n2. Cerrar Puertas\n3. Lanzar Bichos\n4. Terminar Bichos\n5. Añadir personaje\n6. Entrar en tunel\n7. Añadir monedas a la mochila\n8. Quitar monedas de la mochila\n9. Salir")
            else:
                operacion = input("¿Qué quieres hacer?\n1. Desactivar Bombas\n2. Abrir Puertas\n3. Lanzar Bichos\n4. Terminar Bichos\n5. Añadir personaje\n6. Entrar en tunel\n7. Añadir monedas a la mochila\n8. Quitar monedas de la mochila\n9. Salir")
        else:
            if abierto:
                operacion = input("¿Qué quieres hacer?\n1. Activar Bombas\n2. Cerrar Puertas\n3. Lanzar Bichos\n4. Terminar Bichos\n5. Añadir personaje\n6. Entrar en tunel\n7. Añadir monedas a la mochila\n8. Quitar monedas de la mochila\n9. Salir\n")
            else:
                operacion = input("¿Qué quieres hacer?\n1. Activar Bombas\n2. Abrir Puertas\n3. Lanzar Bichos\n4. Terminar Bichos\n5. Añadir personaje\n6. Entrar en tunel\n7. Añadir monedas a la mochila\n8. Quitar monedas de la mochila\n9. Salir\n")

        try:
            operacion = int(operacion)
            if operacion == 1:
                if activado:
                    juego.desactivarBombas()
                    activado = False
                else:
                    juego.activarBombas()
                    activado = True
                print(juego)
            elif operacion == 2:
                if abierto:
                    juego.cerrarPuertas()
                    abierto = False
                else:
                    juego.abrirPuertas()
                    abierto = True
                print(juego)
            elif operacion == 3:
                while True:
                    if len(juego.bichos) == 0:
                        print("\n\nNo hay bichos en el laberinto.\n\n")
                        break
                    else:
                        juego.lanzarBichos()
                        print("Todos los bichos lanzados")
                        break
                print('\n',juego)
            elif operacion == 4:
                juego.terminarBichos()
                print("Todos los hilos terminados")
            elif operacion == 5:
                personaje = Personaje()
                personaje.nickname = input("¿Cuál es tu nickname?\n")
                personaje.poder = input("¿Cuánto es tu poder?(0-100)\n")
                personaje.vidas = input("¿Cuántas vidas tienes?(0-100)\n")
                juego.agregarPersonaje(personaje)
                print("Personaje ",personaje.nickname," añadido al laberinto")
                print(juego)
            elif operacion == 6:
                
                if juego.personaje == None:
                    print("No hay ningun personaje en el laberinto")
                else:
                    
                    #Prueba de movimiento
                    #juego.personaje.irAlSur()
                    #TODO: Entrar a tunel BIEN HECHO (Esto solo para prueba)
                    juego.laberinto.hijos[0].hijos[1].entrar(personaje)
                print(juego)
               
            
            elif operacion == 7:
                if juego.personaje != None:
                    print("¿Que monedas quieres añadir a la mochila de ",personaje.nickname,'?')
                    kindOfCoin = input("1. Moneda de 1\n2. Moneda de 2\n3. Moneda de 5\n4. Moneda de 10\n")
                    kindOfCoin = int(kindOfCoin)
                    if kindOfCoin == 1:
                        moneda1 = juego.fabricarMoneda(1)
                        personaje.agregarObjeto(moneda1)
                        personaje.abrirMochila()
                    elif kindOfCoin == 2:
                        moneda2 = juego.fabricarMoneda(2)
                        personaje.agregarObjeto(moneda2)
                        personaje.abrirMochila()
                    elif kindOfCoin == 3:
                        moneda5 = juego.fabricarMoneda(5)
                        personaje.agregarObjeto(moneda5)
                        personaje.abrirMochila()
                    elif kindOfCoin == 4:
                        moneda10 = juego.fabricarMoneda(10)
                        personaje.agregarObjeto(moneda10)
                        personaje.abrirMochila()
                    else:
                        print("\n\nOpción no válida.\n\n")
                else:
                    print("No hay ningun personaje en el laberinto")

            elif operacion == 8:
                if juego.personaje != None:
                    print("¿Que monedas quieres añadir a la mochila de ",personaje.nickname,'?')
                    kindOfCoin = input("1. Moneda de 1\n2. Moneda de 2\n3. Moneda de 5\n4. Moneda de 10\n")
                    kindOfCoin = int(kindOfCoin)
                    if kindOfCoin == 1:
                        personaje.quitarObjeto(moneda1)
                        personaje.abrirMochila()
                    elif kindOfCoin == 2:
                        personaje.quitarObjeto(moneda2)
                        personaje.abrirMochila()
                    elif kindOfCoin == 3:
                        personaje.quitarObjeto(moneda5)
                        personaje.abrirMochila()
                    elif kindOfCoin == 4:
                        personaje.quitarObjeto(moneda10)
                        personaje.abrirMochila()
                    else:
                        print("\n\nOpción no válida.\n\n")
                else:
                    print("No hay ningun personaje en el laberinto")    
            elif operacion == 9:
               break;
            else:
                print("\n\nOpción no válida.\n\n")
        except ValueError:
            print("\n\nNo se admiten letras ni otro carácter fuera del rango.\n\n")