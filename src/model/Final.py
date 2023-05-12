from src.model.Fase import Fase


class Final(Fase):
    def esFinal(self):
        return True
    
    def agregarPersonajeJuego(self, unPersonaje, unJuego):
        print("El juego ha terminado")