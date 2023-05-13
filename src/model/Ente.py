from src.model.Vivo import Vivo


class Ente():
    def __init__(self):
        self.poder = 10
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
        self.vidas -= int(alguien.poder)
        print(self,' tiene ',self.vidas,' vidas')
        if self.vidas <= 0:
            self.vidas = 0
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

    def irAlNoreste(self):
        print(self, "yendo al Noreste")
        self.irA(self.juego.fabricarNoreste())
    
    def irAlNoroeste(self):
        print(self, "yendo al Noroeste")
        self.irA(self.juego.fabricarNoroeste())

    def irAlSureste(self):
        print(self, "yendo al Sureste")
        self.irA(self.juego.fabricarSureste())
    
    def irAlSuroeste(self):
        print(self, "yendo al Suroeste")
        self.irA(self.juego.fabricarSuroeste())
    