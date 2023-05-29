from Ente import Ente

class Personaje(Ente):
    
    def __init__(self):
        super().__init__()
        self.nick=None

    def enteMuere(self):
        print(str(self), " ha muerto.")
        self.juego.terminarBichos()

    def buscarEnemigo(self):
        return self.juego.buscarBicho()
    
    def __str__(self):
        return "Personaje " + str(self.nick)
    
    def __repr__(self):
        return "Personaje " + str(self.nick)