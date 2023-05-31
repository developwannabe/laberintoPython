from classes.elementoMapa.ElementoMapa import ElementoMapa

class Pared(ElementoMapa):
    
    def entrar(self,ente):
        print("Te has chocado con una pared.")

    def aceptar(self,visitor):
        print("Visitar pared")
        visitor.visitarPared(self)

    def calcularPosicionDesde(self,forma,unPunto):
        pass

    def esPared(self):
        return True
    
    def __str__(self):
        return "Pared"
    
    def __repr__(self):
        return "Pared"