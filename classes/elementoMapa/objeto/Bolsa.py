from classes.elementoMapa.objeto.Objeto import Objeto

class Bolsa(Objeto):
    
    def __init__(self):
        super().__init__()
        self.capacidad = 9
        self.hijos = []

    def entrar(self,ente):
        pass#TODO:Mostrar bolsa

    def usar(self,ente):
        pass#TODO:Mostrar bolsa

    def agregarObjeto(self,obj):
        if len(self.hijos) < self.capacidad:
            self.hijos.append(obj)
        else:
            print("No caben más objetos en la bolsa.")

    def soltarObjeto(self,obj):
        self.hijos.remove(obj)

    def recorrer(self,func):
        func(self)
        map(func,self.hijos)

    def aceptar(self,visitor):
        visitor.visitarBolsa(self)

    def obtenerComandos(self):
        listaComandos = []
        listaComandos.extend(self.comandos)
        for hijo in self.hijos:
            listaComandos.extend(hijo.obtenerComandos())
        return listaComandos
    
    def esBolsa(self):
        return True