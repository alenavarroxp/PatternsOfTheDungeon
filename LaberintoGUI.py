import pygame,sys
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
        self.origenX = 10
        self.origenY = 50
        self.pX = 0
        self.pY = 0
        self.habActual = None
        self.person = None
        self.pasadoPuerta = False
        

    def iniciarJuego(self):
        director = Director()
        director.procesar('laberintos/lab4Hab4Arm4HechicerosTunel.json')
        self.juego=director.obtenerJuego()
        self.mostrarLaberinto()
        #Abrir ventana
        self.agregarPersonaje("Mario")
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
        pygame.display.set_caption("Laberinto")
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
        abrirPuertas = pygame.draw.rect(self.screen, (0, 255, 0), (1200, 100, 200, 50))
        abrirPuertasText = fuente.render("Abrir puertas", True, (255, 255, 255))
        self.screen.blit(abrirPuertasText, (abrirPuertas.x + 10, abrirPuertas.y + 10))
        abrir = False

        iniciarJuego = pygame.draw.rect(self.screen, (0, 255, 0), (1200, 150, 200, 50))
        iniciarJuegoText = fuente.render("Iniciar juego", True, (255, 255, 255))
        self.screen.blit(iniciarJuegoText, (iniciarJuego.x + 10, iniciarJuego.y + 10))

        while running:
            #TODO:
            #self.dibujarComandos()
            keys = pygame.key.get_pressed()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.juego.finJuego()
                    pygame.quit()
                    print(self.juego)
                    exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if abrirPuertas.collidepoint(mouse_pos):
                        if not abrir:
                            abrir = True
                            self.juego.abrirPuertas()
                            abrirPuertas = pygame.draw.rect(self.screen, (0, 255, 0), (1200, 100, 200, 50))
                            abrirPuertasText = fuente.render("Cerrar puertas", True, (255, 255, 255))
                            self.screen.blit(abrirPuertasText, (abrirPuertas.x + 10, abrirPuertas.y + 10))
                            self.redibujar()
                        else:
                            abrir = False
                            self.juego.cerrarPuertas()
                            abrirPuertas = pygame.draw.rect(self.screen, (0, 255, 0), (1200, 100, 200, 50))
                            abrirPuertasText = fuente.render("Abrir puertas", True, (255, 255, 255))
                            self.screen.blit(abrirPuertasText, (abrirPuertas.x + 10, abrirPuertas.y + 10))
                            self.redibujar()  
                    if iniciarJuego.collidepoint(mouse_pos):
                        print("Iniciar juego")
                        self.juego.lanzarBichos()
                        self.juego.lanzarHechiceros()

                if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                    self.pX = self.origenX -(30/2) + 50
                    self.pY = self.origenY + ((self.alto)/2) -(30/2)
                    print("ORIGEN X: ",self.origenX,"ORIGEN Y: ",self.origenY, "PUNTO X: ",self.pX,"PUNTO Y: ",self.pY)
                    self.redibujar()
                    self.personaje = principalOesteImage
                    self.comprobarElemento(self.habActual,self.habActual.forma.oeste)
         
                    

                if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                    self.pX = self.origenX - (30/2) - 50 + self.ancho
                    self.pY = self.origenY + ((self.alto)/2) -(30/2)
                    print("ORIGEN X: ",self.origenX,"ORIGEN Y: ",self.origenY, "PUNTO X: ",self.pX,"PUNTO Y: ",self.pY)
                    self.redibujar()
                    self.personaje = principalOesteImage
                    self.personaje = pygame.transform.flip(self.personaje,True,False)
                    self.comprobarElemento(self.habActual,self.habActual.forma.este)
                    
                    
                    
                if keys[pygame.K_UP] or keys[pygame.K_w]:
                    self.pX = self.origenX + (self.ancho/2) - (30/2)
                    self.pY = self.origenY + (self.alto/5) - (30/2)
                    print("ORIGEN X: ",self.origenX,"ORIGEN Y: ",self.origenY, "PUNTO X: ",self.pX,"PUNTO Y: ",self.pY)
                    self.redibujar()
                    self.personaje = principalNorteImage
                    self.comprobarElemento(self.habActual,self.habActual.forma.norte)

                    


                if keys[pygame.K_DOWN] or keys[pygame.K_s]:
                    self.pX = self.origenX + (self.ancho/2) - (30/2)
                    self.pY = self.origenY + (self.alto-85) - (30/2)
                    print("ORIGEN X: ",self.origenX,"ORIGEN Y: ",self.origenY, "PUNTO X: ",self.pX,"PUNTO Y: ",self.pY)
                    self.redibujar()
                    self.personaje = self.principal
                    self.comprobarElemento(self.habActual,self.habActual.forma.sur)

                if keys[pygame.K_l]:
                    self.juego.personaje.atacar()
                    
                    
                        
            
            self.screen.blit(self.personaje,(self.pX,self.pY))
            
           

            pygame.display.update()
            clock.tick(60)

    def update(self):
        self.mostrarVidasPersonaje()
        self.mostrarBichos()
        self.mostrarHechiceros()
        self.redibujar()
        

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
        else:
            hechicero = pygame.image.load("graphics/hechiceroBrujo.png").convert_alpha()
            hechicero = pygame.transform.scale(hechicero,(30*1.75,30*1.75))
            self.screen.blit(hechicero,(unPuntoX+(ancho/3)+150,unPuntoY+(alto/3)))
        
   
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
        else:
            bicho = pygame.image.load("graphics/bichoPerezoso.png").convert_alpha()
            bicho = pygame.transform.scale(bicho,(30*1.75,30*1.75))
            self.screen.blit(bicho,(unPuntoX+(ancho/3)+150,unPuntoY+(alto/3)+80))
        
    def moverPersonajeHabitacion(self):
        self.pX = (self.habActual.forma.puntoX+(self.ancho/2)-30/2) 
        self.pY = self.habActual.forma.puntoY+(self.alto/2)-30/2
        self.origenX = self.habActual.forma.puntoX
        self.origenY = self.habActual.forma.puntoY
        self.personaje  = self.principal
        print(self.juego.personaje.obtenerComandos())
        self.redibujar()
            
    def redibujar(self):
        for hijo in self.juego.laberinto.hijos:
                    self.dibujarContenedorRectangularEscala(hijo,hijo.forma, 1)
                    self.ocultar()
        self.mostrarBichos()
        self.mostrarHechiceros()

    def comprobarElemento(self,unaHabitacion,unaPuerta):
            if unaPuerta.esPuerta():
                if unaPuerta.abierta:
                    print("Puerta abierta")
                    if self.pasadoPuerta:
                        self.habActual = unaPuerta.lado1
                        self.pasadoPuerta = False
                        
                    else:
                        self.habActual = unaPuerta.lado2
                        self.pasadoPuerta = True

                    self.habActual.entrar(self.juego.personaje)
                    self.moverPersonajeHabitacion()

                    
                    print("Estas en la habitacion: ",self.habActual.num)
                else:
                    print("Puerta cerrada")
                    print("Estas en la habitacion: ",self.habActual.num)
            else: 
                print("Te has chocado con una pared")
                print("Estas en la habitacion: ",self.habActual.num)

    def getImage(self,sheet,frame,width,height,scale,colour):
        image = pygame.Surface((width,height)).convert_alpha()
        image.blit(sheet,(0,0),((frame*width),0,width,height))
        image = pygame.transform.scale(image,(width*scale,height*scale))
        image.set_colorkey(colour)
        return image         
    
    def dibujarLaberinto(self):
        if self.juego is None:
            return self
        
        self.juego.laberinto.aceptar(self)
        self.ocultar()
        self.mostrarVidasPersonaje()
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
        self.habActual = self.person.posicion
      
    def ocultar(self):
        ocultar = pygame.Surface((30,self.height-60))
        ocultar.fill((50,50,50))
        self.screen.blit(ocultar,(1140,50))

    def mostrarVidasPersonaje(self):
        if self.vidasM is None:
            return None
        pygame.init()
        miFuente = pygame.font.SysFont('radnika', 30)
        text = miFuente.render("Vidas: " + str(self.person.vidas), True, (255, 0, 0))
        rectText = text.get_rect()
        rectText.center = (80, 30)
        rect = pygame.Rect(rectText.left - 5, rectText.top - 5, rectText.width + 10, rectText.height + 10)
        if pygame.display.get_active():
            pygame.draw.rect(self.screen, (50, 50, 50), rect)  # Dibuja el rectángulo negro detrás del texto
            self.screen.blit(text, rectText)
            pygame.display.update()


    


    def visitarArmario(self,unArmario):
        print('Armario visitado')
        #dibujar
    
    def visitarBomba(self,unaBomba):
        print('Bomba visitada')
        #dibujar

    def visitarBaul(self,unBaul):
        print('Baul visitado')
        #dibujar    
    
    def visitarHabitacion(self,unaHabitacion):
        print('Habitacion visitada')
        #dibujar
        self.dibujarContenedorRectangularEscala(unaHabitacion,unaHabitacion.forma, 1)
        
    
    def visitarPuerta(self,unaPuerta):
        print('Puerta visitada')
        #dibujar
    
    def visitarPared(self,unaPared):
        print('Pared visitada')
        #dibujar
        

    def visitarTunel(self,unTunel):
        print('Tunel visitado')
        #dibujar

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
       self.dibujarPared(unaForma,unPuntoX,unPuntoY,ancho,alto)
       self.dibujarPuerta(unaForma,unPuntoX,unPuntoY,ancho,alto)
       for hijo in unaHab.hijos:
            if hijo.esArmario():
                self.dibujarArmario(hijo.forma,unPuntoX,unPuntoY,ancho,alto)
            if hijo.esBaul():
                self.dibujarBaul(hijo.forma,unPuntoX,unPuntoY,ancho,alto)

    def dibujarArmario(self,unaForma,unPuntoX,unPuntoY,ancho,alto):
        if unaForma.este.esPuerta():
            if unaForma.este.abierta:
                armario = pygame.image.load("graphics/armarioAbierto.png").convert_alpha()
                armario = pygame.transform.scale(armario,(62,83))
                self.screen.blit(armario,(unPuntoX+ancho/2-120,unPuntoY))
            else:
                armario = pygame.image.load("graphics/armarioCerrado.png").convert_alpha()
                armario = pygame.transform.scale(armario,(45,83))
                self.screen.blit(armario,(unPuntoX+ancho/2-110 ,unPuntoY))
    
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
            
            pared1 = pygame.image.load("graphics/paredOeste.png").convert_alpha()
            for y in range(0,(int(unPuntoX/2)-198),22):
                self.screen.blit(pared1,(unPuntoX,unPuntoY+y))
                self.screen.blit(pared1,(unPuntoX,unPuntoY+alto-y-22))

            puertaOeste = pygame.transform.scale(puertaOeste,(12,128))
            self.screen.blit(puertaOeste,(unPuntoX,unPuntoY+alto/2-60))

    
                   
    

vista = LaberintoGUI()
vista.iniciarJuego()
juego = vista.juego
print(vista.juego)

# print("FUENTES",pygame.font.get_fonts())
