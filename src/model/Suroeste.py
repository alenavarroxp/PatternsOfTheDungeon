from src.model.Orientacion import Orientacion


class Suroeste(Orientacion):
    def ir(self,alguien):
        contenedor = alguien.posicion.forma
        contenedor.suroeste.entrar(alguien)

    def ponerElemento(self,unEM,unaHab):
        unaHab.suroeste = unEM

    def recorrerEn(self, unBloque, unContenedor):
        if unContenedor.suroeste is not None:
            unContenedor.suroeste.recorrer(unBloque)