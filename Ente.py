from Vivo import Vivo
from Norte import Norte
from Este import Este
from Oeste import Oeste
from Sur import Sur
class Ente():

    def __init__(self):
        self.vidas = 100
        self.poder = 1
        self.estado = Vivo()
    
    def estaVivo(self):
        return self.estado.estaVivo()
    
    def irA(self,unaOr):
        unaOr.ir(self)

    def irAlNorte(self):
        self.irA(Norte.obtenerInstancia())

    def irAlEste(self):
        self.irA(Este.obtenerInstancia())

    def irAlOeste(self):
        self.irA(Oeste.obtenerInstancia())

    def irAlSur(self):
        self.irA(Sur.obtenerInstancia())
