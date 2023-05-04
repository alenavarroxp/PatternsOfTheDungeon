import pygame,sys
from model.Director import Director


class LaberintoGUI():
    def __init__(self):
        self.juego = None
        self.ancho = 1150
        self.alto = 900
        self.screen = pygame.display.set_mode((1000,700))
        self.screen.fill((50,50,50))

    def iniciarJuego(self):
        director = Director()
        director.procesar('laberintos/lab4Hab4Arm4BichosTunel.json')
        self.juego=director.obtenerJuego()
        self.mostrarLaberinto()
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
        hab1.puntoX = 0
        hab1.puntoY = 0
        hab1.calcularPosicion()

    def normalizar(self):
        minX = 0
        minY = 0
        for hijo in self.juego.laberinto.hijos:
            if hijo.forma.puntoX < minX:
                minX = hijo.puntoX()
            if hijo.forma.puntoY < minY:
                minY = hijo.puntoY()

        for hijo in self.juego.laberinto.hijos:
            unPuntoX = hijo.forma.puntoX
            unPuntoY = hijo.forma.puntoY
            hijo.forma.puntoX = abs(unPuntoX + minX)
            hijo.forma.puntoY = abs(unPuntoY + minY)
    def calcularDimensiones(self):
        maxX = 0
        maxY = 0
        for hijo in self.juego.laberinto.hijos:
            if hijo.forma.puntoX > maxX:
                maxX = hijo.puntoX()
            if hijo.forma.puntoY > maxY:
                maxY = hijo.puntoY()
        maxX = maxX + 1
        maxY = maxY + 1
        self.ancho = round(1050/maxX)
        self.alto = round(850/maxY)

    def asignarPuntosReales(self):
        origenX = 70
        origenY = 10
        for hijo in self.juego.laberinto.hijos:
            PuntoX = origenX + (hijo.forma.puntoX * self.ancho)
            PuntoY = origenY + (hijo.forma.puntoY * self.alto)
            hijo.forma.puntoX = PuntoX
            hijo.forma.puntoY = PuntoY
            hijo.extentX(self.ancho)
            hijo.extentY(self.alto)

    def mostrarVentana(self):
        pygame.init()
        pygame.display.set_caption("Laberinto")
       

        while True:
            
            #Evento de salida
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
        
            pygame.display.update()
            
    def getImage(self,sheet,frame,width,height,scale,colour):
        image = pygame.Surface((width,height)).convert_alpha()
        image.blit(sheet,(0,0),((frame*width),0,width,height))
        image = pygame.transform.scale(image,(int(width*scale),int(height*scale)))
        image.set_colorkey(colour)
        return image
    
    def dibujarLaberinto(self):
        if self.juego is None:
            return self
        self.juego.laberinto.aceptar(self)

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
        self.dibujarContenedorRectangularEscala(unaHabitacion.forma, 2)
    
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
       pygame.display.update()

vista = LaberintoGUI()
vista.iniciarJuego()
juego = vista.juego
print(vista.juego)
print("ALGO")
