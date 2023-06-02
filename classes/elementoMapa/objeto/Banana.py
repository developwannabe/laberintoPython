from classes.elementoMapa.objeto.Objeto import Objeto

class Banana(Objeto):

    def __init__(self):
        super().__init__()
        self.vida = 20

    def esBanana(self):
        return True
    
    
    def aceptar(self,visitor):
        visitor.visitarBanana(self)

    def usar(self,ente):
        ente.vidas += self.vida

    def __str__(self):
        return "Banana " + str(self.num)
    
    def __repr__(self):
        return "Banana " + str(self.num)