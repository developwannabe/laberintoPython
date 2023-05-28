from Orientacion import Orientacion

class Este(Orientacion):
    __instance = None

    def __init__(self):
        if Este.__instance is None: #Si aún no hay ninguna instancia la creamos
            Este.__instance = self
    
    def obtenerInstancia():
        if Este.__instance is None:
            Este.__instance = Este()
        
        return Este.__instance
    
    def obtenerElementoEn(self,cont):
        return cont.este
    
    def ponerElementoEn(self,em,cont):
        cont.este = em

    def recorrerEn(self,cont,func):
        cont.este.recorrer(func)

    def ir(self,ente):
        cont = ente.posicion
        cont.este.entrar(ente)