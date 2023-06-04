from classes.elementoMapa.objeto.Objeto import Objeto

class Espada (Objeto):

    def __init__(self):
        super().__init__()
        self.material = None

    def aceptar(self,visitor):
        print("Visitar espada")
        visitor.visitarEspada(self)
    
    def usar(self,ente):
        obj = ente.obtenerMDerecha()
        ente.setMDerecha()
        ente.bolsa.borrarDeBolsa(self)
        ente.bolsa.agregarObjeto(obj)

    def __str__(self):
        return "Espada " +str(self.num) + " de "+ str(self.material)
    
    def __repr__(self):
        return "Espada " +str(self.num) + " de "+ str(self.material)
    
    def esEspada(self):
        return True