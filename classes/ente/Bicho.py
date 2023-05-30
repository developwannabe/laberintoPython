from classes.ente.Ente import Ente
from classes.estado.Muerto import Muerto
import threading

class Bicho(Ente):

    def __init__(self):
        super().__init__()
        self.modo=None
        self.num=None

    def buscarEnemigo(self):
        return self.juego.buscarPersonaje(self)

    def actua(self):
        while self.estaVivo():
            self.estado.actua(self)

    def obtenerOrientacionAleatoria(self):
        return self.posicion.obtenerOrientacionAleatoria()
    
    def puedeActuar(self):
        self.modo.actua(self)

    def enteMuere(self):
        self.heMuerto()

    def heMuerto(self):
        self.estado=Muerto()
        self.muere()
        self.juego.muereBicho()

    def muere(self):
        print(str(self), " muere.")
        self.vidas = 0
        self.estado=Muerto()
    
    def __str__(self):
        return "Bicho" + str(self.modo) + " "+str(self.num)
    
    def __repr__(self):
        return "Bicho" + str(self.modo) + str(self.num)
