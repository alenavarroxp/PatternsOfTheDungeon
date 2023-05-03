from model.Juego import Juego
from model.LaberintoFactory import LaberintoFactory


while True:
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
                operacion = input("¿Qué quieres hacer?\n1. Desactivar Bombas\n2. Cerrar Puertas\n3. Bicho actua\n4. Salir\n")
            else:
                operacion = input("¿Qué quieres hacer?\n1. Desactivar Bombas\n2. Abrir Puertas\n3. Bicho actua\n4. Salir\n")
        else:
            if abierto:
                operacion = input("¿Qué quieres hacer?\n1. Activar Bombas\n2. Cerrar Puertas\n3. Bicho actua\n4. Salir\n")
            else:
                operacion = input("¿Qué quieres hacer?\n1. Activar Bombas\n2. Abrir Puertas\n3. Bicho actua\n4. Salir\n")

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
                        numero = input("¿Qué bicho quieres que actúe?\n1. Bicho1\n2. Bicho2\n3. Bicho3\n4. Bicho4\n")
                        juego.bichos[int(numero)-1].actua()
                        break
                print('\n',juego)
            elif operacion == 4:
                break
            else:
                print("\n\nOpción no válida.\n\n")
        except ValueError:
            print("\n\nNo se admiten letras ni otro carácter fuera del rango.\n\n")