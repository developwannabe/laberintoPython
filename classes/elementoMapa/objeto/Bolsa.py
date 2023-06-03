from classes.elementoMapa.objeto.Objeto import Objeto

class Bolsa(Objeto):
    
    def __init__(self):
        super().__init__()
        self.capacidad = 5
        self.hijos = []
        self.observadoresBolsa = []

    def entrar(self,ente):
        pass

    def usar(self,ente):
        pass

    def borrarDeBolsa(self,obj):
        obj.padre = None
        self.hijos.remove(obj)
        for obs in self.observadoresBolsa:
                obs.mostrarBolsa(self)

    def agregarObjeto(self,obj):
        if len(self.hijos) < self.capacidad:
            obj.padre = self
            self.hijos.append(obj)
            for obs in self.observadoresBolsa:
                obs.mostrarBolsa(self)
        else:
            print("No caben más objetos en la bolsa.")

    def usado(self,hijo):
        self.hijos.remove(hijo)
        hijo.padre = None
        for obs in self.observadoresBolsa:
                obs.mostrarBolsa(self)


    def obtenerComandos(self,ente):
        listaComandos = []
        listaComandos.extend(self.comandos)
        for hijo in self.hijos:
            listaComandos.extend(hijo.obtenerComandos(ente))
        return listaComandos
    
    def observarBolsa(self,obs):
        self.observadoresBolsa.append(obs)


    def soltarObjeto(self,obj):
        self.hijos.remove(obj)
        for obs in self.observadoresBolsa:
            obs.mostrarBolsa(self)

    def recorrer(self,func):
        func(self)
        map(func,self.hijos)

    def aceptar(self,visitor):
        visitor.visitarBolsa(self)

    def obtenerComandos(self,ente):
        listaComandos = []
        listaComandos.extend(self.comandos)
        for hijo in self.hijos:
            listaComandos.extend(hijo.obtenerComandos(ente))
        return listaComandos
    
    def esBolsa(self):
        return True