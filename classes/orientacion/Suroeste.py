from classes.orientacion.Orientacion import Orientacion

class Suroeste(Orientacion):
    __instance = None

    def __init__(self):
        if Suroeste.__instance is None: #Si aún no hay ninguna instancia la creamos
            Suroeste.__instance = self
    
    def obtenerInstancia():
        if Suroeste.__instance is None:
            Suroeste.__instance = Suroeste()
        
        return Suroeste.__instance
    
    def obtenerElementoEn(self,cont):
        return cont.suroeste
    
    def aceptar(self,visitor,forma):
        print("Visitar suroeste")
        forma.suroeste.aceptar(visitor)

    def ponerElementoEn(self,em,cont):
        cont.suroeste = em

    def obtenerComandosDe(self,forma):
        return forma.suroeste.obtenerComandos()

    def recorrerEn(self,cont,func):
        cont.suroeste.recorrer(func)

    def ir(self,ente):
        cont = ente.posicion.forma
        cont.suroeste.entrar(ente)