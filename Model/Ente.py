from model.Vivo import Vivo


class Ente():
    def __init__(self):
        self.poder = None
        self.vidas = 50
        self.posicion = None
        self.juego = None
        self.estado = Vivo()
    
    def atacar(self):
        ente = self.buscarEnemigo()
        if ente is not None:
            ente.esAtacadoPor(self)

    def buscarEnemigo(self):
        pass

    def esAtacadoPor(self,alguien):
        self.estado.enteEsAtacadoPor(self,alguien)

    def heMuerto(self):
        pass

    def puedeSerAtacadoPor(self,alguien):
        print(alguien,' ataca a ',self)
        self.vidas -= alguien.poder
        print(self,' tiene ',self.vidas,' vidas')
        if self.vidas <= 0:
            self.heMuerto()

    def irA(self,unaOrientacion):
        unaOrientacion.ir(self)

    def irAlEste(self):
        print(self, "yendo al Este")
        self.irA(self.juego.fabricarEste())
    
    def irAlOeste(self):
        print(self, "yendo al Oeste")
        self.irA(self.juego.fabricarOeste())
    
    def irAlNorte(self):
        print(self, "yendo al Norte")
        self.irA(self.juego.fabricarNorte())

    def irAlSur(self):
        print(self, "yendo al Sur")
        self.irA(self.juego.fabricarSur())
