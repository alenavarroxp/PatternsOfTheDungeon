from src.model.EstadoEspada import EstadoEspada


class Rota(EstadoEspada):
    def estaRota(self):
        super().estaRota()
        print("La espada está rota")

    def __str__(self):
        return "Rota"

    def __repr__(self):
        return "Rota"