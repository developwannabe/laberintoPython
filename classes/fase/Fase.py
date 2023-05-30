from abc import ABC, abstractmethod
class Fase(ABC):
    
    @abstractmethod
    def agregarPersonaje(self,personaje,juego):
        pass
    
    @abstractmethod
    def lanzarBichos(self,juego):
        pass

    def esInicio(self):
        return False
    
    def esJugando(self):
        return False
    
    def esFinal(self):
        return False