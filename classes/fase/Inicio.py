from classes.fase.Fase import Fase
from classes.fase.Jugando import Jugando

class Inicio(Fase):
    
    def agregarPersonaje(self, personaje, juego):
        juego.puedeAgregarPersonaje(personaje)

    def lanzarBichos(self,juego):
        juego.puedeLanzarBichos()
        juego.fase = Jugando()

    def esInicio(self):
        return True