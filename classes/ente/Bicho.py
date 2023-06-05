from classes.ente.Ente import Ente
from classes.estado.Muerto import Muerto
from classes.modo.Agresivo import Agresivo
import random

class Bicho(Ente):

    def __init__(self):
        super().__init__()
        self.modo=None
        self.num=None

    def setPosicion(self, pos):
        self.posicion= pos
        for obs in self.observadoresPosicion:
            obs.mostrarBicho(self)

    def setVidas(self, vida):
        self.vidas = vida
        for obs in self.observadoresPosicion:
            obs.vidasBicho(self)

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

    def cambiarModo(self):
        unEnte = self.juego.buscarBicho(self)
        if unEnte is not None:
            num = random.randint(1,10)
            if num > 9:
                self.modo = Agresivo()
                for obs in self.observadoresPosicion:
                    obs.mostrarBicho(self)


    def esBicho(self):
        return True
    
    def __str__(self):
        return "Bicho" + str(self.modo) + " "+str(self.num)
    
    def __repr__(self):
        return "Bicho" + str(self.modo) + str(self.num)
