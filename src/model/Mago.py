from src.model.ModoHechicero import ModoHechicero
import colorama


class Mago(ModoHechicero):
    def __init__(self):
        super().__init__()

    def esMago(self):
        return True 
    
    def __str__(self):
        colorama.init()
        return ""+colorama.Fore.GREEN+"Mago"+colorama.Style.RESET_ALL
    
