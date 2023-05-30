from abc import ABC, abstractmethod
class Comando(ABC):
    
    def __init__(self):
        self.receptor = None
        
    @abstractmethod
    def ejecutar(self, ente):
        pass

    def esAbrir(self):
        return False
    
    def esCerrar(self):
        return False
    
    def esEntrar(self):
        return False
    