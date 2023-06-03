from classes.ente.Ente import Ente
from classes.cuerpo.Cuerpo import Cuerpo

class Personaje(Ente):
    
    def __init__(self):
        super().__init__()
        self.nick=None
        self.bolsa=None
        self.cuerpo = Cuerpo()

    def obtenermIzquierda(self):
        return self.cuerpo.obtenermIzquierda()
    
    def obtenermDerecha(self):
        return self.cuerpo.obtenermDerecha()
    
    def setmIzquierda(self,obj):
        self.cuerpo.setmIzquierda(obj)

    def setmDerecha(self,obj):
        self.cuerpo.setmDerecha(obj)

    def setPosicion(self, pos):
        self.posicion= pos
        for obs in self.observadoresPosicion:
            obs.mostrarPersonaje()
    
    def setVidas(self, vida):
        self.vidas = vida
        for obs in self.observadoresVidas:
            obs.mostrarVidasPersonaje()
    
    def enteMuere(self):
        self.juego.personajeMuere()

    def buscarEnemigo(self):
        return self.juego.buscarBicho()
    
    def obtenerComandos(self,ente):
        return self.posicion.obtenerComandos(self)
    
    def __str__(self):
        return "Personaje " + str(self.nick)
    
    def __repr__(self):
        return "Personaje " + str(self.nick)