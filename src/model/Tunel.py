from src.model.Hoja import Hoja


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
            vueltaTunel = False
            self.laberinto = alguien.juego.clonarLaberinto()
            
            for hab in self.laberinto.hijos:
                for tunel in hab.hijos:
                    if tunel.esTunel():
                        vueltaTunel = True
                        tunel.laberinto = alguien.juego.laberinto
                        break
                if vueltaTunel:
                    break
        self.laberinto.entrar(alguien)
        
        

    def __str__(self):
        if self.laberinto is None:
            laberinto = 'No Laberinto'
        else:
            laberinto = f"Tiene Laberinto [{self.laberinto.num}]"
        return f"Tunel ({laberinto})"

    
    def __repr__(self):
        if self.laberinto is None:
            laberinto = 'No Laberinto'
        else:
            laberinto = f"Tiene Laberinto [{self.laberinto.num}]"
        return f"Tunel ({laberinto})"
