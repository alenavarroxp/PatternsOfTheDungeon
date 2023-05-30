from src.model.EstadoEspada import EstadoEspada


class Afilada(EstadoEspada):
    def estaAfilada(self):
        return True
    
    def __str__(self):
        return "Afilada"
    
    def __repr__(self):
        return "Afilada"
    