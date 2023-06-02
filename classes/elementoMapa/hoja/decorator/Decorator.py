from classes.elementoMapa.hoja.Hoja import Hoja

class Decorator (Hoja):

    def __init__(self):
        super().__init__()
        self.component = None

    def recorrer(self, funcion):
        funcion(self)
        if self.component is not None:
            self.component.recorrer(funcion)