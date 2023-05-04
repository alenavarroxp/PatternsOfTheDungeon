from model.Director import Director


class LaberintoGUI():
    def iniciarJuego(self):
        director = Director()
        director.procesar('laberintos/lab4Hab4Arm4BichosTunel.json')
        self.juego=director.obtenerJuego()
        self.dibujarLaberinto()

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
    
    def visitarPuerta(self,unaPuerta):
        print('\n\n',unaPuerta,'Puerta visitada')
        #dibujar
    
    def visitarPared(self,unaPared):
        print('Pared visitada')
        #dibujar

    def visitarTunel(self,unTunel):
        print('Tunel visitado')
        #dibujar

vista = LaberintoGUI()
vista.iniciarJuego()
print(vista.juego)
