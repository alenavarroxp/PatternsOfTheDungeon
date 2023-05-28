import pygame,sys,os
from src.model.Tienda import Tienda
from src.model.Abierto import Abierto
from src.model.Baul import Baul
from src.model.Vivo import Vivo
from src.model.Armario import Armario
from src.model.Habitacion import Habitacion
from src.model.Sur import Sur
from src.model.Norte import Norte
from src.model.Mago import Mago
from src.model.Agresivo import Agresivo
from src.model.Personaje import Personaje
from src.model.Director import Director


class LaberintoGUI():
    def __init__(self):
        self.juego = None
        self.ancho = 0
        self.alto = 0
        self.width = 1400
        self.height = 700
        self.screen = pygame.display.set_mode((self.width,self.height))
        self.screen.fill((50,50,50))
        self.maxX = 0
        self.maxY = 0
        self.minX = 0
        self.minY = 0
        self.vidasM = 0
        self.poderM = 0
        self.dineroM = 0
        self.origenX = 10
        self.origenY = 50
        self.pX = 0
        self.pY = 0
        self.contActual = None
        self.person = None
        self.pasadoPuerta = False
        self.longitud_comandos_anterior = 0
    
    def pantallaInicial(self):
        pygame.init()
        pygame.font.init()
        self.screen.fill((50, 50, 50))
        pygame.display.set_caption("Patterns of the Dungeon")
        self.screen.blit(pygame.image.load("graphics/Inicio.jpg"), (0, 0))

        empezar = pygame.Surface((250, 75), pygame.SRCALPHA)
        self.screen.blit(empezar, (self.width/2-125, self.height/2+235))

        pygame.display.flip()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.MOUSEMOTION:  # Evento de movimiento del ratón
                    mouse_pos = pygame.mouse.get_pos()
                    if empezar.get_rect(x=self.width/2-125, y=self.height/2+235).collidepoint(mouse_pos):
                        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                    else:
                        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                elif event.type == pygame.MOUSEBUTTONDOWN:  # Evento de clic del ratón
                    mouse_pos = pygame.mouse.get_pos()
                    if empezar.get_rect(x=self.width/2-125, y=self.height/2+235).collidepoint(mouse_pos):
                        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)  # Restaurar el cursor predeterminado
                        self.seleccionarJuego()

    def obtenerLaberintos(self, directorio):
        laberintos = []
        for file in os.listdir(directorio):
            if file.endswith(".json") and "Rombo" not in file:
                laberintos.append(file)
        return laberintos

    def seleccionarJuego(self):
        pygame.init()
        pygame.font.init()
        self.screen.fill((50, 50, 50))
        pygame.display.set_caption("Seleccionar juego - Patterns of the Dungeon")
        self.screen.blit(pygame.image.load("graphics/SeleccionJuego.jpg"), (0, 0))

        seleccionar = pygame.Surface((275, 500), pygame.SRCALPHA)
        self.screen.blit(seleccionar, (self.width - 300, 190))

        directorio = "laberintos/"
        laberintos = self.obtenerLaberintos(directorio)
        laberintos_rects = []
        font = pygame.font.SysFont("Arial", 24)
        seleccionado = None

        scroll_offset = 0  # Desplazamiento del scroll
        max_visible_items = min(8, len(laberintos))  # Número máximo de elementos visibles en la lista
        if scroll_offset + max_visible_items > len(laberintos):
            scroll_offset = max(0, len(laberintos) - max_visible_items)

        imagen_laberinto = None  # Variable para almacenar la imagen del laberinto seleccionado
        rect_preview = pygame.Rect(self.width - 750, self.height // 2 - 191, 674, 382)  # Rectángulo para la vista previa del laberinto

        while True:
            self.screen.fill((50, 50, 50))
            self.screen.blit(pygame.image.load("graphics/SeleccionJuego.jpg"), (0, 0))

            seleccionar = pygame.Surface((275, 500), pygame.SRCALPHA)
            self.screen.blit(seleccionar, (self.width - 300, 190))

            # Dentro del bucle principal
            for i in range(scroll_offset, scroll_offset + max_visible_items):
                if i >= len(laberintos):
                    break
                laberinto = laberintos[i]
                rect = pygame.Rect(30, 190 + ((i - scroll_offset) * 60), 500, 50)
                laberintos_rects.append(rect)
                pygame.draw.rect(self.screen, (255, 255, 255), rect)
                text = font.render(laberinto, True, (0, 0, 0))
                self.screen.blit(text, (rect.x + 10, rect.y + 10))

                # Verificar si el laberinto está seleccionado
                if seleccionado == laberinto:
                    # Rectángulo de resaltado
                    resaltado_rect = pygame.Rect(rect.x, rect.y, rect.width, rect.height)
                    pygame.draw.rect(self.screen, (222, 186, 122), resaltado_rect, 3)

            # Barra de scroll
            scroll_bar_rect = pygame.Rect(self.width - 20, 190, 10, 500)
            pygame.draw.rect(self.screen, (100, 100, 100), scroll_bar_rect)

            # Cálculo del tamaño y posición del scroll thumb
            visible_ratio = max_visible_items / len(laberintos)
            thumb_height = int(scroll_bar_rect.height * visible_ratio)
            thumb_pos = int(scroll_bar_rect.y + (scroll_offset / len(laberintos)) * scroll_bar_rect.height)

            # Scroll thumb
            thumb_rect = pygame.Rect(self.width - 20, thumb_pos, 10, thumb_height)
            pygame.draw.rect(self.screen, (200, 200, 200), thumb_rect)

            if imagen_laberinto is not None:
                self.screen.blit(imagen_laberinto, rect_preview)

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                elif event.type == pygame.MOUSEMOTION:  # Evento de movimiento del ratón
                    mouse_pos = pygame.mouse.get_pos()
                    if seleccionar.get_rect(x=self.width - 300, y=190).collidepoint(mouse_pos):
                        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                    else:
                        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # Botón izquierdo del ratón
                        for i, rect in enumerate(laberintos_rects):
                            if i >= len(laberintos):
                                break
                            if rect.collidepoint(event.pos):
                                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                                seleccionado = laberintos[i + scroll_offset]
                                laberinto_nombre = os.path.splitext(seleccionado)[0]
                                imagen_laberinto = pygame.image.load(f"graphics/preview/{laberinto_nombre}.png")
                                break

                        if seleccionado is not None:
                            if seleccionar.get_rect(x=self.width - 300, y=190).collidepoint(event.pos):
                                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                                self.iniciarJuego(directorio + seleccionado)

                    elif event.button == 4:  # Rueda hacia arriba
                        scroll_offset = max(0, scroll_offset - 1)
                    elif event.button == 5:  # Rueda hacia abajo
                        scroll_offset = min(len(laberintos) - max_visible_items, scroll_offset + 1)
                        if scroll_offset + max_visible_items > len(laberintos):
                            scroll_offset = max(0, len(laberintos) - max_visible_items)

    def iniciarJuego(self,json):
        director = Director()
        director.procesar(json)
        self.juego=director.obtenerJuego()
        self.mostrarLaberinto()
        #Abrir ventana
        self.agregarPersonaje("Mario")
        self.screen.fill((50, 50, 50))
        self.dibujarLaberinto()
        
        self.mostrarVentana()
        
    def mostrarLaberinto(self):
        self.calcularPosicion()
        self.normalizar()
        self.calcularDimensiones()
        self.asignarPuntosReales()

    def calcularPosicion(self):
        if self.juego is None:
            return self
        hab1 = self.juego.obtenerHabitacion(1)
        hab1.forma.puntoX = 0
        hab1.forma.puntoY = 0
        hab1.calcularPosicion()

    def normalizar(self):
        for hijo in self.juego.laberinto.hijos:
            if hijo.forma.puntoX < self.minX:
                self.minX = hijo.forma.puntoX
            if hijo.forma.puntoY < self.minY:
                self.minY = hijo.forma.puntoY

        for hijo in self.juego.laberinto.hijos:
            unPuntoX = hijo.forma.puntoX
            unPuntoY = hijo.forma.puntoY
            hijo.forma.puntoX = abs(unPuntoX + self.minX)
            hijo.forma.puntoY = abs(unPuntoY + self.minY)

    def calcularDimensiones(self):
        
        for hijo in self.juego.laberinto.hijos:
            if hijo.forma.puntoX > self.maxX:
                self.maxX = hijo.forma.puntoX
            if hijo.forma.puntoY > self.maxY:
                self.maxY = hijo.forma.puntoY
        self.maxX += 1
        self.maxY += 1
        self.ancho = round(1130/self.maxX)
        self.alto = round(640/self.maxY)

    def asignarPuntosReales(self):
       
        for hijo in self.juego.laberinto.hijos:
            PuntoX = self.origenX + (hijo.forma.puntoX * self.ancho)
            PuntoY = self.origenY + (hijo.forma.puntoY * self.alto)
            hijo.forma.puntoX = PuntoX
            hijo.forma.puntoY = PuntoY
            hijo.forma.extentX = self.ancho
            hijo.forma.extentY = self.alto

    def mostrarVentana(self):
        pygame.init()
        pygame.display.set_caption("Juego - Patterns of the Dungeon")
        clock = pygame.time.Clock()
        running = True
        self.pX = self.origenX + (self.ancho/2) - (30/2)
        self.pY = self.origenY + (self.alto/2) - (30/2)
        fuente = pygame.font.SysFont('radnika',20)
        self.principal = pygame.image.load("graphics/principal.png").convert_alpha()
        self.principal = pygame.transform.scale(self.principal,(30*1.35,30*1.35))
        self.personaje = self.principal
        self.personaje = pygame.transform.scale(self.personaje,(30*1.35,30*1.35))
        principalOesteImage = pygame.image.load("graphics/principalOeste.png")
        principalOesteImage = pygame.transform.scale(principalOesteImage,(30*1.35,30*1.35))
        principalNorteImage = pygame.image.load("graphics/principalNorte.png")
        principalNorteImage = pygame.transform.scale(principalNorteImage,(30*1.35,30*1.35))
    
        
        self.screen.blit(self.personaje,(self.pX,self.pY))
        # abrirPuertas = pygame.draw.rect(self.screen, (0, 255, 0), (1200, 100, 200, 50))
        # abrirPuertasText = fuente.render("Abrir puertas", True, (255, 255, 255))
        # self.screen.blit(abrirPuertasText, (abrirPuertas.x + 10, abrirPuertas.y + 10))
        # abrir = False

        iniciarJuego = pygame.draw.rect(self.screen, (0, 255, 0), (1200, 550, 200, 50))
        iniciarJuegoText = fuente.render("Iniciar juego", True, (255, 255, 255))
        self.screen.blit(iniciarJuegoText, (iniciarJuego.x + 10, iniciarJuego.y + 10))


        # activarBombas = pygame.draw.rect(self.screen, (0, 255, 0), (1200, 200, 200, 50))
        # activarBombasText = fuente.render("Activar bombas", True, (255, 255, 255))
        # self.screen.blit(activarBombasText, (activarBombas.x + 10, activarBombas.y + 10))
        # activar = False
        
        updateIntervalo = 2000
        lastUpdate = pygame.time.get_ticks()
        self.mouse_pos = None
        while self.juego.fase.esFinal() == False:
            # currentTime = pygame.time.get_ticks()
            
            keys = pygame.key.get_pressed()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.juego.finJuego()
                    pygame.quit()
                    print(self.juego)
                    exit()
                
                
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.mouse_pos = pygame.mouse.get_pos()
                    
                    # if abrirPuertas.collidepoint(self.mouse_pos):
                    #     if not abrir:
                    #         abrir = True
                    #         self.juego.abrirPuertas()
                    #         abrirPuertas = pygame.draw.rect(self.screen, (0, 255, 0), (1200, 100, 200, 50))
                    #         abrirPuertasText = fuente.render("Cerrar puertas", True, (255, 255, 255))
                    #         self.screen.blit(abrirPuertasText, (abrirPuertas.x + 10, abrirPuertas.y + 10))
                    #         self.redibujar()
                    #     else:
                    #         abrir = False
                    #         self.juego.cerrarPuertas()
                    #         abrirPuertas = pygame.draw.rect(self.screen, (0, 255, 0), (1200, 100, 200, 50))
                    #         abrirPuertasText = fuente.render("Abrir puertas", True, (255, 255, 255))
                    #         self.screen.blit(abrirPuertasText, (abrirPuertas.x + 10, abrirPuertas.y + 10))
                    #         self.redibujar()  

                    if iniciarJuego.collidepoint(self.mouse_pos):
                        print("Iniciar juego")
                        self.juego.lanzarBichos()
                        self.juego.lanzarHechiceros()

                    # if activarBombas.collidepoint(self.mouse_pos):
                    #     if not activar:
                    #         activar = True
                    #         self.juego.activarBombas()
                    #         activarBombas = pygame.draw.rect(self.screen, (0, 255, 0), (1200, 200, 200, 50))
                    #         activarBombasText = fuente.render("Desactivar bombas", True, (255, 255, 255))
                    #         self.screen.blit(activarBombasText, (activarBombas.x + 10, activarBombas.y + 10))
                    #         self.redibujar()
                    #     else:
                    #         activar = False
                    #         self.juego.desactivarBombas()
                    #         activarBombas = pygame.draw.rect(self.screen, (0, 255, 0), (1200, 200, 200, 50))
                    #         activarBombasText = fuente.render("Activar bombas", True, (255, 255, 255))
                    #         self.screen.blit(activarBombasText, (activarBombas.x + 10, activarBombas.y + 10))
                    #         self.redibujar()

                if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                    if isinstance(self.contActual,Habitacion):
                        self.pX = self.origenX -(30/2) + 50
                        self.pY = self.origenY + ((self.alto)/2) -(30/2)
                        print("ORIGEN X: ",self.origenX,"ORIGEN Y: ",self.origenY, "PUNTO X: ",self.pX,"PUNTO Y: ",self.pY)
                        self.redibujar()
                        self.personaje = principalOesteImage
                        self.comprobarElemento(self.contActual,self.contActual.forma.oeste)
                        
         
                    

                if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                    if isinstance(self.contActual,Habitacion):
                        self.pX = self.origenX - (30/2) - 50 + self.ancho
                        self.pY = self.origenY + ((self.alto)/2) -(30/2)
                        print("ORIGEN X: ",self.origenX,"ORIGEN Y: ",self.origenY, "PUNTO X: ",self.pX,"PUNTO Y: ",self.pY)
                        self.redibujar()
                        self.personaje = principalOesteImage
                        self.personaje = pygame.transform.flip(self.personaje,True,False)
                        self.comprobarElemento(self.contActual,self.contActual.forma.este)
                    
                if keys[pygame.K_UP] or keys[pygame.K_w]:
                    if isinstance(self.contActual,Habitacion):
                        self.pX = self.origenX + (self.ancho/2) - (30/2)
                        self.pY = self.origenY + (self.alto/5) - (30/2)
                        print("ORIGEN X: ",self.origenX,"ORIGEN Y: ",self.origenY, "PUNTO X: ",self.pX,"PUNTO Y: ",self.pY)
                        self.redibujar()
                        self.personaje = principalNorteImage
                        self.comprobarElemento(self.contActual,self.contActual.forma.norte)

                if keys[pygame.K_DOWN] or keys[pygame.K_s]:
                    if isinstance(self.contActual,Habitacion):
                        self.pX = self.origenX + (self.ancho/2) - (30/2)
                        self.pY = self.origenY + (self.alto-85) - (30/2)
                        print("ORIGEN X: ",self.origenX,"ORIGEN Y: ",self.origenY, "PUNTO X: ",self.pX,"PUNTO Y: ",self.pY)
                        self.redibujar()
                        self.personaje = self.principal
                        self.comprobarElemento(self.contActual,self.contActual.forma.sur)
                        

                if keys[pygame.K_l]:
                    self.juego.personaje.atacar()
                        
                    
                        
            self.dibujarComandos(self.mouse_pos)
            self.screen.blit(self.personaje,(self.pX,self.pY))
            self.mouse_pos = None
           
            # if currentTime - lastUpdate >= updateIntervalo:
            #     self.update()
            #     lastUpdate = currentTime
                
            pygame.display.update()
        self.pantallaFinal()

    def dibujarComandos(self, mouse_pos):
        fuente = pygame.font.SysFont('radnika', 14)

        comandos = self.contActual.obtenerComandos(self.juego.personaje)
        longitud_anterior = self.longitud_comandos_anterior  # Obtener la longitud anterior
        rect_borrar = pygame.Rect(1175, 50, 210, 20 + longitud_anterior * 60)  # Usar la longitud anterior
        pygame.draw.rect(self.screen, (50, 50, 50), rect_borrar)
        
        # if isinstance(self.contActual,Habitacion):

        for i, comando in enumerate(comandos):
            rect_comando = pygame.Rect(1175, 50 + i * 30, 210, 30)

            if mouse_pos is not None and rect_comando.collidepoint(mouse_pos):
                if comando.esComprar() or comando.esAbrir() or comando.esEntrar() or comando.esCerrar() or comando.esActivar() or comando.esDesactivar():
                    comando.ejecutar(self.juego.personaje)
                    self.moverPersonajeHabitacion()
                self.redibujar()
            else:
                pygame.draw.rect(self.screen, (50, 50, 50), rect_comando)

            pygame.draw.rect(self.screen, (0, 255, 0), rect_comando)
            comando_texto = fuente.render(str(comando), True, (255, 255, 255))
            self.screen.blit(comando_texto, (rect_comando.x + 5, rect_comando.y + 5))

        self.longitud_comandos_anterior = len(comandos)  # Almacenar la longitud actual para usar en la siguiente iteración
        pygame.display.update()

    def pantallaFinal(self):
        pygame.init()
        pygame.font.init()
        self.screen.fill((50, 50, 50))
        pygame.display.set_caption("Fin del juego - Patterns of the Dungeon")
       
        if self.juego.personaje is not None:
            self.__init__()
            self.screen.blit(pygame.image.load("graphics/FinDeJuego.jpg"), (0, 0))
        else:
            self.__init__()
            self.screen.blit(pygame.image.load("graphics/FinDeJuegoPerder.jpg"), (0, 0))
        

        volver = pygame.Surface((450, 50), pygame.SRCALPHA)
        self.screen.blit(volver, (self.width/2-225, self.height/2+240))

        pygame.display.flip()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.MOUSEMOTION:  # Evento de movimiento del ratón
                    mouse_pos = pygame.mouse.get_pos()
                    if volver.get_rect(x=self.width/2-125, y=self.height/2+235).collidepoint(mouse_pos):
                        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                    else:
                        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                elif event.type == pygame.MOUSEBUTTONDOWN:  # Evento de clic del ratón
                    mouse_pos = pygame.mouse.get_pos()
                    if volver.get_rect(x=self.width/2-125, y=self.height/2+235).collidepoint(mouse_pos):
                        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)  # Restaurar el cursor predeterminado
                        self.pantallaInicial()


    def update(self):
        if self.juego is not None:
            self.mostrarVidasPersonaje()
            self.mostrarPoderPersonaje()
            self.mostrarDineroPersonaje()
            # self.mostrarPersonaje()
            self.mostrarBichos()
            self.mostrarHechiceros()
            self.redibujar()
            
    # def mostrarPersonaje(self):
    #     self.dibujarPersonaje(self.juego.personaje)

    # def dibujarPersonaje(self,personaje):
        # self.principal = pygame.image.load("graphics/principal.png").convert_alpha()
        # self.principal = pygame.transform.scale(self.principal,(30*1.35,30*1.35))
        # self.personaje = self.principal
        # self.personaje = pygame.transform.scale(self.personaje,(30*1.35,30*1.35))


    def mostrarHechiceros(self):
        for hechicero in self.juego.hechiceros:
            self.dibujarHechicero(hechicero)

    def dibujarHechicero(self,unHechicero):
        unPuntoX = unHechicero.posicion.forma.puntoX
        unPuntoY = unHechicero.posicion.forma.puntoY
        ancho = unHechicero.posicion.forma.extentX
        alto = unHechicero.posicion.forma.extentY

        if isinstance(unHechicero.modohechicero,Mago):
            hechicero = pygame.image.load("graphics/hechiceroMago.png").convert_alpha()
            hechicero = pygame.transform.scale(hechicero,(30*2,30*2))
            hechicero = pygame.transform.flip(hechicero,True,False)
            self.screen.blit(hechicero,(unPuntoX+(ancho/3)-10,unPuntoY+(alto/3)+80))
            self.mostrarVidasEnemigo(unHechicero,unPuntoX+(ancho/3)-10,unPuntoY+(alto/3)+80)
        else:
            hechicero = pygame.image.load("graphics/hechiceroBrujo.png").convert_alpha()
            hechicero = pygame.transform.scale(hechicero,(30*1.75,30*1.75))
            self.screen.blit(hechicero,(unPuntoX+(ancho/3)+150,unPuntoY+(alto/3)))
            self.mostrarVidasEnemigo(unHechicero,unPuntoX+(ancho/3)+150,unPuntoY+alto/3)
        
   
    def mostrarBichos(self):
        for bicho in self.juego.bichos:
            self.dibujarBicho(bicho)

    
    def dibujarBicho(self,unBicho):
        unPuntoX = unBicho.posicion.forma.puntoX
        unPuntoY = unBicho.posicion.forma.puntoY
        ancho = unBicho.posicion.forma.extentX
        alto = unBicho.posicion.forma.extentY

        if isinstance(unBicho.modo,Agresivo):
            bicho = pygame.image.load("graphics/bichoAgresivo.png").convert_alpha()
            bicho = pygame.transform.scale(bicho,(30*1.75,30*1.75))
            bicho = pygame.transform.flip(bicho,True,False)
            self.screen.blit(bicho,(unPuntoX+ancho/3,unPuntoY+alto/3))
            self.mostrarVidasEnemigo(unBicho,unPuntoX+ancho/3,unPuntoY+alto/3)
        else:
            bicho = pygame.image.load("graphics/bichoPerezoso.png").convert_alpha()
            bicho = pygame.transform.scale(bicho,(30*1.75,30*1.75))
            self.screen.blit(bicho,(unPuntoX+(ancho/3)+150,unPuntoY+(alto/3)+80))
            self.mostrarVidasEnemigo(unBicho,unPuntoX+(ancho/3)+150,unPuntoY+(alto/3)+70)
    
    def mostrarVidasEnemigo(self,unEnemigo,unPuntoX,unPuntoY):
        vida = pygame.Surface((65,1), pygame.SRCALPHA)
        if isinstance(unEnemigo.estado,Vivo):
            if unEnemigo.vidas == 50:
                vida = pygame.image.load("graphics/50L.jpg").convert_alpha()
            elif unEnemigo.vidas == 40:
                vida = pygame.image.load("graphics/40L.jpg").convert_alpha()
            elif unEnemigo.vidas == 30:
                vida = pygame.image.load("graphics/30L.jpg").convert_alpha()
            elif unEnemigo.vidas == 20:
                vida = pygame.image.load("graphics/20L.jpg").convert_alpha()
            elif unEnemigo.vidas == 10:
                vida = pygame.image.load("graphics/10L.jpg").convert_alpha()
            elif unEnemigo.vidas <= 0:
                vida = pygame.Surface((65,1), pygame.SRCALPHA)
                
                
            vida = pygame.transform.scale(vida,(65,1))
            self.screen.blit(vida,(unPuntoX,unPuntoY))
        pass
        

    def moverPersonajeHabitacion(self):
        self.contActual = self.juego.personaje.posicion
        if isinstance(self.contActual,Armario):
            self.pX = (self.contActual.padre.forma.puntoX+self.contActual.padre.forma.extentX-67)
            self.pY = self.contActual.padre.forma.puntoY+63
            self.origenX = self.contActual.padre.forma.puntoX
            self.origenY = self.contActual.padre.forma.puntoY

        elif isinstance(self.contActual,Baul):
            self.pX = (self.contActual.padre.forma.puntoX+self.contActual.padre.forma.extentX/2-173)
            self.pY = self.contActual.padre.forma.puntoY+26
            self.origenX = self.contActual.padre.forma.puntoX
            self.origenY = self.contActual.padre.forma.puntoY
        elif isinstance(self.contActual,Tienda):
            self.pX = (self.contActual.padre.forma.puntoX+self.contActual.padre.forma.extentX-70)
            self.pY = self.contActual.padre.forma.puntoY+self.contActual.padre.forma.extentY-70
            self.origenX = self.contActual.padre.forma.puntoX
            self.origenY = self.contActual.padre.forma.puntoY

        else:
            self.pX = (self.contActual.forma.puntoX+(self.ancho/2)-30/2) 
            self.pY = self.contActual.forma.puntoY+(self.alto/2)-30/2
            self.origenX = self.contActual.forma.puntoX
            self.origenY = self.contActual.forma.puntoY
        self.personaje  = self.principal
        self.redibujar()
            
    def redibujar(self):
        self.juego.laberinto.aceptar(self)
        self.ocultar()
        # self.mostrarPersonaje()
        self.mostrarBichos()
        self.mostrarHechiceros()

    def comprobarElemento(self,unContenedor,unaPuerta):
            if unaPuerta.esPuerta():
                if unaPuerta.abierta:
                    print("Puerta abierta")
                    if self.pasadoPuerta:
                        self.contActual = unaPuerta.lado1
                        self.pasadoPuerta = False
                        
                    else:
                        self.contActual = unaPuerta.lado2
                        self.pasadoPuerta = True

                    comandos = unaPuerta.obtenerComandos(self.juego.personaje)

                    for i, comando in enumerate(comandos):
                    
                        if comando.esEntrar():
                            comando.ejecutar(self.juego.personaje)
                            self.moverPersonajeHabitacion()
                            self.redibujar()
                            break

                    
                    print("Estas en la habitacion: ",self.contActual.num)
                else:
                    print("Puerta cerrada")
                    print("Estas en la habitacion: ",self.contActual.num)
            else: 
                print("Te has chocado con una pared")
                print("Estas en la habitacion: ",self.contActual.num)
        
    
    def dibujarLaberinto(self):
        if self.juego is None:
            return self
        self.juego.laberinto.aceptar(self)
        self.ocultar()
        self.mostrarVidasPersonaje()
        self.mostrarPoderPersonaje()
        self.mostrarDineroPersonaje()
        # Meter aqui los botones del menú
        
        self.mostrarBichos()
        self.mostrarHechiceros()


    def agregarPersonaje(self,unaCadena):
        personaje = Personaje()
        personaje.nickname = unaCadena
        self.juego.agregarPersonaje(personaje)
        self.person = self.juego.personaje
        self.person.añadirDependencia(self)
        self.vidasM = self.person.vidas
        self.poderM = self.person.poder
        self.dineroM = self.person.dinero
        self.contActual = self.person.posicion
      
    def ocultar(self):
        ocultar = pygame.Surface((30,self.height-60))
        ocultar.fill((50,50,50))
        self.screen.blit(ocultar,(1140,50))

    def mostrarVidasPersonaje(self):
        if self.vidasM is None or self.person is None:
            return None
        pygame.init()
        miFuente = pygame.font.SysFont('radnika', 30)
        text = miFuente.render("Vidas: " + str(self.person.vidas), True, (255, 0, 0))
        rectText = text.get_rect()
        rectText.center = (80, 30)
        rect = pygame.Rect(rectText.left - 5, rectText.top - 5, rectText.width + 10, rectText.height + 7)
        if pygame.display.get_active():
            pygame.draw.rect(self.screen, (50, 50, 50), rect)  # Dibuja el rectángulo negro detrás del texto
            self.screen.blit(text, rectText)
            pygame.display.update()

    def mostrarPoderPersonaje(self):
        if self.poderM is None or self.person is None:
            return None
        pygame.init()
        miFuente = pygame.font.SysFont('radnika', 30)
        text = miFuente.render("Poder: " + str(self.person.poder), True, (255, 0, 0))
        rectText = text.get_rect()
        rectText.center = (240, 30)
        rect = pygame.Rect(rectText.left - 5, rectText.top - 5, rectText.width + 10, rectText.height + 7)
        if pygame.display.get_active():
            pygame.draw.rect(self.screen, (50, 50, 50), rect)  # Dibuja el rectángulo negro detrás del texto
            self.screen.blit(text, rectText)
            pygame.display.update()

    def mostrarDineroPersonaje(self):
        if self.dineroM is None or self.person is None:
            return None
        pygame.init()
        miFuente = pygame.font.SysFont('radnika', 30)
        text = miFuente.render("Dinero: " + str(self.person.dinero), True, (255, 0, 0))
        rectText = text.get_rect()
        rectText.center = (400, 30)
        rect = pygame.Rect(rectText.left - 5, rectText.top - 5, rectText.width + 10, rectText.height + 7)
        if pygame.display.get_active():
            pygame.draw.rect(self.screen, (50, 50, 50), rect)  # Dibuja el rectángulo negro detrás del texto
            self.screen.blit(text, rectText)
            pygame.display.update()


    def visitarArmario(self,unArmario):
        # print('Armario visitado')
        #dibujar
        unPuntoX = unArmario.padre.forma.puntoX
        unPuntoY = unArmario.padre.forma.puntoY
        ancho = unArmario.padre.forma.extentX
        alto = unArmario.padre.forma.extentY
        self.dibujarArmario(unArmario.forma,unPuntoX,unPuntoY,ancho,alto)
    
    def visitarBomba(self,unaBomba):
        print('Bomba visitada')
        #dibujar
        unPuntoX = unaBomba.padre.forma.puntoX
        unPuntoY = unaBomba.padre.forma.puntoY
        ancho = unaBomba.padre.forma.extentX
        alto = unaBomba.padre.forma.extentY
        self.dibujarBomba(unaBomba, unPuntoX,unPuntoY,ancho,alto)

    def dibujarBomba(self,unaBomba,unPuntoX,unPuntoY,ancho,alto):
        if unaBomba.activa:
                bomba = pygame.image.load("graphics/bombActive.png").convert_alpha()
                bomba = pygame.transform.scale(bomba,(100,100))
                self.screen.blit(bomba,(unPuntoX+ancho/2+50,unPuntoY+20))
        else:
                bomba = pygame.image.load("graphics/bombNoActive.png").convert_alpha()
                bomba = pygame.transform.scale(bomba,(100,100))
                self.screen.blit(bomba,(unPuntoX+ancho/2+50 ,unPuntoY+20))

    def visitarBaul(self,unBaul):
        # print('Baul visitado')
        #dibujar    
        unPuntoX = unBaul.padre.forma.puntoX
        unPuntoY = unBaul.padre.forma.puntoY
        ancho = unBaul.padre.forma.extentX
        alto = unBaul.padre.forma.extentY
        self.dibujarBaul(unBaul.forma,unPuntoX,unPuntoY,ancho,alto)
    
    def visitarHabitacion(self,unaHabitacion):
        # print('Habitacion visitada')
        #dibujar
        self.dibujarContenedorRectangularEscala(unaHabitacion,unaHabitacion.forma, 1)
        
    
    def visitarPuerta(self,unaPuerta):
        # print('Puerta visitada')
        # #dibujar
        # puntoX = unaPuerta.padre.forma.puntoX
        # puntoY = unaPuerta.padre.forma.puntoY
        # extentX =unaPuerta.padre.forma.extentX
        # extentY =unaPuerta.padre.forma.extentY
        # if isinstance(unaPuerta.padre, Habitacion):
        #     self.dibujarPuerta(unaPuerta.padre.forma,puntoX,puntoY,extentX,extentY)
        pass
    
    def visitarPared(self,unaPared):
        # print('Pared visitada')
        #dibujar
        puntoX = unaPared.padre.forma.puntoX
        puntoY = unaPared.padre.forma.puntoY
        extentX = unaPared.padre.forma.extentX
        extentY = unaPared.padre.forma.extentY
        self.dibujarPared(unaPared.padre.forma,puntoX,puntoY,extentX,extentY)
        

    def visitarTunel(self,unTunel):
        # print('Tunel visitado')
        #dibujar
        self.dibujarTunel(unTunel.padre)

    def dibujarTunel(self,unaHab):
        archivo = "graphics/tunel.png"
        #rotar
        imagen = pygame.image.load(archivo).convert_alpha()
        imagen = pygame.transform.rotate(imagen, -180)
        imagen = pygame.transform.scale(imagen,(50,50))
        self.screen.blit(imagen,(unaHab.forma.puntoX,unaHab.forma.puntoY+unaHab.forma.extentY-60))
    
    def visitarTienda(self,unaTienda):
        print("Tienda visitada")
        unPuntoX = unaTienda.padre.forma.puntoX
        unPuntoY = unaTienda.padre.forma.puntoY
        ancho = unaTienda.padre.forma.extentX
        alto = unaTienda.padre.forma.extentY
        self.dibujarTienda(unaTienda,unPuntoX,unPuntoY,ancho,alto)

    def dibujarTienda(self,unaTienda,unPuntoX,unPuntoY,ancho,alto):
        if isinstance(unaTienda.estadoTienda,Abierto):  
            tienda = pygame.image.load("graphics/tiendaOpen.png").convert_alpha()
            tienda = pygame.transform.scale(tienda,(100,100))
            self.screen.blit(tienda,(unPuntoX+ancho-120,unPuntoY+alto-120))
        else:
            tienda = pygame.image.load("graphics/tiendaClose.png").convert_alpha()
            tienda = pygame.transform.scale(tienda,(100,100))
            self.screen.blit(tienda,(unPuntoX+ancho-120,unPuntoY+alto-120))
       

    def dibujarContenedorRectangularEscala(self,unaHab,unaForma,escala):
       unPuntoX = unaForma.puntoX
       unPuntoY = unaForma.puntoY
       ancho = (unaForma.extentX)/escala
       alto = (unaForma.extentY)/escala

       unaForma.extentX = ancho
       unaForma.extentY = alto
       
       suelo = pygame.image.load("graphics/suelo.png").convert_alpha()

       if self.juego.laberinto.hijos.__len__() == 4:
        rect =pygame.Rect(unPuntoX,unPuntoY,ancho,alto)
        pygame.draw.rect(self.screen,(255,0,0),rect)
        if unPuntoX == 10 and unPuntoY == 50:
                suelo = pygame.image.load("graphics/suelo.png").convert_alpha()
        if unPuntoX == 10 and unPuntoY == 370:
                suelo = pygame.image.load("graphics/suelo2.png").convert_alpha()
        if unPuntoX == 575 and unPuntoY == 50:
                suelo = pygame.image.load("graphics/suelo3.png").convert_alpha()
        if unPuntoX == 575 and unPuntoY == 370:
                suelo = pygame.image.load("graphics/suelo4.png").convert_alpha()

       suelo = pygame.transform.scale(suelo,(64,64))
       for x in range(0, int(ancho), 64):
            for y in range(0, int(alto), 64):
                self.screen.blit(suelo,(unPuntoX+x,unPuntoY+y))
       rect = pygame.Surface((ancho,alto),pygame.SRCALPHA)
       
       pygame.draw.rect(rect,(0,0,0),rect.get_rect(),2)
       self.screen.blit(rect,(unPuntoX,unPuntoY))        
    #    self.dibujarPared(unaForma,unPuntoX,unPuntoY,ancho,alto)
       self.dibujarPuerta(unaForma,unPuntoX,unPuntoY,ancho,alto)
    #    for hijo in unaHab.hijos:
    #         if hijo.esArmario():
    #             self.dibujarArmario(hijo.forma,unPuntoX,unPuntoY,ancho,alto)
    #         if hijo.esBaul():
    #             self.dibujarBaul(hijo.forma,unPuntoX,unPuntoY,ancho,alto)

    def dibujarArmario(self,unaForma,unPuntoX,unPuntoY,ancho,alto):
        if unaForma.este.esPuerta():
            if unaForma.este.abierta:
                armario = pygame.image.load("graphics/armarioAbierto.png").convert_alpha()
                armario = pygame.transform.scale(armario,(62,83))
                self.screen.blit(armario,(unPuntoX+ancho-80,unPuntoY+30))
            else:
                armario = pygame.image.load("graphics/armarioCerrado.png").convert_alpha()
                armario = pygame.transform.scale(armario,(45,83))
                self.screen.blit(armario,(unPuntoX+ancho-70 ,unPuntoY+30))
    
    def dibujarBaul(self,unaForma,unPuntoX,unPuntoY,ancho,alto):
        if unaForma.este.esPuerta():
            if unaForma.este.abierta:
                baul = pygame.image.load("graphics/baulAbierto.png").convert_alpha()
                baul = pygame.transform.scale(baul,(14*2.5,12*2.5))
                self.screen.blit(baul,(unPuntoX+ancho/2-170,unPuntoY+30))
            else:
                baul = pygame.image.load("graphics/baulCerrado.png").convert_alpha()
                baul = pygame.transform.scale(baul,(14*2.5,12*2.5))
                self.screen.blit(baul,(unPuntoX+ancho/2-170 ,unPuntoY+30))
            
    
    def dibujarPared(self,unaForma,unPuntoX,unPuntoY,ancho,alto):
       if unaForma.norte.esPared():
            pared = pygame.image.load("graphics/paredNorte.png").convert_alpha()
            for x in range(0,int(ancho),21):
                    self.screen.blit(pared,(unPuntoX+x,unPuntoY))
       if unaForma.sur.esPared():
            pared = pygame.image.load("graphics/paredSur.png").convert_alpha()
            for x in range(0,int(ancho),21):
                    self.screen.blit(pared,(unPuntoX+x,unPuntoY+alto-4))
       if unaForma.este.esPared():
            pared = pygame.image.load("graphics/paredEste.png").convert_alpha()
            for y in range(0,int(alto)-21,21):
                    self.screen.blit(pared,(unPuntoX+ancho-11,unPuntoY+y))
       if unaForma.oeste.esPared():
            pared = pygame.image.load("graphics/paredOeste.png").convert_alpha()
            for y in range(0,int(alto)-21,21):
                self.screen.blit(pared,(unPuntoX,unPuntoY+y))

    def dibujarPuerta(self,unaForma,unPuntoX,unPuntoY,ancho,alto):
       if unaForma.norte.esPuerta():
            if unaForma.norte.abierta:
                puertaNorte = pygame.image.load("graphics/puertaNorteAbierta.png").convert_alpha()
            else:
                puertaNorte = pygame.image.load("graphics/puertaNorte.png").convert_alpha()
            # colocar la puerta en el medio del ancho de la habitacion
            
            puertaNorte = pygame.transform.scale(puertaNorte,(128,64))
            self.screen.blit(puertaNorte,(unPuntoX+ancho/2-60,unPuntoY-64))
       if unaForma.oeste.esPuerta():
            if unaForma.oeste.abierta:
                puertaOeste = pygame.image.load("graphics/puertaOesteAbierta.png").convert_alpha()

            else:
                puertaOeste = pygame.image.load("graphics/puertaOeste.png").convert_alpha()
        
            puertaOeste = pygame.transform.scale(puertaOeste,(12,128))
            self.screen.blit(puertaOeste,(unPuntoX,unPuntoY+alto/2-60))





vista = LaberintoGUI()
vista.pantallaInicial()

juego = vista.juego
print(vista.juego)

# print("FUENTES",pygame.font.get_fonts())
