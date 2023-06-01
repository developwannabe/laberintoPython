from abc import ABC, abstractmethod

class ElementoMapa(ABC):
    
    def __init__(self):
        self.padre = None
        self.comandos = []

    @abstractmethod 
    def entrar(self,ente):
        pass
    
    @abstractmethod
    def aceptar(self,visitor):
        pass

    def agregarComando(self,comando):
        for comandoP in self.comandos:
            if comandoP.equals(comando):
                return
        self.comandos.append(comando)

    def obtenerComandos(self,ente):
        return self.comandos
    
    def quitarComando(self,comando):
        self.comandos.remove(comando)

    def recorrer(self, funcion):
        funcion(self)

    def esHabitacion(self):
        return False
    
    def esBomba(self):
        return False
    
    def esPared(self):
        return False
    
    def esPuerta(self):
        return False
    
    def esBaul(self):
        return False
    
    def esEspada(self):
        return False
    
    def esFuego(self):
        return False

    def esArmario(self):
        return False
    
    def esTunel(self):
        return False
    
    def esBolsa(self):
        return False
    
    def esBanana(self):
        return False