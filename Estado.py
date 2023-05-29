from abc import ABC,abstractmethod
class Estado(ABC):
    
    @abstractmethod
    def actua(unBicho):
        pass
    
    @abstractmethod
    def enteEsAtacadoPor(self,atacado,atacante):
        pass
    
    @abstractmethod
    def estaVivo(self):
        pass