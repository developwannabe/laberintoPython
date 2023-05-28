from Laberinto import Laberinto
from Puerta import Puerta
from Habitacion import Habitacion
from Pared import Pared
from Norte import Norte
from Este import Este
from Oeste import Oeste
from Sur import Sur
from Bomba import Bomba
from Baul import Baul
from Fuego import Fuego
from Espada import Espada
from Bicho import Bicho
from Personaje import Personaje
from Agresivo import Agresivo
from Perezoso import Perezoso

class LaberintoBuilder():
    
    def __init__(self):
        self.juego = None
        self.laberinto = None
        self.dict = None

    def obtenerJuego(self):
        return self.juego
    
    def fabricarLaberinto(self):
        self.laberinto = Laberinto()
    
    def fabricarModoAgresivo(self):
        return Agresivo()
    
    def fabricarModoPerezoso(self):
        return Perezoso()
    
    def fabricarBicho(self):
        return Bicho()
    
    def fabricarBichoAgresivo(self,posicion):
        bicho = self.fabricarBicho()
        bicho.posicion = posicion
        bicho.modo = self.fabricarModoAgresivo()
        bicho.vidas = 10
        bicho.poder = 3
        return bicho
    
    def fabricarBichoPerezoso(self,posicion):
        bicho = self.fabricarBicho()
        bicho.posicion = posicion
        bicho.modo = self.fabricarModoPerezoso()
        bicho.vidas = 10
        bicho.poder = 1
        return bicho

    
    def fabricarBaul(self,num,hab):
        baul = Baul(num)
        
        p1= self.fabricarPuerta()

        p1.lado1= baul
        p1.lado2 =hab

        baul.ponerElementoEn(self.fabricarNorte(),p1)
        baul.ponerElementoEn(self.fabricarEste(),self.fabricarPared())
        baul.ponerElementoEn(self.fabricarOeste(),self.fabricarPared())
        baul.ponerElementoEn(self.fabricarSur(),self.fabricarPared())

        return baul
    
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
    
    def fabricarBomba(self):
        return Bomba()
    
    def fabricarFuego(self):
        return Fuego()
    
    def fabricarEspada(self):
        return Espada()