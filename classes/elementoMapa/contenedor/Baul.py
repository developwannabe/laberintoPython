from classes.elementoMapa.contenedor.Contenedor import Contenedor

class Baul (Contenedor):

    def entrar(self,ente):
        print("Contenido del baúl: \n")
        map(lambda y:print('   -',str(y),'\n'),self.hijos)

    def esBaul(self):
        return True
    
    def aceptar(self,visitor):
        print("Visitar baúl")
        visitor.visitarBaul(self)

    def __str__(self):
        ret = "Baul " + str(self.num) + " con contenido: "
        for i in self.hijos:
            ret = ret + str(i)
        return ret

    
    def __repr__(self):
        ret = "Baul " + str(self.num) + " con contenido: "
        for i in self.hijos:
            ret = ret + str(i)
        return ret
