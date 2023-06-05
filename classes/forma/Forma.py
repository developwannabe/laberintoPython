class Forma():
    
    def __init__(self):
        self.orientaciones = []
        self.num = None
        self.punto = None
        self.extent = None

    def agregarOrientacion(self, orientacion):
        self.orientaciones.append(orientacion)
    
    def obtenerComandos(self,ente):
        listaComandos = []
        for ori in self.orientaciones:
            listaComandos.extend(ori.obtenerComandosDe(self,ente))
        return listaComandos
    
    def calcularPosicion(self):
        for ori in self.orientaciones:
            ori.calcularPosicionDesde(self)
    
    def aceptar(self,visitor):
        for ori in self.orientaciones:
            ori.aceptar(visitor,self)

    def obtenerElemento(self, unaOr):
        return unaOr.obtenerElementoEn(unaOr)
    
    def ponerElementoEn(self,unaOr,elemento):
        unaOr.ponerElementoEn(elemento,self)

    def recorrer(self,func):
        for ori in self.orientaciones:
            ori.recorrerEn(self,func)

    def esCuadrado(self):
        return False
    
    def esRombo(self):
        return False