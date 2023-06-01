from classes.elementoMapa.ElementoMapa import ElementoMapa
import random

class Contenedor (ElementoMapa):

    def __init__(self, num):
        super().__init__()
        self.num= num
        self.hijos = []
        self.forma = None
        self.extent = None

    def recorrer(self,func):
        func(self)
        map(func,self.hijos)
        self.forma.recorrer(func)

    def calcularPosicion(self):
        self.forma.calcularPosicion()

    def getPunto(self):
        return self.forma.punto
    
    def setPunto(self,punto):
        self.forma.punto = punto

    def getExtent(self):
        return self.forma.extent
    
    def setExtent(self,extent):
        self.forma.extent = extent

    def obtenerComandos(self,ente):
        listaComandos = []
        listaComandos.extend(self.comandos)
        for hijo in self.hijos:
            listaComandos.extend(hijo.obtenerComandos(ente))
        listaComandos.extend(self.forma.obtenerComandos(ente))
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
