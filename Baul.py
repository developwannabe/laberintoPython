from Contenedor import Contenedor

class Baul (Contenedor):

    def entrar(self):
        print("Contenido del baúl: \n")
        map(lambda y:print('   -',str(y),'\n'),self.hijos)

    def esBaul(self):
        return True

    def __str__(self):
        return "Baul " + str(self.num)
    
    def __repr__(self):
        return "Baul " + str(self.num)
