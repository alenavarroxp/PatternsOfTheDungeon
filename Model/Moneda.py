from model.Objeto import Objeto


class Moneda(Objeto):
    # Aproximación de flyweight para reducir el uso de memoria y evitar la creación de objetos innecesarios 
    instanciasMonedas = {}
    def __new__(cls, valor):
        if valor not in cls.instanciasMonedas:
            cls.instanciasMonedas[valor] = super().__new__(cls)
            cls.instanciasMonedas[valor].contador = 1
        else:
            cls.instanciasMonedas[valor].contador += 1
        return cls.instanciasMonedas[valor]

    def __init__(self, valor):
        self.valor = valor

    def usarObjeto(self):
        print(self)

    def __str__(self):
        return f"Moneda: {self.valor} x{self.contador}"
    
    def __repr__(self):
        return f"Moneda: {self.valor} x{self.contador}"
