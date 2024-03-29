from src.model.Rota import Rota
from src.model.Canjear import Canjear
from src.model.Entrar import Entrar
from src.model.Coger import Coger
from src.model.Comprar import Comprar
from src.model.Moneda import Moneda
from src.model.Mercader import Mercader
from src.model.Mochila import Mochila
from src.model.Tienda import Tienda
from src.model.Activar import Activar
from src.model.Brujo import Brujo
from src.model.Hechicero import Hechicero
from src.model.Mago import Mago
from src.model.Abrir import Abrir
from src.model.Agresivo import Agresivo
from src.model.Armario import Armario
from src.model.Baul import Baul
from src.model.Bicho import Bicho
from src.model.Bomba import Bomba
from src.model.Cuadrado import Cuadrado
from src.model.Espada import Espada
from src.model.Este import Este
from src.model.Habitacion import Habitacion
from src.model.Juego import Juego
from src.model.Laberinto import Laberinto
from src.model.Norte import Norte
from src.model.Oeste import Oeste
from src.model.Pared import Pared
from src.model.Perezoso import Perezoso
from src.model.Puerta import Puerta
from src.model.Sur import Sur
from src.model.Tunel import Tunel

class LaberintoBuilder():
    def __init__(self):
        self.juego = None
        self.laberinto = None

    def obtenerJuego(self):
        return self.juego
    
    def fabricarJuego(self):
       self.juego = Juego()
       self.juego.laberinto = self.laberinto
       return self.juego
    
    def fabricarLaberinto(self):
        self.laberinto = Laberinto()
        return self.laberinto

    
    def fabricarArmario(self,num):
        return Armario(num)
    
    def fabricarArmarioEn(self,unContenedor):
        num = unContenedor.num
        arm = self.fabricarArmario(num)
        arm.forma = self.fabricarForma()
        arm.ponerEnElemento(self.fabricarNorte(),self.fabricarPared(arm))
        arm.ponerEnElemento(self.fabricarEste(),self.fabricarPared(arm))
        arm.ponerEnElemento(self.fabricarOeste(),self.fabricarPared(arm))
        arm.ponerEnElemento(self.fabricarSur(),self.fabricarPared(arm))
        arm.agregarOrientacion(self.fabricarNorte())
        arm.agregarOrientacion(self.fabricarEste())
        arm.agregarOrientacion(self.fabricarOeste())
        arm.agregarOrientacion(self.fabricarSur())
        puerta = self.fabricarPuerta(arm,unContenedor)
        arm.ponerEnElemento(self.fabricarEste(),puerta)
        unContenedor.agregarHijo(arm)

    def fabricarBaul(self,num):
        return Baul(num)
    
    def fabricarBaulEn(self,unContenedor,num,contenido):
        baul = self.fabricarBaul(num)
        baul.forma = self.fabricarForma()
        baul.ponerEnElemento(self.fabricarNorte(),self.fabricarPared(baul))
        baul.ponerEnElemento(self.fabricarEste(),self.fabricarPared(baul))
        baul.ponerEnElemento(self.fabricarOeste(),self.fabricarPared(baul))
        baul.ponerEnElemento(self.fabricarSur(),self.fabricarPared(baul))
        for i in range(0,len(contenido)):
            if contenido[i]['tipo'] == 'espada':
                poder = contenido[i]['poder']
                tipo = contenido[i]['tipo']
                getattr(self, 'fabricar' + tipo.capitalize() + 'En')(baul,poder)
            elif contenido[i]['tipo'] == 'mochila':
                getattr(self, 'fabricar' + contenido[i]['tipo'].capitalize() + 'En')(baul,contenido[i]['contenido'])
            elif contenido[i]['tipo'] == 'moneda':
                getattr(self, 'fabricar' + contenido[i]['tipo'].capitalize())(baul,contenido[i]['valor'])
        baul.agregarOrientacion(self.fabricarNorte())
        baul.agregarOrientacion(self.fabricarEste())
        baul.agregarOrientacion(self.fabricarOeste())
        baul.agregarOrientacion(self.fabricarSur())
        puerta = self.fabricarPuerta(baul,unContenedor)
        baul.ponerEnElemento(self.fabricarEste(),puerta)
        unContenedor.agregarHijo(baul)
        


    def fabricarBichoAgresivo(self):
        bicho = Bicho()
        bicho.modo = self.fabricarModoAgresivo()
        bicho.vidas = 50
        bicho.poder = 10
        return bicho
    
    def fabricarBichoAgresivoPosicion(self,unaHabitacion):
        bicho = Bicho()
        bicho.modo = self.fabricarModoAgresivo()
        bicho.vidas = 50
        bicho.poder = 10
        bicho.posicion = self.juego.obtenerHabitacion(unaHabitacion)
        return bicho
     
    def fabricarBichoPerezoso(self):
        bicho = Bicho()
        bicho.modo = self.fabricarModoPerezoso()
        bicho.vidas = 50
        bicho.poder = 10
        return bicho
    
    def fabricarBichoPerezosoPosicion(self,unaHabitacion):
        bicho = Bicho()
        bicho.modo = self.fabricarModoPerezoso()
        bicho.vidas = 50
        bicho.poder = 10
        bicho.posicion = self.juego.obtenerHabitacion(unaHabitacion)
        return bicho
    
    def fabricarHechiceroMago(self):
        hechicero = Hechicero()
        hechicero.modohechicero = self.fabricarModoHechiceroMago()
        hechicero.vidas = 50
        hechicero.poder = 10
        return hechicero
    
    def fabricarHechiceroMagoPosicion(self,unaHabitacion):
        hechicero = Hechicero()
        hechicero.modohechicero = self.fabricarModoHechiceroMago()
        hechicero.vidas = 50
        hechicero.poder = 10
        hechicero.posicion = self.juego.obtenerHabitacion(unaHabitacion)
        return hechicero
    
    def fabricarHechiceroBrujo(self):
        hechicero = Hechicero()
        hechicero.modohechicero = self.fabricarModoHechiceroBrujo()
        hechicero.vidas = 50
        hechicero.poder = 10
        return hechicero
    
    def fabricarHechiceroBrujoPosicion(self,unaHabitacion):
        hechicero = Hechicero()
        hechicero.modohechicero = self.fabricarModoHechiceroBrujo()
        hechicero.vidas = 50
        hechicero.poder = 10
        hechicero.posicion = self.juego.obtenerHabitacion(unaHabitacion)
        return hechicero
    

    
    def fabricarBomba(self):
        bomba = Bomba()
        bomba.agregarComando(Activar(),bomba)
        return bomba
    
    def fabricarBombaEn(self,unContenedor):
        unContenedor.agregarHijo(self.fabricarBomba())

    def fabricarEste(self):
        return Este()
    
    def fabricarEspada(self,):
        espada = Espada()
        return espada
    
    def fabricarEspadaEn(self,unContenedor,poder):
        espada = Espada()
        espada.poder = poder
        if espada.poder <= 0:
            espada.estado = Rota()
        if not unContenedor.esTienda():
            espada.agregarComando(Coger(),espada)
        if isinstance(unContenedor,Mochila):
            unContenedor.agregarObjeto(espada)
        else:
            if not unContenedor.esTienda():
                unContenedor.agregarHijo(espada)
        return espada


    
    def fabricarForma(self):
        return Cuadrado()
    
    def fabricarHabitacion(self,num):
        hab = Habitacion(num)
        hab.forma = self.fabricarForma()
        hab.forma.num = num
        hab.ponerEnElemento(self.fabricarNorte(),self.fabricarPared(hab))
        hab.ponerEnElemento(self.fabricarEste(),self.fabricarPared(hab))
        hab.ponerEnElemento(self.fabricarOeste(),self.fabricarPared(hab))
        hab.ponerEnElemento(self.fabricarSur(),self.fabricarPared(hab))
        hab.agregarOrientacion(self.fabricarNorte())
        hab.agregarOrientacion(self.fabricarEste())
        hab.agregarOrientacion(self.fabricarOeste())
        hab.agregarOrientacion(self.fabricarSur())
        self.laberinto.agregarHabitacion(hab)
        return hab
    
    def fabricarLaberinto(self):
        self.laberinto = Laberinto()
        return self.laberinto
    
    def fabricarModoAgresivo(self):
        return Agresivo()
    
    def fabricarModoPerezoso(self):
        return Perezoso()
    
    def fabricarModoHechiceroMago(self):
        return Mago()
    
    def fabricarModoHechiceroBrujo(self):
        return Brujo()
   
    def fabricarNorte(self):
        return Norte()
 
    def fabricarOeste(self):
        return Oeste()
    
    def fabricarPared(self,padre):
        pared = Pared()
        pared.padre = padre
        return pared
    
    def fabricarPuerta(self,unaHab:Habitacion,otraHab:Habitacion):
        puerta = Puerta()
        puerta.lado1 = unaHab
        puerta.lado2 = otraHab
        puerta.padre = unaHab
        puerta.agregarComando(Abrir(),puerta)
        return puerta
    
    def fabricarPuertaBuilder(self,num1, ori1, num2, ori2):
        hab1 = self.laberinto.obtenerHabitacion(num1)
        hab2 = self.laberinto.obtenerHabitacion(num2)
        cadena1 = getattr(self,'fabricar' + ori1)()
        cadena2 = getattr(self,'fabricar' + ori2)()
        puerta = self.fabricarPuerta(hab1, hab2)
        hab1.ponerEnElemento(cadena1, puerta)
        hab2.ponerEnElemento(cadena2, puerta)
    
    def fabricarPuertaEstado(self,unaHab:Habitacion,otraHab:Habitacion,estado:bool):
        puerta = Puerta()
        puerta.lado1 = unaHab
        puerta.lado2 = otraHab
        puerta.padre = unaHab
        puerta.abierta = estado
        return puerta
    
    def fabricarSur(self):
        return Sur()
    
    def fabricarTunel(self):
        tunel = Tunel()
        # tunel.agregarComando(Entrar(),tunel)
        return tunel
    
    def fabricarTunelEn(self,unContenedor):
        unContenedor.agregarHijo(self.fabricarTunel())

    def fabricarTienda(self,num):
        tienda = Tienda(num)
        tienda.forma = self.fabricarForma()
        tienda.forma.num = num
        mercader = self.fabricarMercader(None)
        tienda.mercader = mercader
        tienda.ponerEnElemento(self.fabricarNorte(),self.fabricarPared(tienda))
        tienda.ponerEnElemento(self.fabricarEste(),self.fabricarPared(tienda))
        tienda.ponerEnElemento(self.fabricarOeste(),self.fabricarPared(tienda))
        tienda.ponerEnElemento(self.fabricarSur(),self.fabricarPared(tienda))
        tienda.agregarOrientacion(self.fabricarNorte())
        tienda.agregarOrientacion(self.fabricarEste())
        tienda.agregarOrientacion(self.fabricarOeste())
        tienda.agregarOrientacion(self.fabricarSur())
        tienda.abrirTienda()
        return tienda
    
    def fabricarTiendaEn(self,unContenedor,num,objetos):
        tienda = Tienda(num)
        tienda.forma = self.fabricarForma()
        tienda.forma.num = num
        mercader = self.fabricarMercader(objetos,tienda)
        tienda.mercader = mercader
        tienda.ponerEnElemento(self.fabricarNorte(),self.fabricarPared(tienda))
        tienda.ponerEnElemento(self.fabricarEste(),self.fabricarPared(tienda))
        tienda.ponerEnElemento(self.fabricarOeste(),self.fabricarPared(tienda))
        tienda.ponerEnElemento(self.fabricarSur(),self.fabricarPared(tienda))
        tienda.agregarOrientacion(self.fabricarNorte())
        tienda.agregarOrientacion(self.fabricarEste())
        tienda.agregarOrientacion(self.fabricarOeste())
        tienda.agregarOrientacion(self.fabricarSur())
        puertaTienda = self.fabricarPuerta(tienda,unContenedor)
        tienda.ponerEnElemento(self.fabricarOeste(),puertaTienda)
        tienda.abrirTienda()
        unContenedor.agregarHijo(tienda)
        return tienda
    
    def fabricarMochila(self,contenido):
        mochila = Mochila()
        for i in range(0,len(contenido)):
            item = contenido[i]['tipo']
            if item == 'espada':
                getattr(self,'fabricar' + item.capitalize()+"En")(mochila,contenido[i]['poder'])
            elif item == 'moneda':
                getattr(self,'fabricar' + item.capitalize()+"")(mochila,contenido[i]['valor'])
        return mochila
    
    def fabricarMochilaEn(self,unContenedor,contenido):
        mochila = self.fabricarMochila(contenido)
        mochila.agregarComando(Coger(),mochila)
        unContenedor.agregarHijo(mochila)
        return mochila
    
    def fabricarMercader(self,objetos,padre):
        mercader = Mercader('Antonio')
        for objeto in objetos:
            precio = objeto['precio']
            tipo = objeto['tipo']
            if tipo == 'mochila':
                objeto = getattr(self,'fabricar' + tipo.capitalize())(objeto['contenido'])
            elif tipo == 'espada':
                poder = objeto['poder']
                objeto = getattr(self,'fabricar' + tipo.capitalize()+"En")(padre,poder)
            else:
                objeto = getattr(self,'fabricar' + tipo.capitalize())()
            objeto.agregarComando(Comprar(),objeto)
            mercader.agregarObjeto(objeto,precio)
        return mercader
    
    def fabricarMoneda(self,ubicacion,valor):
        moneda = Moneda(valor,ubicacion)
        if isinstance(ubicacion,Mochila):
            moneda.agregarComando(Canjear(),moneda)
            ubicacion.agregarObjeto(moneda)
        else:
            moneda.agregarComando(Coger(),moneda)
            ubicacion.agregarHijo(moneda)
        return moneda