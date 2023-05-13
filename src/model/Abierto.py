from src.model.EstadoTienda import EstadoTienda


class Abierto(EstadoTienda):
    def estaAbierto(self):
        return True
    
    def __str__(self):
        return "Abierto"
    
    def __repr__(self):
        return "Abierto"
    