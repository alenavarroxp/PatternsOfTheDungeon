class Ente():
    def __init__(self):
        self.poder = None
        self.vidas = None
        self.posicion = None
        self.juego = None
    
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
