from classes.elementoMapa.decorator.Decorator import Decorator

class Espada (Decorator):

    def __init__(self):
        super().__init__()
        self.poder = 10
        self.usos = 5
    
    def entrar(self,ente):
        print("Espada")

    def __str__(self):
        return "Espada"
    
    def __repr__(self):
        return "Espada"
    
    def esEspada(self):
        return True