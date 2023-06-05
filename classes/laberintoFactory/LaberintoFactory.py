from classes.elementoMapa.contenedor.Laberinto import Laberinto
from classes.elementoMapa.Puerta import Puerta
from classes.elementoMapa.contenedor.habitacion.Habitacion import Habitacion
from classes.elementoMapa.pared.Pared import Pared
from classes.orientacion.Norte import Norte
from classes.orientacion.Este import Este
from classes.orientacion.Oeste import Oeste
from classes.orientacion.Sur import Sur
from classes.elementoMapa.hoja.decorator.Bomba import Bomba
from classes.elementoMapa.objeto.Espada import Espada
from classes.ente.Bicho import Bicho
from classes.modo.Agresivo import Agresivo
from classes.modo.Perezoso import Perezoso
from classes.forma.Cuadrado import Cuadrado

class LaberintoFactory():
    def fabricarLaberinto(self):
        return Laberinto()
    
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

    
    def fabricarPuerta(self):
        return Puerta()

    def fabricarForma(self):
        return Cuadrado()
    
    def fabricarHabitacion(self,num):
        hab = Habitacion(num)

        forma = self.fabricarForma()
        forma.num= num
        hab.forma = forma

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
    
    
    def fabricarEspada(self):
        return Espada()