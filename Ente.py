from Vivo import Vivo
from Norte import Norte
from Este import Este
from Oeste import Oeste
from Sur import Sur
from abc import ABC,abstractmethod
class Ente(ABC):

    def __init__(self):
        self.vidas = 100
        self.poder = 1
        self.estado = Vivo()
        self.posicion= None
        self.juego = None

    def atacar(self):
        unEnte = self.buscarEnemigo()
        if unEnte is not None:
            unEnte.esAtacadoPor(self)
    
    def esAtacadoPor(self,unEnte):
        self.estado.enteEsAtacadoPor(self,unEnte)

    def puedeSerAtacadoPor(self,unEnte):
        self.recalcularVidas(unEnte)
        if self.comprobarEstado():
            self.enteMuere()

    def recalcularVidas(self,unEnte):
        self.vidas = self.vidas - unEnte.vidas
        if self.vidas < 0:
            self.vidas = 0
        print(str(self)," vidas: "+str(self.vidas))
    
    def comprobarEstado(self):
        if self.vidas == 0:
            return True
        else:
            return False
        
    @abstractmethod
    def buscarEnemigo(self):
        pass

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

    @abstractmethod
    def enteMuere():
        pass
