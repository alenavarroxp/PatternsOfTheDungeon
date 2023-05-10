import pygame,sys
from model.Personaje import Personaje
from model.Director import Director


class LaberintoGUI():
    def __init__(self):
        self.juego = None
        self.ancho = 0
        self.alto = 0
        self.width = 1200
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
        director.procesar('laberintos/lab4Hab4Arm4BichosTunel.json')
        self.juego=director.obtenerJuego()
        self.mostrarLaberinto()
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

        
        self.personaje = pygame.image.load("graphics/principal.png").convert_alpha()
        self.personaje = pygame.transform.scale(self.personaje,(30*1.35,30*1.35))
        mirando_izquierda = False
        
        self.screen.blit(self.personaje,(self.pX,self.pY))

        abrir = False
        while running:
            keys = pygame.key.get_pressed()
            self.screen.blit(self.personaje,(self.pX,self.pY))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if keys[pygame.K_SPACE]:
                    if not abrir:
                        abrir = True
                        self.juego.abrirPuertas()
                        pygame.display.flip()
                    else:
                        abrir = False
                        self.juego.cerrarPuertas()
                        pygame.display.flip()        

            
            if keys[pygame.K_LSHIFT]:
                shift = 2
            else:
                shift = 0

            if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                self.pX = self.origenX/2 + 50 
                self.pY = ((self.alto)/2) + self.origenY/2 + self.origenX
                self.redibujar()
                self.comprobarElemento(self.habActual,self.habActual.forma.oeste)
                
                #voltear 
                if not mirando_izquierda:
                    mirando_izquierda = True
                    self.personaje = pygame.transform.flip(self.personaje,True,False)

            if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                self.pX = self.ancho - 50
                self.pY = ((self.alto)/2) + self.origenY/2 + self.origenX
                self.redibujar()
                self.comprobarElemento(self.habActual,self.habActual.forma.este)
                
                #voltear
                if mirando_izquierda:
                    mirando_izquierda = False
                    self.personaje = pygame.transform.flip(self.personaje,True,False)
                
            if keys[pygame.K_UP] or keys[pygame.K_w]:
                self.pX = self.origenX + (self.ancho/2) - (30/2)
                self.pY = self.origenY + (self.alto/5) - (30/2)
                self.redibujar()
                self.comprobarElemento(self.habActual,self.habActual.forma.norte)

            if keys[pygame.K_DOWN] or keys[pygame.K_s]:
                self.pX = self.origenX + (self.ancho/2) - (30/2)
                self.pY = self.origenY + (self.alto-85) - (30/2)
                self.redibujar()
                self.comprobarElemento(self.habActual,self.habActual.forma.sur)
                # self.juego.personaje.irAlSur()
            
            # self.screen.blit(self.personaje,(self.pX,self.pY))
            pygame.display.update()
            clock.tick(60)
    
    def moverPersonajeHabitacion(self):
        self.pX = (self.habActual.forma.puntoX+(self.ancho/2)-30/2) 
        self.pY = self.habActual.forma.puntoY+(self.alto/2)-30/2
        self.screen.blit(self.personaje,(self.pX,self.pY))
            
    def redibujar(self):
        for hijo in self.juego.laberinto.hijos:
                    self.dibujarContenedorRectangularEscala(hijo.forma, 1)
                    self.ocultar()

    def comprobarElemento(self,unaHabitacion,unaOrientacion):
            if unaOrientacion.esPuerta():
                if unaOrientacion.abierta:
                    print("Puerta abierta")
                    if self.pasadoPuerta:
                        self.habActual = unaOrientacion.lado1
                        self.pasadoPuerta = False
                    else:
                        self.habActual = unaOrientacion.lado2
                        self.pasadoPuerta = True
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

    def agregarPersonaje(self,unaCadena):
        personaje = Personaje()
        personaje.nickname = unaCadena
        self.juego.agregarPersonaje(personaje)
        self.person = self.juego.personaje
        self.vidasM = self.person.vidas
        self.habActual = self.person.posicion
      
    def ocultar(self):
        ocultar = pygame.Surface((11,self.height-60))
        ocultar.fill((50,50,50))
        self.screen.blit(ocultar,(1140,50))

    def mostrarVidasPersonaje(self):
        if self.vidasM == None:
            return None
        pygame.init()
        miFuente = pygame.font.SysFont('radnika',30)
        text = miFuente.render("Vidas: "+str(self.person.vidas),True,(255,0,0))
        rectText = text.get_rect()
        rectText.center = (80,30)
        self.screen.blit(text,rectText)
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
        self.dibujarContenedorRectangularEscala(unaHabitacion.forma, 1)
        
    
    def visitarPuerta(self,unaPuerta):
        print('Puerta visitada')
        #dibujar
    
    def visitarPared(self,unaPared):
        print('Pared visitada')
        #dibujar
        

    def visitarTunel(self,unTunel):
        print('Tunel visitado')
        #dibujar

    def dibujarContenedorRectangularEscala(self,unaForma,escala):
       unPuntoX = unaForma.puntoX
       unPuntoY = unaForma.puntoY
       ancho = (unaForma.extentX)/escala
       alto = (unaForma.extentY)/escala

       unaForma.extentX = ancho
       unaForma.extentY = alto
     
       
      
       
       
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
