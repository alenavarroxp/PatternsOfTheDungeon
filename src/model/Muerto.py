from src.model.Estado import Estado


class Muerto(Estado):
    def actua(self,unBicho):
        print(unBicho, "está muerto y no puede actuar")
    
    def enteEsAtacadoPor(self,atacado,atacante):
        print(atacado, "está muerto y no puede ser atacado")