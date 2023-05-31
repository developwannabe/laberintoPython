from classes.orientacion.Orientacion import Orientacion

class Noreste(Orientacion):
    __instance = None

    def __init__(self):
        if Noreste.__instance is None: #Si aún no hay ninguna instancia la creamos
            Noreste.__instance = self
    
    def obtenerInstancia():
        if Noreste.__instance is None:
            Noreste.__instance = Noreste()
        
        return Noreste.__instance
    
    def obtenerElementoEn(self,cont):
        return cont.noreste
    
    def aceptar(self,visitor,forma):
        print("Visitar noreste")
        forma.noreste.aceptar(visitor)
    
    def ponerElementoEn(self,em,cont):
        cont.noreste = em

    def obtenerComandosDe(self,forma):
        return forma.noreste.obtenerComandos()

    def recorrerEn(self,cont,func):
        cont.noreste.recorrer(func)

    def ir(self,ente):
        cont = ente.posicion.forma
        cont.noreste.entrar(ente)