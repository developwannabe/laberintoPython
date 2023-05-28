from Ente import Ente
import threading

class Bicho(Ente):

    def __init__(self):
        super().__init__()
        self.modo=None
        self.num=None

    def actua(self):
        while self.estaVivo():
            self.estado.actua(self)

    def obtenerOrientacionAleatoria(self):
        return self.posicion.obtenerOrientacionAleatoria()
    
    def puedeActuar(self):
        self.modo.actua(self)

    def __str__(self):
        return "Bicho" + str(self.modo) + " "+str(self.num)
    
    def __repr__(self):
        return "Bicho" + str(self.modo) + str(self.num)
