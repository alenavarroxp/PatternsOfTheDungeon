from src.model.Fase import Fase


class Inicial(Fase):
    def esInicial(self):
        return True
    
    def agregarPersonajeJuego(self, unPersonaje, unJuego):
        unJuego.puedeAgregarPersonaje(unPersonaje)
