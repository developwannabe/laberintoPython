from classes.elementoMapa.objeto.Objeto import Objeto
from classes.comando.Desequipar import Desequipar
from classes.comando.Usar import Usar
from classes.comando.Soltar import Soltar

class Escudo(Objeto):

    def __init__(self):
        super().__init__()
        self.defensa = 4

    def aceptar(self,visitor):
        print("Visitar escudo")
        visitor.visitarEscudo(self)
    
    def obtenerDefensa(self):
        return self.defensa
    
    def usar(self,ente):
        obj = ente.obtenermIzquierda()
        ente.setmIzquierda(self)
        ente.bolsa.usado(self)
        if obj is not None:
            obj.desequipar(ente)
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
        ente.setmIzquierda(None)
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
        return "Escudo " +str(self.num)
    
    def __repr__(self):
        return "Escudo " +str(self.num)
    
    def esEscudo(self):
        return True