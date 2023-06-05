from src.model.Fase import Fase


class Jugando(Fase):
    def esJugando(self):
        return True
    
    def agregarPersonajeJuego(self, unPersonaje, unJuego):
        print("El juego ya ha comenzado")

    