from classes.elementoMapa.hoja.decorator.Decorator import Decorator
from classes.comando.Entrar import Entrar

class Bomba (Decorator):

    def __init__(self):
        super().__init__()
        self.num = None
        self.activa = True
        self.observadoresActiva = []
        com = Entrar()
        com.receptor = self
        self.comandos.append(com)

    def esBomba(self):
        return True
    
    def agregarObservadoresActiva(self,obs):
        self.observadoresActiva.append(obs)

    def aceptar(self,visitor):
        print("Visitar bomba")
        visitor.visitarBomba(self)
    
    def entrar(self,ente):
        if self.activa:
            print("La bomba ha explotado.")
            ente.setVidas(ente.vidas - 20)
            self.activa = False
            for com in self.comandos:
                if com.esEntrar():
                    self.comandos.remove(com)
            for obs in self.observadoresActiva:
                obs.mostrarBomba(self)
        else:
            if self.component is not None:
                self.component.entrar(ente)
            else:
                print("Bomba desactivada.")
    
    def __str__(self):
        if self.component is not None:
            return str(self.component) + " decorado con bomba " +str(self.num)+ "."
        else:
            return "Bomba " +str(self.num)+ "."
    
    def __repr__(self):
        if self.component is not None:
            return str(self.component) + " decorado con bomba " +str(self.num)+ "."
        else:
            return "Bomba " +str(self.num)+ "."