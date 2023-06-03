from classes.elementoMapa.objeto.Objeto import Objeto

class Espada (Objeto):

    def __init__(self):
        super().__init__()
        self.poder = 10
        self.usos = 5

    def aceptar(self,visitor):
        print("Visitar espada")
        visitor.visitarEspada(self)
    
    def usar(self,ente):
        obj = ente.obtenerMDerecha()
        ente.setMDerecha()
        ente.bolsa.borrarDeBolsa(self)
        ente.bolsa.agregarObjeto(obj)

    def __str__(self):
        return "Espada"
    
    def __repr__(self):
        return "Espada"
    
    def esEspada(self):
        return True