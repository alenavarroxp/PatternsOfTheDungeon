from src.model.Ente import Ente


class Mercader(Ente):
    def __init__(self,nick):
        super().__init__()
        self.nick = nick
        self.objetos = []

    def agregarObjeto(self, objeto,precio):
        objeto.precio = precio
        self.objetos.append(objeto)

    def quitarObjeto(self, objeto):
        self.objetos.remove(objeto)

    def __str__(self):
        return f"{self.nick} tiene: {self.objetos}"
    
