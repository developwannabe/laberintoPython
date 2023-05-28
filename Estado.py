from abc import ABC,abstractmethod
class Estado(ABC):
    
    @abstractmethod
    def actua(unBicho):
        pass
    
    @abstractmethod
    def enteEsAtacadoPor(atacado,atacante):
        pass
    
    @abstractmethod
    def estaVivo(self):
        pass