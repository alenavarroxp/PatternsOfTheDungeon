from src.model.Orientacion import Orientacion


class Suroeste(Orientacion): 
    UnicaInstancia = None

    def __new__(cls):
        if cls.UnicaInstancia is None:
            cls.UnicaInstancia = super().__new__(cls)
        return cls.UnicaInstancia
    
    def ir(self,alguien):
        contenedor = alguien.posicion.forma
        contenedor.suroeste.entrar(alguien)

    def ponerElemento(self,unEM,unaHab):
        unaHab.suroeste = unEM

    def obtenerComandosDe(self,unaForma):
        return unaForma.suroeste.obtenerComandos(None)
    
    def recorrerEn(self, unBloque, unContenedor):
        if unContenedor.suroeste is not None:
            unContenedor.suroeste.recorrer(unBloque)