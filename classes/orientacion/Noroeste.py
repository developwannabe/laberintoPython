from classes.orientacion.Orientacion import Orientacion

class Noroeste(Orientacion):
    __instance = None

    def __init__(self):
        if Noroeste.__instance is None: #Si aún no hay ninguna instancia la creamos
            Noroeste.__instance = self
    
    def obtenerInstancia():
        if Noroeste.__instance is None:
            Noroeste.__instance = Noroeste()
        
        return Noroeste.__instance
    
    def obtenerElementoEn(self,cont):
        return cont.noroeste
    
    def aceptar(self,visitor,forma):
        print("Visitar noroeste")
        forma.noroeste.aceptar(visitor)

    def ponerElementoEn(self,em,cont):
        cont.noroeste = em

    def obtenerComandosDe(self,forma,ente):
        return forma.noroeste.obtenerComandos(ente)
    
    def calcularPosicionDesde(self,forma):
        pass

    def recorrerEn(self,cont,func):
        cont.noroeste.recorrer(func)

    def ir(self,ente):
        cont = ente.posicion.forma
        cont.noroeste.entrar(ente)