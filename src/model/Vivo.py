from src.model.Estado import Estado


class Vivo(Estado):
    def actua(self,unBicho):
       unBicho.puedeActuar()

    def conjura(self,unHechicero):
        unHechicero.puedeConjurar()

    def enteEsAtacadoPor(self,atacado,atacante):
        atacado.puedeSerAtacadoPor(atacante)

    def enteEsHechizadoPor(self,hechizado,hechicero):
        hechizado.puedeSerHechizadoPor(hechicero)
        
    def estaVivo(self):
        return True