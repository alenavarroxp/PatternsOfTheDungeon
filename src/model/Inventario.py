from src.model.Usar import Usar


class Inventario:
    UnicaInstancia = None

    def __new__(cls):
        if not cls.UnicaInstancia:
            cls.UnicaInstancia = super().__new__(cls)
            cls.UnicaInstancia.objetos = {}
        else:
            cls.UnicaInstancia.vaciarInventario()
        return cls.UnicaInstancia

    def vaciarInventario(self):
        self.objetos = {}

    def agregarObjeto(self, objeto):
        if objeto in self.objetos:
            self.objetos[objeto] += 1
        else:
            self.objetos[objeto] = 1
        if any(comando.esComprar() for comando in objeto.comandos):
            self.quitarComprar(objeto)
        if any(comando.esCoger() for comando in objeto.comandos):
            self.quitarCoger(objeto)
        # self.quitarCoger(objeto)

    def quitarComprar(self, objeto):
        for comando in objeto.comandos:
            if comando.esComprar():
                objeto.quitarComando(comando)
            objeto.agregarComando(Usar(), objeto)
        
    def quitarCoger(self,objeto):
       for comando in objeto.comandos:
            if comando.esCoger():
                objeto.quitarComando(comando)
            objeto.agregarComando(Usar(),objeto)

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
