from src.model.Orientacion import Orientacion


class Sureste(Orientacion):
    def ir(self,alguien):
        contenedor = alguien.posicion.forma
        contenedor.sureste.entrar(alguien)

    def ponerElemento(self,unEM,unaHab):
        unaHab.sureste = unEM

    def recorrerEn(self, unBloque, unContenedor):
        if unContenedor.sureste is not None:
            unContenedor.sureste.recorrer(unBloque)