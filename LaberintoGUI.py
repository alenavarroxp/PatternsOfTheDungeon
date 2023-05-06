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
        pX = self.origenX + (self.ancho/2) - (30/2)
        pY = self.origenY + (self.alto/2) - (30/2)
        personaje = pygame.image.load("graphics/principal.png").convert_alpha()
        personaje = pygame.transform.scale(personaje,(30*1.35,30*1.35))
        rect = personaje.get_rect(center=(pX,pY))

        
        personaje = pygame.image.load("graphics/principal.png").convert_alpha()
        personaje = pygame.transform.scale(personaje,(30*1.35,30*1.35))
        mirando_izquierda = False
        

        
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                shift = 2
            else:
                shift = 0

            if keys[pygame.K_LEFT]:
                self.screen.blit(personaje,(pX,pY))
                for hijo in self.juego.laberinto.hijos:
                    self.dibujarContenedorRectangularEscala(hijo.forma, 1)
                pX -= (2 + shift)
                #voltear 
                if not mirando_izquierda:
                    mirando_izquierda = True
                    personaje = pygame.transform.flip(personaje,True,False)
                self.screen.blit(personaje,(pX,pY))
            if keys[pygame.K_RIGHT]:
                self.screen.blit(personaje,(pX,pY))
                for hijo in self.juego.laberinto.hijos:
                    self.dibujarContenedorRectangularEscala(hijo.forma, 1)
                pX += (2 +shift)
                #voltear
                if mirando_izquierda:
                    mirando_izquierda = False
                    personaje = pygame.transform.flip(personaje,True,False)
                self.screen.blit(personaje,(pX,pY))
            if keys[pygame.K_UP]:
                self.screen.blit(personaje,(pX,pY))
                for hijo in self.juego.laberinto.hijos:
                    self.dibujarContenedorRectangularEscala(hijo.forma, 1)
                pY -= (2 + shift)
                self.screen.blit(personaje,(pX,pY))
            if keys[pygame.K_DOWN]:
                self.screen.blit(personaje,(pX,pY))
                for hijo in self.juego.laberinto.hijos:
                    self.dibujarContenedorRectangularEscala(hijo.forma, 1)
                pY += (2 + shift)
                self.screen.blit(personaje,(pX,pY))
            
            self.screen.blit(personaje,(pX,pY))
        
            pygame.display.update()
            clock.tick(60)
    
            
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
        ocultar = pygame.Surface((11,self.height-60))
        ocultar.fill((50,50,50))
        self.screen.blit(ocultar,(1140,50))

        self.mostrarVidasPersonaje()

    def agregarPersonaje(self,unaCadena):
        personaje = Personaje()
        personaje.nickname = unaCadena
        self.juego.agregarPersonaje(personaje)
        self.person = self.juego.personaje
        self.vidasM = self.person.vidas
       
    
    def dibujarPersonaje(self,pX,pY):
        if pX == 0 and pY == 0:
            pX = self.origenX + (self.ancho/2) - (30/2)
            pY = self.origenY + (self.alto/2) - (30/2)
      
        
        

        
       
        
        
        
    def mostrarVidasPersonaje(self):
        if self.vidasM == None:
            return None
        pygame.init()
        miFuente = pygame.font.SysFont('radnika',30)
        text = miFuente.render("Vidas: "+str(self.person.vidas),True,(255,0,0))
        rectText = text.get_rect()
        rectText.center = (80,30)
        pygame.draw.rect(self.screen,(0,0,0),rectText,2)
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
     
       
       
    #    rect =pygame.Rect(unPuntoX,unPuntoY,ancho,alto)
    #    pygame.draw.rect(self.screen,(255,0,0),rect)
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
       
    
        
    # def dibujarPared(self,unaOrientacion):
    #     pared = pygame.Surface((self.ancho,100))
    #     pared.fill((255,0,0))
    #     pygame.draw.rect(pared,(0,0,0),pared.get_rect(),3)
    #     self.screen.blit(pared,(0,0))
    #     pygame.display.update()

vista = LaberintoGUI()
vista.iniciarJuego()
juego = vista.juego
print(vista.juego)

# print("FUENTES",pygame.font.get_fonts())
