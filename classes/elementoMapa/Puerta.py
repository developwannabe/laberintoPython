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
        self.visitada = False
        self.observadoresAbierto = []

    def entrar(self,ente):
        if self.abierta:
            if ente.posicion == self.lado1:
                self.lado2.entrar(ente)
            else:
                self.lado1.entrar(ente)
        else:
            print(str(ente)," ha chocado con una puerta cerrada.")

    def suscribirAbierto(self,observer):
        self.observadoresAbierto.append(observer)

    def calcularPosicionDesde(self,forma,unPunto):
        if self.visitada:
            return self
        self.visitada=True
        if forma.num == self.lado1.num:
            self.lado2.setPunto(unPunto)
            self.lado2.calcularPosicion()
        else:
            self.lado1.setPunto(unPunto)
            self.lado1.calcularPosicion()

    def aceptar(self,visitor):
        print("Visitar puerta")
        visitor.visitarPuerta(self)

    def abrir(self,ente = None):#Al no existir la sobrecarga de métodos en python, usamos argumentos adicionales
        self.abierta = True
        self.quitarAbrir()
        com1 = Entrar()
        com2 = Cerrar()
        com1.receptor = self
        com2.receptor = self
        self.agregarComando(com1)
        self.agregarComando(com2)
        self.lado1.notificarSuscriptoresAbierto()
        self.lado2.notificarSuscriptoresAbierto()
        self.notificarSuscriptoresAbierto()

    def notificarSuscriptoresAbierto(self):
        for obs in self.observadoresAbierto:
            obs.mostrarPuerta(self)

    def quitarAbrir(self):
        for com in self.comandos:
            if com.esAbrir():
                self.quitarComando(com)
                return

    def cerrar(self,ente = None):
        self.abierta = False
        self.quitarCerrar()
        self.quitarEntrar()
        com = Abrir()
        com.receptor = self
        self.agregarComando(com)
        self.lado1.notificarSuscriptoresAbierto()
        self.lado2.notificarSuscriptoresAbierto()
        self.notificarSuscriptoresAbierto()

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
    
    def estaAbierta(self):
        return self.abierta

    def __str__(self):
        return "Puerta: " + (type(self.lado1).__name__) + " " + str(self.lado1.num) + " - " + (type(self.lado2).__name__) + " " + str(self.lado2.num)
    
    def __repr__(self):
        return "Puerta: " + (type(self.lado1).__name__) + " " + str(self.lado1.num) + " - " + (type(self.lado2).__name__) + " " + str(self.lado2.num)
