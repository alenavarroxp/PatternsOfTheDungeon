from src.model.EstadoEspada import EstadoEspada


class Afilada(EstadoEspada):
    def estaAfilada(self):
        return True
    
    def usarObjeto(self, alguien, objeto):
        espadaUsada = False  

        for obj in alguien.inventario.objetos:
            if obj.esEspada() and not any(comando.esUsar() for comando in obj.comandos):
                if not espadaUsada:
                    alguien.poder -= obj.poder
                    espadaUsada = True

        alguien.poder += objeto.poder
        print("La espada está afilada. ", alguien, " puede usarla")


    def __str__(self):
        return "Afilada"
    
    def __repr__(self):
        return "Afilada"
    