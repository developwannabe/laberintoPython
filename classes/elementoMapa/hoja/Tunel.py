from classes.elementoMapa.hoja.Hoja import Hoja

class Tunel(Hoja):
    
    def __init__(self):
        super().__init__()
        self.laberinto = None

    def entrar(self,ente): #TODO: Arreglar vuelta al laberinto
        if self.laberinto is None:
            self.laberinto = ente.juego.clonarLaberinto()
        self.laberinto.entrar(ente)

    def esTunel(self):
        return True
    
    def __str__(self):
        return "Túnel"
    
    def __repr__(self):
        return "Túnel"