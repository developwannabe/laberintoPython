from Orientacion import Orientacion

class Oeste(Orientacion):
    __instance = None

    def __init__(self):
        if Oeste.__instance is None: #Si aún no hay ninguna instancia la creamos
            Oeste.__instance = self
            
        return Oeste.__instance #Devolvemos la instancia
    
    def obtenerElementoEn(self,cont):
        return cont.oeste
    
    def ponerElementoEn(self,em,cont):
        cont.oeste = em

    def recorrerEn(self,cont,func):
        cont.oeste.recorrer(func)