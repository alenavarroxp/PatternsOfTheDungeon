from src.model.Orientacion import Orientacion


class Noroeste(Orientacion):
    UnicaInstancia = None

    def __new__(cls):
        if cls.UnicaInstancia is None:
            cls.UnicaInstancia = super().__new__(cls)
        return cls.UnicaInstancia
    
    def ir(self,alguien):
        contenedor = alguien.posicion.forma
        contenedor.noroeste.entrar(alguien)

    def ponerElemento(self,unEM,unaHab):
        unaHab.noroeste = unEM

    def recorrerEn(self, unBloque, unContenedor):
        if unContenedor.noroeste is not None:
            unContenedor.noroeste.recorrer(unBloque)