from src.model.Objeto import Objeto


class Moneda(Objeto):
    # # Aproximación de flyweight para reducir el uso de memoria y evitar la creación de objetos innecesarios 
    # instanciasMonedas = {}
    # def __new__(cls, valor,ubicacion):
    #     if (valor,ubicacion) not in cls.instanciasMonedas:
    #         cls.instanciasMonedas[(valor,ubicacion)] = super(Moneda,cls).__new__(cls)
    #         cls.instanciasMonedas[(valor,ubicacion)].contador = 1
    #     else:
    #         cls.instanciasMonedas[(valor,ubicacion)].contador += 1
    #     return cls.instanciasMonedas[(valor,ubicacion)]

    def __init__(self, valor,ubicacion):
        super().__init__()
        self.valor = valor
        self.ubicacion = ubicacion

    def aceptar(self,unVisitor):
        unVisitor.visitarMoneda(self)

    def canjearValor(self, alguien):
        alguien.dinero += self.valor
        alguien.inventario.quitarObjeto(self)
        for comando in self.comandos:
            if comando.esCanjear():
                self.quitarCanjear(comando)

    def quitarCanjear(self, comando):
        self.quitarComando(comando)
    
    def esMoneda(self):
        return True

    def __str__(self):
        return f"Moneda: {self.valor}"
    
    def __repr__(self):
        return f"Moneda: {self.valor}"
