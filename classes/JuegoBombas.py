from classes.Juego import Juego
from classes.HabitacionBomba import HabitacionBomba
from classes.ParedBomba import ParedBomba

class JuegoBombas(Juego):

    def fabricarHabitacion(self, num):
        return HabitacionBomba(num)

    def fabricarPared(self):
        return ParedBomba()
    
juego = JuegoBombas()
juego.laberinto2HabFM()
hab = juego.laberinto.obtenerHabitacion(1)
print(juego.laberinto)
print(hab.entrar())
print(hab.entrar())
print(hab.norte.entrar())
print(hab.norte.entrar())