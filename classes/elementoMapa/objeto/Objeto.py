from classes.elementoMapa.ElementoMapa import ElementoMapa
from abc import ABC,abstractmethod

class Objeto(ElementoMapa,ABC):
    
    def __init__(self):
        super().__init__()
        self.num = None
        
    @abstractmethod
    def usar(self,ente):
        pass
