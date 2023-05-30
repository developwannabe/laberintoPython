from classes.Decorator import Decorator

class Fuego(Decorator):

    def __init__(self):
        super().__init__()
        self.daño = 10

    def esFuego(self):
        return True
    
    def __str__(self):
        return "Fuego"
    
    def __repr__(self):
        return "Fuego"