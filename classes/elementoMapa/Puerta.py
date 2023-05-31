from classes.elementoMapa.ElementoMapa import ElementoMapa
from classes.comando.Abrir import Abrir
from classes.comando.Entrar import Entrar
from classes.comando.Cerrar import Cerrar

class Puerta(ElementoMapa):

    def __init__(self): 
        super().__init__()
        self.abierta = False
        self.lado1 = None
        self.lado2 = None

    def entrar(self,ente):
        if self.abierta:
            if ente.posicion == self.lado1:
                self.lado2.entrar(ente)
            else:
                self.lado1.entrar(ente)
        else:
            print(str(ente)," ha chocado con una puerta cerrada.")

    def aceptar(self,visitor):
        print("Visitar puerta")
        visitor.visitarPuerta(self)

    def abrir(self,ente = None):#Al no existir la sobrecarga de métodos en python, usamos argumentos adicionales
        self.abierta = True
        if ente is not None:
            self.quitarAbrir()
            com1 = Entrar()
            com2 = Cerrar()
            com1.receptor = self
            com2.receptor = self
            self.agregarComando(com1)
            self.agregarComando(com2)
    
    def quitarAbrir(self):
        for com in self.comandos:
            if com.esAbrir():
                self.quitarComando(com)
                return

    def cerrar(self,ente = None):
        self.abierta = False
        if ente is not None:
            self.quitarCerrar()
            self.quitarEntrar()
            com = Abrir()
            com.receptor = self
            self.agregarComando(com)

    def quitarCerrar(self):
        for com in self.comandos:
            if com.esCerrar():
                self.quitarComando(com)
                return
    
    def quitarEntrar(self):
        for com in self.comandos:
            if com.esEntrar():
                self.quitarComando(com)
                return
        
    def esPuerta(self):
        return True

    def __str__(self):
        return "Puerta: Lado 1 es Hab " + str(self.lado1.num) +", Lado 2 es hab " + str(self.lado2.num) + '. Abierta: ' +str(self.abierta)
    
    def __repr__(self):
        return "Puerta: Lado 1 es Hab " + str(self.lado1.num) +", Lado 2 es hab " + str(self.lado2.num) + '. Abierta: ' +str(self.abierta)
