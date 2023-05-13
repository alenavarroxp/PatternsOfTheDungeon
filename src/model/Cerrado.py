from src.model.EstadoTienda import EstadoTienda


class Cerrado(EstadoTienda):
    def estaAbierto(self):
        super().estaAbierto()
        print("La tienda esta cerrada")

    def __str__(self):
        return "Cerrado"

    def __repr__(self):
        return "Cerrado"