from classes.elementoMapa.objeto.Objeto import Objeto

class Banana(Objeto):

    def __init__(self):
        super().__init__()
        self.vida = 20

    def esBanana(self):
        return True
    
    def entrar(self,ente):
        pass#TODO:Meter en la bolsa del personaje.
    
    def aceptar(self,visitor):
        visitor.visitarBanana(self)

    def usar(self,ente):
        ente.vidas += self.vida