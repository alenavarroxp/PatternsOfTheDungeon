from src.model.Final import Final
from src.model.Abrir import Abrir
from src.model.Director import Director
from src.model.Juego import Juego
from src.model.LaberintoFactory import LaberintoFactory
from src.model.Personaje import Personaje
from colorama import init, Fore, Style


while True:
    init()
    metodo = input(Fore.MAGENTA+"¿Quieres usar el builder para crear el laberinto?\n"+Style.RESET_ALL+"1. Sí\n2. No\n")
    metodo = int(metodo)
    if metodo == 1:
        opcion1 = input(Fore.MAGENTA+"¿Qué JSON quieres elegir para crear el laberinto?\n"+Style.RESET_ALL+Fore.LIGHTWHITE_EX+"1. Laberinto 2 habitaciones (VERTICAL)\n2. Laberinto 2 habitacion (HORIZONTAL)\n3. Laberinto 2 habitaciones y 2 armarios\n4. Laberinto 2 habitaciones y 2 bichos\n5. Laberinto 2 habitaciones y tunel\n6. Laberinto 4 habitaciones,4 armarios\n7. Laberinto 4 habitaciones, 4 armarios y 4 bichos\n8. Laberinto 4 habitaciones, 4 armarios, 4 bichos y tunel\n"+Style.RESET_ALL)
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
        opcion = input(Fore.MAGENTA+"¿Qué opción quieres elegir?\n"+Style.RESET_ALL+Fore.LIGHTWHITE_EX+"1. Laberinto 2 habitaciones\n2. EJERCICIO 1: Laberinto 2 habitaciones (Factory Method)\n3. Laberinto 2 habitaciones (FM & Decorator)\n4. Laberinto 4 habitaciones y 4 bichos\n5. Laberinto 4 habitaciones, 4 armarios y 4 bichos\n6. Laberinto 4 habitaciones,4 armarios, 4 bombas y 4 bichos\n7. EJERCICIO 2 Laberinto 4 habitaciones y 2 baúles\n8. Laberinto 4 habitaciones,4 armarios, 4 bombas y 4 bichos (ABSTRACT FACTORY)\n9. Laberinto 2 habitaciones y tienda\n"+Style.RESET_ALL)
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
                8: juego.laberinto4Hab4Arm4Bombas4BichosAF,
                9: juego.laberinto2HabitacionesTienda,
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
    while juego.fase.esFinal() == False:
        if activado:
            if abierto:
                operacion = input(Fore.MAGENTA+"\n¿Qué quieres hacer?\n"+Fore.RED+"0. Atacar\n"+Fore.LIGHTBLUE_EX+"1. Desactivar Todas Las Bombas\n2. Cerrar Todas Las Puertas\n"+Fore.LIGHTGREEN_EX+"3. Lanzar Bichos\n4. Terminar Bichos\n"+Fore.LIGHTWHITE_EX+"5. Añadir personaje\n6. Entrar en tunel\n"+Fore.YELLOW+"7. Añadir monedas al inventario\n8. Quitar monedas del inventario\n"+Fore.BLUE+"9. Abrir Puerta\n"+Fore.CYAN+"10. Mover personaje\n"+Fore.LIGHTMAGENTA_EX+"11. Entrar a la tienda\n"+Fore.WHITE+"12. Salir\n"+Style.RESET_ALL)
            else:
                operacion = input(Fore.MAGENTA+"\n¿Qué quieres hacer?\n"+Fore.RED+"0. Atacar\n"+Fore.LIGHTBLUE_EX+"1. Desactivar Todas Las Bombas\n2. Abrir Todas Las Puertas\n"+Fore.LIGHTGREEN_EX+"3. Lanzar Bichos\n4. Terminar Bichos\n"+Fore.LIGHTWHITE_EX+"5. Añadir personaje\n6. Entrar en tunel\n"+Fore.YELLOW+"7. Añadir monedas al inventario\n8. Quitar monedas del inventario\n"+Fore.BLUE+"9. Abrir Puerta\n"+Fore.CYAN+"10. Mover personaje\n"+Fore.LIGHTMAGENTA_EX+"11. Entrar a la tienda\n"+Fore.WHITE+"12. Salir\n"+Style.RESET_ALL)
        else:
            if abierto:
                operacion = input(Fore.MAGENTA+"\n¿Qué quieres hacer?\n"+Fore.RED+"0. Atacar\n"+Fore.LIGHTBLUE_EX+"1. Activar Todas Las Bombas\n2. Cerrar Todas Las Puertas\n"+Fore.LIGHTGREEN_EX+"3. Lanzar Bichos\n4. Terminar Bichos\n"+Fore.LIGHTWHITE_EX+"5. Añadir personaje\n6. Entrar en tunel\n"+Fore.YELLOW+"7. Añadir monedas al inventario\n8. Quitar monedas del inventario\n"+Fore.BLUE+"9. Abrir Puerta\n"+Fore.CYAN+"10. Mover personaje\n"+Fore.LIGHTMAGENTA_EX+"11. Entrar a la tienda\n"+Fore.WHITE+"12. Salir\n"+Style.RESET_ALL)
            else:
                operacion = input(Fore.MAGENTA+"\n¿Qué quieres hacer?\n"+Fore.RED+"0. Atacar\n"+Fore.LIGHTBLUE_EX+"1. Activar Todas Las Bombas\n2. Abrir Todas Las Puertas\n"+Fore.LIGHTGREEN_EX+"3. Lanzar Bichos\n4. Terminar Bichos\n"+Fore.LIGHTWHITE_EX+"5. Añadir personaje\n6. Entrar en tunel\n"+Fore.YELLOW+"7. Añadir monedas al inventario\n8. Quitar monedas del inventario\n"+Fore.BLUE+"9. Abrir Puerta\n"+Fore.CYAN+"10. Mover personaje\n"+Fore.LIGHTMAGENTA_EX+"11. Entrar a la tienda\n"+Fore.WHITE+"12. Salir\n"+Style.RESET_ALL)

        try:
            operacion = int(operacion)
            if operacion == 0:
                if juego.personaje == None:
                    print("No hay ningun personaje en el laberinto")
                else:
                    juego.personaje.atacar()
            elif operacion == 1:
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
                    hayTunel = False
                    for hab in juego.laberinto.hijos:
                        for tunel in hab.hijos:
                            if tunel.esTunel():
                                hayTunel = True
                                tunel.entrar(personaje)
                                print("Entrando en tunel")
                                break;
                        if hayTunel:
                            break;
                    
                print(juego)
               
            
            elif operacion == 7:
                if juego.personaje != None:
                    print("¿Que monedas quieres añadir al inventario de ",personaje.nickname,'?')
                    kindOfCoin = input("1. Moneda de 1\n2. Moneda de 2\n3. Moneda de 5\n4. Moneda de 10\n")
                    kindOfCoin = int(kindOfCoin)
                    if kindOfCoin == 1:
                        moneda1 = juego.fabricarMoneda(1,juego.personaje.inventario)
                        personaje.cogerObjeto(moneda1)
                        personaje.dinero += moneda1.valor
                        personaje.abrirInventario()
                    elif kindOfCoin == 2:
                        moneda2 = juego.fabricarMoneda(2,juego.personaje.inventario)
                        personaje.cogerObjeto(moneda2)
                        personaje.dinero += moneda2.valor
                        personaje.abrirInventario()
                    elif kindOfCoin == 3:
                        moneda5 = juego.fabricarMoneda(5,juego.personaje.inventario)
                        personaje.cogerObjeto(moneda5)
                        personaje.dinero += moneda5.valor
                        personaje.abrirInventario()
                    elif kindOfCoin == 4:
                        moneda10 = juego.fabricarMoneda(10,juego.personaje.inventario)
                        personaje.cogerObjeto(moneda10)
                        personaje.dinero += moneda10.valor
                        personaje.abrirInventario()
                    else:
                        print("\n\nOpción no válida.\n\n")
                else:
                    print("No hay ningun personaje en el laberinto")

            elif operacion == 8:
                if juego.personaje != None:
                    print("¿Que monedas quieres añadir al inventario de ",personaje.nickname,'?')
                    kindOfCoin = input("1. Moneda de 1\n2. Moneda de 2\n3. Moneda de 5\n4. Moneda de 10\n")
                    kindOfCoin = int(kindOfCoin)
                    if kindOfCoin == 1:
                        personaje.soltarObjeto(moneda1)
                        personaje.abrirInventario()
                    elif kindOfCoin == 2:
                        personaje.soltarObjeto(moneda2)
                        personaje.abrirInventario()
                    elif kindOfCoin == 3:
                        personaje.soltarObjeto(moneda5)
                        personaje.abrirInventario()
                    elif kindOfCoin == 4:
                        personaje.soltarObjeto(moneda10)
                        personaje.abrirInventario()
                    else:
                        print("\n\nOpción no válida.\n\n")
                else:
                    print("No hay ningun personaje en el laberinto")    
            elif operacion == 9:
                if juego.personaje != None:
                    print("¿Que puerta quieres abrir",personaje.nickname,'?')
                    print("El personaje esta en la habitacion: ",personaje.posicion.num)
                    print(personaje.posicion)
                    puerta = input("1. Puerta Norte\n2. Puerta Sur\n3. Puerta Este\n4. Puerta Oeste\n")
                    puerta = int(puerta)
                    if puerta == 1:
                        if juego.personaje.posicion.forma.norte.esPuerta():
                            juego.personaje.posicion.forma.norte.comandos[0].ejecutar(juego.personaje)
                        else:
                            print("No hay puerta en esa dirección")
                    elif puerta == 2:
                        if juego.personaje.posicion.forma.sur.esPuerta():
                            juego.personaje.posicion.forma.sur.comandos[0].ejecutar(juego.personaje)
                        else:
                            print("No hay puerta en esa dirección")
                       
                    elif puerta == 3:
                        if juego.personaje.posicion.forma.este.esPuerta():
                            juego.personaje.posicion.forma.este.comandos[0].ejecutar(juego.personaje)
                        else:
                            print("No hay puerta en esa dirección")                        
                    elif puerta == 4:
                        if juego.personaje.posicion.forma.oeste.esPuerta():
                            juego.personaje.posicion.forma.oeste.comandos[0].ejecutar(juego.personaje)
                        else:
                            print("No hay puerta en esa dirección")
                    else:
                        print("\n\nOpción no válida.\n\n")
                else:
                    print("No hay ningun personaje en el laberinto")
                print(juego)
            elif operacion == 10:
                if juego.personaje != None:
                    print("¿A donde quieres mover a ",personaje.nickname,'?')
                    print("El personaje esta en la habitacion: ",personaje.posicion)
                    direccion = input("W. Norte\nS. Sur\nD. Este\nA. Oeste\n")
                    if direccion == 'W' or direccion == 'w':
                        juego.personaje.irAlNorte()
                    elif direccion == 'S' or direccion == 's':
                        juego.personaje.irAlSur()
                    elif direccion == 'D' or direccion == 'd':
                        juego.personaje.irAlEste()
                    elif direccion == 'A' or direccion == 'a':
                        juego.personaje.irAlOeste()
                    else:
                        print("\n\nOpción no válida.\n\n")
                else:
                    print("No hay ningun personaje en el laberinto")
                print(juego)
            elif operacion == 11:
                existsTienda = False
                if juego.personaje is not None:
                    for hijo in juego.personaje.posicion.hijos:
                        if hijo.esTienda():
                            existsTienda = True
                            hijo.entrar(juego.personaje)
                            print("Entrando a la tienda")
                            while juego.personaje.posicion == hijo:
                                comprar = False
                                print("¿Que quieres hacer en la tienda ",personaje.nickname,'?')
                                accion = input("1. Comprar\n2. Salir\n")
                                accion = int(accion)
                                if accion == 1:
                                    contObjetos = 0
                                    
                                    print("Tienes",juego.personaje.dinero,"de dinero")
                                    print("Hay ",len(hijo.mercader.objetos)," objetos en la tienda")
                                    for objeto in hijo.mercader.objetos:
                                        contObjetos += 1
                                        if juego.personaje.dinero >= objeto.precio:
                                            print(str(contObjetos)+". "+str(objeto)+" (Puedes comprarlo)")
                                            comprar = True
                                        else: 
                                            print(str(contObjetos)+". "+str(objeto))
                                    obj = input("¿Que objeto quieres comprar?\n")
                                    obj = int(obj)
                                    if comprar:
                                        if obj > 0 and obj <= len(hijo.mercader.objetos):
                                            hijo.enteCompraObjeto(juego.personaje,hijo.mercader.objetos[obj-1])
                                        if len(hijo.mercader.objetos) == 0:
                                            print("No hay objetos en la tienda")
                                            hijo.cerrarTienda()
                                            break
                                        else:
                                            print("\n\nPuede seguir comprando objetos en la tienda de "+hijo.mercader.nick+".\n\n")
                                    else:
                                        print("No tienes suficiente dinero")
                                    
                                elif accion == 2:
                                    hijo.salir(juego.personaje)
                                    print("Saliendo de la tienda")

                                
                            break
                    if existsTienda == False:
                        print("No hay tienda en la habitación")
                else:
                    print("No hay ningun personaje en el laberinto")
            elif operacion == 12:
               break;
            else:
                print("\n\nOpción no válida.\n\n")
        except ValueError:
            print("\n\nNo se admiten letras ni otro carácter fuera del rango.\n\n")