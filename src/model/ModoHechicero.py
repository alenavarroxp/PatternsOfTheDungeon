from time import sleep


class ModoHechicero():
    def __init__(self):
        pass

    def conjura(self, hechicero):
        self.caminar(hechicero)
        self.hechiza(hechicero)
        self.dormir()

    def dormir(self):
        print("Hechicero duerme")
        sleep(5)

    def caminar(self, hechicero):
        print("Hechicero camina")
        orientacion = hechicero.obtenerOrientacionAleatoria()
        hechicero.irA(orientacion)

    def hechiza(self, hechicero):
        print("Hechicero hechiza")
        hechicero.hechizar()

    def esMago(self):
        return False
    
    def esBrujo(self):
        return False
    