from src.model.Coger import Coger
from src.model.Soltar import Soltar
from src.model.Canjear import Canjear
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
        print(f"\n{str(objeto)} agregado al inventario")
        
        
        

    def quitarComprar(self, objeto):
        for comando in objeto.comandos[:]:
            if comando.esComprar():
                objeto.quitarComando(comando)
            objeto.agregarComando(Usar(), objeto)
            if not objeto.esMoneda():
                objeto.agregarComando(Soltar(), objeto)
        
    def quitarCoger(self,objeto):
       for comando in objeto.comandos[:]:
            if comando.esCoger():
                objeto.quitarComando(comando)
                if not objeto.esMoneda():
                    objeto.agregarComando(Soltar(),objeto)
            if objeto.esMoneda():
                objeto.agregarComando(Canjear(),objeto)
            else:
                objeto.agregarComando(Usar(),objeto)
            

    def quitarObjeto(self, objeto):
        if objeto in self.objetos:
            self.objetos[objeto] -= 1
            if self.objetos[objeto] == 0:
                del self.objetos[objeto]

    def soltarObjeto(self, objeto, alguien):
        if objeto in self.objetos:
            self.quitarObjeto(objeto)
            for comando in objeto.comandos[:]:
                if comando.esSoltar() or comando.esUsar():
                    objeto.quitarComando(comando)
            if objeto.esEspada():
                if not any(comando.esUsar() for comando in objeto.comandos):
                    if alguien.objetoUsado is objeto:
                        alguien.poder -= objeto.poder
                        alguien.objetoUsado = None
            objeto.agregarComando(Coger(), objeto)
            objeto.padre = alguien.posicion
            alguien.posicion.agregarObjeto(objeto)
            print(f"{str(objeto)} soltado")

    def abrirInventario(self):
        print("Inventario:")
        for objeto, cantidad in self.objetos.items():
            print(f"{str(objeto)} x{cantidad}")

    def __str__(self):
        return f"Inventario: {list(self.objetos.keys())}"
