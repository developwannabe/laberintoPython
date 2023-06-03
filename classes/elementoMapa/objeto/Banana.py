from classes.elementoMapa.objeto.Objeto import Objeto

class Banana(Objeto):

    def __init__(self):
        super().__init__()
        self.vida = 20

    def esBanana(self):
        return True
    
    def aceptar(self,visitor):
        print("Visitar banana")
        visitor.visitarBanana(self)

    def usar(self,ente):
        ente.setVidas(ente.vidas + self.vida)
        self.padre.usado(self)

    def __str__(self):
        return "Banana " + str(self.num)
    
    def __repr__(self):
        return "Banana " + str(self.num)