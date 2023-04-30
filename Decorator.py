from Hoja import Hoja

class Decorator (Hoja):

    def __init__(self):
        self.component = None

    def recorrer(self, funcion):
        funcion(self)
        self.component.recorrer(funcion)