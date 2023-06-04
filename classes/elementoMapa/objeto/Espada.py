from classes.elementoMapa.objeto.Objeto import Objeto
from classes.comando.Desequipar import Desequipar

class Espada (Objeto):

    def __init__(self):
        super().__init__()
        self.material = None

    def aceptar(self,visitor):
        print("Visitar espada")
        visitor.visitarEspada(self)
    
    def obtenerPoder(self):
        return self.material.poder
    
    def usar(self,ente):
        obj = ente.obtenermDerecha()
        ente.setmDerecha(self)
        ente.bolsa.borrarDeBolsa(self)
        if obj is not None:
            ente.bolsa.agregarObjeto(obj)
        com = Desequipar()
        com.receptor = self
        self.agregarComando(Desequipar())

    def __str__(self):
        return "Espada " +str(self.num) + " de "+ str(self.material)
    
    def __repr__(self):
        return "Espada " +str(self.num) + " de "+ str(self.material)
    
    def esEspada(self):
        return True