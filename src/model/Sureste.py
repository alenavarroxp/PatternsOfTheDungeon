from src.model.Orientacion import Orientacion


class Sureste(Orientacion):
    UnicaInstancia = None

    def __new__(cls):
        if cls.UnicaInstancia is None:
            cls.UnicaInstancia = super().__new__(cls)
        return cls.UnicaInstancia
    
    def ir(self,alguien):
        contenedor = alguien.posicion.forma
        contenedor.sureste.entrar(alguien)

    def ponerElemento(self,unEM,unaHab):
        unaHab.sureste = unEM

    def obtenerComandosDe(self,unaForma):
        return unaForma.sureste.obtenerComandos(None)
    
    def recorrerEn(self, unBloque, unContenedor):
        if unContenedor.sureste is not None:
            unContenedor.sureste.recorrer(unBloque)