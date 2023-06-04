from abc import ABC
class Material(ABC):

    def __init__(self):
        self.poder = None
        self.usos = None
    
    def getPoder(self):
        return self.poder
    
    def setPoder(self,poder):
        self.poder = poder

    def getUsos(self):
        return self.usos
    
    def setUsos(self,usos):
        self.usos = usos

    def esMadera(self):
        return False
    
    def esMetal(self):
        return False
    
    def esDiamante(self):
        return False

        