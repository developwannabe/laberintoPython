from classes.orientacion.Orientacion import Orientacion

class Norte(Orientacion):
    __instance = None

    def __init__(self):
        if Norte.__instance is None: #Si aún no hay ninguna instancia la creamos
            Norte.__instance = self
    
    def obtenerInstancia():
        if Norte.__instance is None:
            Norte.__instance = Norte()
        
        return Norte.__instance
    
    def obtenerElementoEn(self,cont):
        return cont.norte
    
    def calcularPosicionDesde(self,forma):
        unPunto = (forma.punto[0],forma.punto[1]-1)
        forma.norte.calcularPosicionDesde(forma,unPunto)
    
    def aceptar(self,visitor,forma):
        print("Visitar norte")
        forma.norte.aceptar(visitor)
    
    def ponerElementoEn(self,em,cont):
        cont.norte = em

    def obtenerComandosDe(self,forma):
        return forma.norte.obtenerComandos()

    def recorrerEn(self,cont,func):
        cont.norte.recorrer(func)

    def ir(self,ente):
        cont = ente.posicion.forma
        cont.norte.entrar(ente)