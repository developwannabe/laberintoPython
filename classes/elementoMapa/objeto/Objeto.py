from classes.elementoMapa.ElementoMapa import ElementoMapa
from abc import ABC,abstractmethod

class Objeto(ElementoMapa,ABC):
    
    def __init__(self):
        super().__init__()
        self.num = None
        
    def entrar(self,ente):
        ente.bolsa.agregarObjeto(self)

    @abstractmethod
    def usar(self,ente):
        pass
