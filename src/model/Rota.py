from src.model.EstadoEspada import EstadoEspada


class Rota(EstadoEspada):
    def estaRota(self):
        super().estaRota()
        print("La espada está rota")

    def usarObjeto(self, alguien,objeto):
        objeto.poder = 0
        print("La espada está rota. ",alguien," no la puede usar")

    def __str__(self):
        return "Rota"

    def __repr__(self):
        return "Rota"