from ElementoMapa import ElementoMapa
import random

class Contenedor (ElementoMapa):

    def __init__(self, num):
        super().__init__()
        self.num= num
        self.hijos = []
        self.forma = None

    def recorrer(self,func):
        func(self)
        map(func,self.hijos)
        self.forma.recorrer(func)

    def obtenerComandos(self):
        listaComandos = []
        listaComandos.extend(self.comandos)
        for hijo in self.hijos:
            listaComandos.extend(hijo.obtenerComandos())
        listaComandos.extend(self.forma.obtenerComandos())
        return listaComandos

    def agregarHijo(self, EM):
        EM.padre = self
        self.hijos.append(EM)

    def ponerElementoEn(self,ori,em):
        self.forma.ponerElementoEn(ori,em)

    def agregarOrientacion(self, ori):
        self.forma.agregarOrientacion(ori)

    def obtenerOrientacionAleatoria(self):
        indice = self.obtenerNumeroAleatorio(len(self.forma.orientaciones))

        return self.forma.orientaciones[indice]
    
    def obtenerNumeroAleatorio(self,long):
        return random.randint(0,long-1)

    def obtenerHijos(self):
        return self.hijos
