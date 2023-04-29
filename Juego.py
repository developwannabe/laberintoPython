from Laberinto import Laberinto
from Puerta import Puerta
from Habitacion import Habitacion
from Pared import Pared
from Norte import Norte
from Este import Este
from Oeste import Oeste
from Sur import Sur

class Juego():

    def __init__(self):
        self.laberinto = None

    #Métodos iterator

    def abrirPuertas(self):
        funcl = lambda x: x.abrir() if x.esPuerta() else None
        self.laberinto.recorrer(funcl)
    #Métodos para el Factory Method

    def fabricarLaberinto(self):
        return Laberinto()

    def fabricarPuerta(self):
        return Puerta()

    def fabricarHabitacion(self,num):
        hab = Habitacion(num)

        hab.ponerElementoEn(self.fabricarNorte(),self.fabricarPared())
        hab.ponerElementoEn(self.fabricarEste(),self.fabricarPared())
        hab.ponerElementoEn(self.fabricarOeste(),self.fabricarPared())
        hab.ponerElementoEn(self.fabricarSur(),self.fabricarPared())

        hab.agregarOrientacion(self.fabricarNorte())
        hab.agregarOrientacion(self.fabricarEste())
        hab.agregarOrientacion(self.fabricarOeste())
        hab.agregarOrientacion(self.fabricarSur())

        return hab

    def fabricarPared(self):
        return Pared()

    def fabricarNorte(self):
        return Norte.obtenerInstancia()
    
    def fabricarEste(self):
        return Este.obtenerInstancia()
    
    def fabricarOeste(self):
        return Oeste.obtenerInstancia()
    
    def fabricarSur(self):
        return Sur.obtenerInstancia()
    
    #Final de los métodos para el Factory Method

    #Fabricación de laberintos

    #Laberinto para la segunda entrega

    def laberinto2Entrega(self):
        self.laberinto = self.fabricarLaberinto()

        hab1 = self.fabricarHabitacion(1)
        hab2 = self.fabricarHabitacion(2)
        hab3 = self.fabricarHabitacion(3)
        hab4 = self.fabricarHabitacion(4)

        p1 = self.fabricarPuerta()
        p2 = self.fabricarPuerta()
        p3 = self.fabricarPuerta()
        p4 = self.fabricarPuerta()

        p1.lado1= hab1
        p1.lado2= hab2

        p2.lado1= hab2
        p2.lado2= hab4

        p3.lado1 = hab4
        p3.lado2 = hab3

        p4.lado1 = hab3
        p4.lado2 = hab1

        hab1.ponerElementoEn(self.fabricarEste(),p1)
        hab1.ponerElementoEn(self.fabricarSur(),p4)

        hab2.ponerElementoEn(self.fabricarOeste(),p1)
        hab2.ponerElementoEn(self.fabricarSur(),p2)

        hab3.ponerElementoEn(self.fabricarNorte(),p4)
        hab3.ponerElementoEn(self.fabricarEste(),p3)

        hab4.ponerElementoEn(self.fabricarNorte(),p2)
        hab4.ponerElementoEn(self.fabricarOeste(),p3)

        self.laberinto.agregarHabitacion(hab1)
        self.laberinto.agregarHabitacion(hab2)
        self.laberinto.agregarHabitacion(hab3)
        self.laberinto.agregarHabitacion(hab4)

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
