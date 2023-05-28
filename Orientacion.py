from abc import ABC, abstractmethod

class Orientacion(ABC):

    @abstractmethod
    def obtenerElementoEn(self,cont):
        pass

    @abstractmethod
    def ponerElementoEn(self,em,cont):
        pass
    
    @abstractmethod
    def recorrerEn(self,cont,func):
        pass

    @abstractmethod
    def ir(ente):
        pass