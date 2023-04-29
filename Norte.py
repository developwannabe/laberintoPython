from Orientacion import Orientacion

class Norte(Orientacion):
    __instance = None

    def __init__(self):
        if Norte.__instance is None: #Si aún no hay ninguna instancia la creamos
            Norte.__instance = self
            
        return Norte.__instance #Devolvemos la instancia
    
    def obtenerElementoEn(self,cont):
        return cont.norte
    
    def ponerElementoEn(self,em,cont):
        cont.norte = em

    def recorrerEn(self,cont,func):
        cont.norte.recorrer(func)