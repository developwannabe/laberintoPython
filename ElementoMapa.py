from abc import ABC

class ElementoMapa(ABC):
    
    def entrar(self):
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
