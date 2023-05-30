from classes.ente.Ente import Ente

class Personaje(Ente):
    
    def __init__(self):
        super().__init__()
        self.nick=None

    def enteMuere(self):
        self.juego.personajeMuere()

    def buscarEnemigo(self):
        return self.juego.buscarBicho()
    
    def obtenerComandos(self):
        return self.posicion.obtenerComandos()
    
    def __str__(self):
        return "Personaje " + str(self.nick)
    
    def __repr__(self):
        return "Personaje " + str(self.nick)