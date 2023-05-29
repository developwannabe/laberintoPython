class Forma():
    
    def __init__(self):
        self.orientaciones = []
        self.num = None

    def agregarOrientacion(self, orientacion):
        self.orientaciones.append(orientacion)
    
    def obtenerElemento(self, unaOr):
        return unaOr.obtenerElementoEn(unaOr)
    
    def ponerElementoEn(self,unaOr,elemento):
        unaOr.ponerElementoEn(elemento,self)

    def recorrer(self,func):
        for ori in self.orientaciones:
            ori.recorrerEn(self,func)