from src.model.Estado import Estado


class Vivo(Estado):
    def actua(self,unBicho):
       unBicho.puedeActuar()

    def enteEsAtacadoPor(self,atacado,atacante):
        atacado.puedeSerAtacadoPor(atacante)
        
    def estaVivo(self):
        return True