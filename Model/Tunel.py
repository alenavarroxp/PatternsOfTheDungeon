from model.Hoja import Hoja


class Tunel(Hoja):
    def __init__(self):
        super().__init__()
        self.laberinto = None
        
    def aceptar(self,unVisitor):
        unVisitor.visitarTunel(self)

    def esTunel(self):
        return True
    
    def entrar(self,alguien):
        if self.laberinto == None:
            self.laberinto = alguien.juego.clonarLaberinto()
        self.laberinto.entrar(alguien) 
        # TODO: Pensar como hacer que el tunel te traiga de vuelta
        

    def __str__(self):
        if self.laberinto == None:
            laberinto = 'No Laberinto'
        else:
            laberinto = 'Tiene Laberinto'
        return f"Tunel ({laberinto}) [{self.laberinto}]"
    
    def __repr__(self):
        if self.laberinto == None:
            laberinto = 'No Laberinto'
        else:
            laberinto = 'Tiene Laberinto'
        return f"Tunel ({laberinto}) [{self.laberinto}]"