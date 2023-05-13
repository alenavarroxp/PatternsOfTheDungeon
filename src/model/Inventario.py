class Inventario:
    def __init__(self):
        self.objetos = {}

    def agregarObjeto(self, objeto):
        if objeto in self.objetos:
            self.objetos[objeto] += 1
        else:
            self.objetos[objeto] = 1

    def quitarObjeto(self, objeto):
        if objeto in self.objetos:
            self.objetos[objeto] -= 1
            if self.objetos[objeto] == 0:
                del self.objetos[objeto]

    def abrirInventario(self):
        print("Inventario:")
        for objeto, cantidad in self.objetos.items():
            print(f"{str(objeto)} x{cantidad}")

    def __str__(self):
        return f"Inventario: {list(self.objetos.keys())}"
