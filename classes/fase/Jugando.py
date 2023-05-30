from classes.fase.Fase import Fase

class Jugando(Fase):

    def agregarPersonaje(self, personaje, juego):
        print("No se puede añadir el personaje, el juego ha comenzado.")

    def lanzarBichos(self,juego):
        print("El juego ya ha comenzado.")

    def esJugando(self):
        return True
    