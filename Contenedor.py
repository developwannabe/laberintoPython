from ElementoMapa import ElementoMapa 

class Contenedor (ElementoMapa):

    def __init__(self, num):
        self.num= num
        self.hijos = []
        self.orientaciones = []

    def recorrer(self,func):
        func(self)
        map(func,self.hijos)
        map(func,self.orientaciones)

    def agregarHijo(self, EM):
        EM.padre = self
        self.hijos.append(EM)

