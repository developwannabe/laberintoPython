from classes.elementoMapa.objeto.Objeto import Objeto
from classes.comando.Desequipar import Desequipar
from classes.comando.Usar import Usar
from classes.comando.Soltar import Soltar


class Espada(Objeto):

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
        if obj is not None:
            obj.desequipar(ente)
        ente.setmDerecha(self)
        ente.bolsa.usado(self)
        com = Desequipar()
        com.receptor = self
        self.agregarComando(com)
        for coma in self.comandos:
            if coma.esSoltar():
                self.quitarComando(coma)
        for coma in self.comandos:
            if coma.esUsar():
                self.quitarComando(coma)
    
    def desequipar(self,ente):
        ente.setmDerecha(None)
        ente.bolsa.agregarObjeto(self)
        com1 = Usar()
        com1.receptor= self
        com2 = Soltar()
        com2.receptor = self
        self.agregarComando(com1)
        self.agregarComando(com2)
        for com in self.comandos:
            if com.esDesequipar():
                self.quitarComando(com)

    def __str__(self):
        return "Espada " +str(self.num) + " de "+ str(self.material)
    
    def __repr__(self):
        return "Espada " +str(self.num) + " de "+ str(self.material)
    
    def esEspada(self):
        return True