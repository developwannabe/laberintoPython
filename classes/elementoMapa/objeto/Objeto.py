from classes.elementoMapa.ElementoMapa import ElementoMapa
from classes.comando.Soltar import Soltar
from classes.comando.Coger import Coger
from abc import ABC,abstractmethod

class Objeto(ElementoMapa,ABC):
    
    def __init__(self):
        super().__init__()
        self.num = None
        
    def entrar(self,ente):
        ente.bolsa.agregarObjeto(self)
        self.padre.hijos.remove(self)
        for com in self.comandos:
            if com.esCoger():
                self.quitarComando(com)
        self.agregarComando(Soltar())

    def soltar(self,ente):
        ente.posicion.agregarHijo(self)
        ente.bolsa.soltarObjeto(self)
        for com in self.comandos:
            if com.esSoltar():
                self.quitarComando(com)
        self.agregarComando(Coger())

    @abstractmethod
    def usar(self,ente):
        pass
