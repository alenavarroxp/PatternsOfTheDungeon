from time import sleep
from src.model.ModoHechicero import ModoHechicero
import colorama

class Brujo(ModoHechicero):
    def __init__(self):
        super().__init__()

    def esBrujo(self):
        return True
    
    def dormir(self):
        sleep(7)
    
    def __str__(self):
        colorama.init()
        return ""+colorama.Fore.YELLOW+"Brujo"+colorama.Style.RESET_ALL