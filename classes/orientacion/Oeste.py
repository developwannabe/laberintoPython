from classes.orientacion.Orientacion import Orientacion

class Oeste(Orientacion):
    __instance = None

    def __init__(self):
        if Oeste.__instance is None: #Si aún no hay ninguna instancia la creamos
            Oeste.__instance = self
    
    def obtenerInstancia():
        if Oeste.__instance is None:
            Oeste.__instance = Oeste()
            
        return Oeste.__instance
    
    def obtenerElementoEn(self,cont):
        return cont.oeste
    
    def calcularPosicionDesde(self,forma):
        unPunto = (forma.punto[0] - 1,forma.punto[1])
        forma.oeste.calcularPosicionDesde(forma,unPunto)
    
    def aceptar(self,visitor,forma):
        print("Visitar oeste")
        forma.oeste.aceptar(visitor)
    
    def ponerElementoEn(self,em,cont):
        cont.oeste = em

    def recorrerEn(self,cont,func):
        cont.oeste.recorrer(func)

    def obtenerComandosDe(self,forma):
        return forma.oeste.obtenerComandos()

    def ir(self,ente):
        cont = ente.posicion.forma
        cont.oeste.entrar(ente)