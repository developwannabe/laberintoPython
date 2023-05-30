from classes.fase.Fase import Fase

class Final(Fase):
    
    def agregarPersonaje(self, personaje, juego):
        print("No se puede añadir el personaje, el juego ha terminado.")

    def lanzarBichos(self,juego):
        print("El juego ya ha terminado.")

    def esFinal(self):
        return True
    