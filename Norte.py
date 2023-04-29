from Orientacion import Orientacion

class Norte(Orientacion):
    __instance = None

    def __init__(self):
        if Norte.__instance is None: #Si aún no hay ninguna instancia la creamos
            Norte.__instance = self
    
    def obtenerInstancia():
        if Norte.__instance is None:
            Norte.__instance = Norte()
            return Norte.__instance
        else:
            return Norte.__instance
    
    def obtenerElementoEn(self,cont):
        return cont.norte
    
    def ponerElementoEn(self,em,cont):
        cont.norte = em

    def recorrerEn(self,cont,func):
        cont.norte.recorrer(func)