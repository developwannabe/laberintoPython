from classes.estado.Vivo import Vivo
from classes.orientacion.Norte import Norte
from classes.orientacion.Este import Este
from classes.orientacion.Oeste import Oeste
from classes.orientacion.Sur import Sur
from classes.estado.Vivo import Vivo
from classes.orientacion.Noreste import Noreste
from classes.orientacion.Noroeste import Noroeste
from classes.orientacion.Sureste import Sureste
from classes.orientacion.Suroeste import Suroeste
from abc import ABC,abstractmethod
class Ente(ABC):

    def __init__(self):
        self.vidas = 100
        self.poder = 10
        self.estado = Vivo()
        self.posicion= None
        self.juego = None
        self.observadoresPosicion = []
        self.observadoresVidas = []


    def suscribirPosicion(self,obs):
        self.observadoresPosicion.append(obs)

    def suscribirVida(self,obs):
        self.observadoresVidas.append(obs)

    def setPosicion(self,pos):
        self.posicion = pos
    
    def setVidas(self,vida):
        self.vidas = vida

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
        poder = 0
        defensa = 0
        if unEnte.esPersonaje():
            arma = unEnte.obtenermDerecha()
            if arma is not None:
                poder += arma.obtenerPoder()
        if self.esPersonaje():
            defn = self.obtenermIzquierda()
            if defn is not None:
                defensa += defn.obtenerDefensa() 
        calc = (self.vidas + defensa) - (unEnte.poder + poder)
        if calc > self.vidas:
            self.setVidas(self.vidas)
        else:
            self.setVidas(calc)
        if self.vidas < 0:
            self.setVidas(0)
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

    def irAlNoreste(self):
        self.irA(Noreste.obtenerInstancia())

    def irAlNoroeste(self):
        self.irA(Noroeste.obtenerInstancia())

    def irAlSureste(self):
        self.irA(Sureste.obtenerInstancia())

    def irAlSuroeste(self):
        self.irA(Suroeste.obtenerInstancia())

    def esPersonaje(self):
        return False
    
    def esBicho(self):
        return False
    
    @abstractmethod
    def enteMuere():
        pass
