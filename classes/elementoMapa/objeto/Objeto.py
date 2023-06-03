from classes.elementoMapa.ElementoMapa import ElementoMapa
from classes.comando.Soltar import Soltar
from classes.comando.Coger import Coger
from classes.comando.Usar import Usar
from abc import ABC,abstractmethod

class Objeto(ElementoMapa,ABC):
    
    def __init__(self):
        super().__init__()
        self.num = None
        self.observadoresPosicion = []
        
    def entrar(self,ente):
        self.padre.hijos.remove(self)
        ente.bolsa.agregarObjeto(self)
        for com in self.comandos:
            if com.esCoger():
                self.quitarComando(com)
        self.agregarComando(Soltar())
        self.agregarComando(Usar())
        for obs in self.observadoresPosicion:
            obs.mostrarObjeto(self)

    def soltar(self,ente):
        ente.posicion.agregarHijo(self)
        ente.bolsa.soltarObjeto(self)
        for com in self.comandos:
            if com.esSoltar():
                self.quitarComando(com)
        for com in self.comandos:
            if com.esUsar():
                self.quitarComando(com)
        self.agregarComando(Coger())
        for obs in self.observadoresPosicion:
            obs.mostrarObjeto(self)

    def agregarObservadorPosicion(self,obs):
        self.observadoresPosicion.append(obs)

    @abstractmethod
    def usar(self,ente):
        pass
