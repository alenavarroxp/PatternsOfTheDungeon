from src.model.Orientacion import Orientacion


class Noreste(Orientacion):
    UnicaInstancia = None

    def __new__(cls):
        if cls.UnicaInstancia is None:
            cls.UnicaInstancia = super().__new__(cls)
        return cls.UnicaInstancia
    
    def ir(self,alguien):
        contenedor = alguien.posicion.forma
        contenedor.noreste.entrar(alguien)

    def ponerElemento(self,unEM,unaHab):
        unaHab.noreste = unEM

    def recorrerEn(self, unBloque, unContenedor):
        if unContenedor.noreste is not None:
            unContenedor.noreste.recorrer(unBloque)