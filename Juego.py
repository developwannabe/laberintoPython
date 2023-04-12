from Laberinto import Laberinto
from Puerta import Puerta
from Habitacion import Habitacion
from Pared import Pared

class Juego():

    def __init__(self):
        self.laberinto = None

    #Métodos para el Factory Method

    def fabricarLaberinto(self):
        return Laberinto()

    def fabricarPuerta(self):
        return Puerta()

    def fabricarHabitacion(self,num):
        return Habitacion(num)

    def fabricarPared(self):
        return Pared()

    #Final de los métodos para el Factory Method

    #Fabricación de laberintos

    #Fabricación con FactoryMethod

    def laberinto2HabFM(self):

        self.laberinto = self.fabricarLaberinto()

        hab1 = self.fabricarHabitacion(1)
        hab2 = self.fabricarHabitacion(2)

        puerta = self.fabricarPuerta()

        puerta.lado1 = hab1
        puerta.lado2 = hab2

        hab1.sur = puerta
        hab2.norte = puerta

        hab1.norte= self.fabricarPared()
        hab1.este= self.fabricarPared()
        hab1.oeste= self.fabricarPared()

        hab2.este= self.fabricarPared()
        hab2.oeste= self.fabricarPared()
        hab2.sur= self.fabricarPared()

        self.laberinto.agregarHabitacion(hab1)
        self.laberinto.agregarHabitacion(hab2)

    #Fabricación clásica
    def laberinto2Hab(self):
        self.laberinto = Laberinto()

        hab1 = Habitacion(1)
        hab2 = Habitacion(2)

        puerta = Puerta()

        hab1.sur = puerta
        hab2.norte = puerta

        puerta.lado1 = hab1
        puerta.lado2 = hab2

        hab1.norte= Pared()
        hab1.este= Pared()
        hab1.oeste= Pared()

        hab2.este= Pared()
        hab2.oeste= Pared()
        hab2.sur= Pared()

        self.laberinto.agregarHabitacion(hab1)
        self.laberinto.agregarHabitacion(hab2)

juego = Juego()

juego.laberinto2HabFM()

print(juego.laberinto)