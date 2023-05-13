from src.model.Orientacion import Orientacion


class Noroeste(Orientacion):
    def ir(self,alguien):
        contenedor = alguien.posicion.forma
        contenedor.noroeste.entrar(alguien)

    def ponerElemento(self,unEM,unaHab):
        unaHab.noroeste = unEM

    def recorrerEn(self, unBloque, unContenedor):
        if unContenedor.noroeste is not None:
            unContenedor.noroeste.recorrer(unBloque)