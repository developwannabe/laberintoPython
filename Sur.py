from Orientacion import Orientacion

class Sur(Orientacion):
    __instance = None

    def __init__(self):
        if Sur.__instance is None: #Si aún no hay ninguna instancia la creamos
            Sur.__instance = self
            
        return Sur.__instance #Devolvemos la instancia
    
    def obtenerElementoEn(self,cont):
        return cont.sur
    
    def ponerElementoEn(self,em,cont):
        cont.sur = em

    def recorrerEn(self,cont,func):
        cont.sur.recorrer(func)