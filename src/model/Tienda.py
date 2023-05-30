from colorama import init, Fore, Style
from src.model.Abierto import Abierto
from src.model.Cerrado import Cerrado
from src.model.Contenedor import Contenedor


class Tienda(Contenedor):
    def __init__(self, num):
        super().__init__(num)
        self.mercader = None
        self.estadoTienda = Cerrado()

    def aceptar(self, unVisitor):
        unVisitor.visitarTienda(self)
        self.forma.aceptar(unVisitor)
    
    def obtenerComandos(self,alguien):
        lista = []
        if alguien.posicion is self:
            lista = super().obtenerComandos(None)
            for objeto in self.mercader.objetos:
                lista.append(objeto.comandos[0])
        else: 
            lista = super().obtenerComandos(alguien)
        
        return lista

    def agregarMercader(self, mercader):
        self.mercader = mercader

    def enteCompraObjeto(self,personaje,objeto):
        if self.mercader is not None:
            if personaje.dinero >= objeto.precio:
                self.mercader.quitarObjeto(objeto)
                if self.mercader.objetos.__len__() == 0:
                    self.cerrarTienda()
                print(personaje,' compra ',objeto,' a ',self.mercader)
                personaje.dinero -= objeto.precio
                personaje.cogerObjeto(objeto)
            else:
                print(personaje,' no tiene suficiente dinero para comprar ',objeto,' a ',self.mercader)
               


        else:
            print('No hay mercader en la tienda: ',self.num)

    def abrirTienda(self):
        if self.mercader is not None and self.mercader.objetos.__len__() > 0:
            self.estadoTienda = Abierto()
        else:
            self.estadoTienda = Cerrado()
        
    def cerrarTienda(self):
        self.estadoTienda = Cerrado()

    def entrar(self,alguien):
        if self.estadoTienda.estaAbierto():
            print(alguien,' entra en la tienda: ',self.num)
            alguien.posicion = self
        else:
            print('No se puede entrar a la tienda: ',self.num)        

    def salir(self,alguien):
        print(alguien,' sale de la tienda: ',self.num)
        alguien.posicion = self.padre
    def esTienda(self):
        return True

    def __str__(self):
        # Configurar los estilos de colores
        init()

        # Definir los colores
        color_tienda = Fore.YELLOW
        color_estado = Fore.CYAN
        color_mercader = Fore.GREEN
        color_texto = Fore.MAGENTA

        # Formatear las variables
        num_formatted = f"{color_tienda}{self.num}{Style.RESET_ALL}"
        estado_formatted = f"{color_estado}{self.estadoTienda}{Style.RESET_ALL}"
        mercader_formatted = f"{color_mercader}{self.mercader}{Style.RESET_ALL}"

        # Construir la cadena de salida
        output = f"{color_texto}Tienda: {num_formatted}\n"
        output += f"\t Estado Tienda: {estado_formatted}\n"
        output += f"\t Mercader: {mercader_formatted}\n"
        output += f"\t {super().__str__()}{Style.RESET_ALL}"

        return output