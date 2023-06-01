from classes.elementoMapa.ElementoMapa import ElementoMapa
from abc import ABC,abstractmethod

class Objeto(ElementoMapa,ABC):
    
    @abstractmethod
    def usar(self,ente):
        pass
