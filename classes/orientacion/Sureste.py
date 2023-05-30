from classes.orientacion.Orientacion import Orientacion

class Sureste(Orientacion):
    __instance = None

    def __init__(self):
        if Sureste.__instance is None: #Si aún no hay ninguna instancia la creamos
            Sureste.__instance = self
    
    def obtenerInstancia():
        if Sureste.__instance is None:
            Sureste.__instance = Sureste()
        
        return Sureste.__instance
    
    def obtenerElementoEn(self,cont):
        return cont.sureste
    
    def ponerElementoEn(self,em,cont):
        cont.sureste = em

    def obtenerComandosDe(self,forma):
        return forma.sureste.obtenerComandos()

    def recorrerEn(self,cont,func):
        cont.sureste.recorrer(func)

    def ir(self,ente):
        cont = ente.posicion.forma
        cont.sureste.entrar(ente)