from src.model.Orientacion import Orientacion


class Noreste(Orientacion):
    def ir(self,alguien):
        contenedor = alguien.posicion.forma
        contenedor.noreste.entrar(alguien)

    def ponerElemento(self,unEM,unaHab):
        unaHab.noreste = unEM

    def recorrerEn(self, unBloque, unContenedor):
        if unContenedor.noreste is not None:
            unContenedor.noreste.recorrer(unBloque)