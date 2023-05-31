from classes.orientacion.Orientacion import Orientacion

class Sur(Orientacion):
    __instance = None

    def __init__(self):
        if Sur.__instance is None: #Si aún no hay ninguna instancia la creamos
            Sur.__instance = self
    
    def obtenerInstancia():
        if Sur.__instance is None:
            Sur.__instance = Sur()
        
        return Sur.__instance
    
    def obtenerElementoEn(self,cont):
        return cont.sur
    
    def calcularPosicionDesde(self,forma):
        unPunto = (forma.punto[0],forma.punto[1]+1)
        forma.sur.calcularPosicionDesde(forma,unPunto)
    
    def aceptar(self,visitor,forma):
        print("Visitar sur")
        forma.sur.aceptar(visitor)
    
    def ponerElementoEn(self,em,cont):
        cont.sur = em

    def recorrerEn(self,cont,func):
        cont.sur.recorrer(func)

    def obtenerComandosDe(self,forma):
        return forma.sur.obtenerComandos()

    def ir(self,ente):
        cont = ente.posicion.forma
        cont.sur.entrar(ente)