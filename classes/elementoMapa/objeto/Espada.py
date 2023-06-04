from classes.elementoMapa.objeto.Objeto import Objeto
from classes.comando.Desequipar import Desequipar
from classes.comando.Usar import Usar


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
        ente.bolsa.usado(self)
        if obj is not None:
            obj.desequipar(ente)
        com = Desequipar()
        com.receptor = self
        self.agregarComando(Desequipar())
        for com in self.comandos:
            if com.esAbrir():
                self.quitarComando(com)
            if com.esUsar():
                self.quitarComando(com)
    
    def desequipar(self,ente):
        ente.bolsa.agregarObjeto(self)
        self.agregarComando(Usar())
        for com in self.comandos:
            if com.esDesequipar():
                self.quitarComando(com)

    def __str__(self):
        return "Espada " +str(self.num) + " de "+ str(self.material)
    
    def __repr__(self):
        return "Espada " +str(self.num) + " de "+ str(self.material)
    
    def esEspada(self):
        return True