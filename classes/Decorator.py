from classes.Hoja import Hoja

class Decorator (Hoja):

    def __init__(self):
        super().__init__()
        self.component = None

    def recorrer(self, funcion):
        funcion(self)
        self.component.recorrer(funcion)