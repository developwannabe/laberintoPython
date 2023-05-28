from ElementoMapa import ElementoMapa
import random

class Contenedor (ElementoMapa):

    def __init__(self, num):
        super().__init__()
        self.num= num
        self.hijos = []
        self.orientaciones = []
        self.norte = None
        self.este = None
        self.oeste= None
        self.sur = None

    def recorrer(self,func):
        func(self)
        map(func,self.hijos)
        for ori in self.orientaciones:
            ori.recorrerEn(self,func)

    def agregarHijo(self, EM):
        EM.padre = self
        self.hijos.append(EM)

    def ponerElementoEn(self,ori,em):
        ori.ponerElementoEn(em,self)

    def agregarOrientacion(self, ori):
        self.orientaciones.append(ori)

    def obtenerOrientacionAleatoria(self):
        indice = self.obtenerNumeroAleatorio(len(self.orientaciones))

        return self.orientaciones[indice]
    
    def obtenerNumeroAleatorio(self,long):
        return random.randint(0,long-1)

