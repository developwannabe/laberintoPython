from classes.orientacion.Orientacion import Orientacion

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
    
    def calcularPosicionDesde(self,forma):
        unPunto = (forma.punto[0] + 1,forma.punto[1])
        forma.este.calcularPosicionDesde(forma,unPunto)
    
    def aceptar(self,visitor,forma):
        print("Visitar este")
        forma.este.aceptar(visitor)
    
    def ponerElementoEn(self,em,cont):
        cont.este = em

    def obtenerComandosDe(self,forma,ente):
        return forma.este.obtenerComandos(ente)

    def recorrerEn(self,cont,func):
        cont.este.recorrer(func)

    def ir(self,ente):
        cont = ente.posicion.forma
        cont.este.entrar(ente)