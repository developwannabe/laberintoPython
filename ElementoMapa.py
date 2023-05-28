from abc import ABC

class ElementoMapa(ABC):
    
    def __init__(self):
        self.padre = None
        
    def entrar(self,ente):
        pass

    def recorrer(self, funcion):
        funcion(self)

    def esHabitacion(self):
        return False
    
    def esBomba(self):
        return False
    
    def esPared(self):
        return False
    
    def esPuerta(self):
        return False
    
    def esBaul(self):
        return False
    
    def esEspada(self):
        return False
    
    def esFuego(self):
        return False
