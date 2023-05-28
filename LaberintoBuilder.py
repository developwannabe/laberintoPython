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
from Juego import Juego
from Armario import Armario

class LaberintoBuilder():
    
    def __init__(self):
        self.juego = None
        self.laberinto = None
        self.dict = None

    def obtenerJuego(self):
        return self.juego
    
    def fabricarJuego(self):
        juego = Juego()
        juego.laberinto = self.laberinto
        self.juego = juego
        return juego
    
    def fabricarLaberinto(self):
        self.laberinto = Laberinto()
    
    def fabricarModoAgresivo(self):
        return Agresivo()
    
    def fabricarModoPerezoso(self):
        return Perezoso()
    
    def fabricarBicho(self):
        return Bicho()
    
    def fabricarArmario(self,num):
        return Armario(num)
    
    def fabricarArmarioEn(self,padre,num):
        armario = self.fabricarArmario(num)
        
        p1= self.fabricarPuerta()

        p1.lado1= armario
        p1.lado2 = padre

        armario.ponerElementoEn(self.fabricarNorte(),self.fabricarPared())
        armario.ponerElementoEn(self.fabricarEste(),self.fabricarPared())
        armario.ponerElementoEn(self.fabricarOeste(),self.fabricarPared())
        armario.ponerElementoEn(self.fabricarSur(),p1)

        padre.agregarHijo(armario)

    def fabricarBombaEn(self,padre):
        bomba = self.fabricarBomba()
        padre.agregarHijo(bomba)
        
    
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

    def fabricarBichoL(self,modo,posicion):
        hab = self.juego.obtenerHabitacion(posicion)

        if modo == "agresivo":
            bicho = self.fabricarBichoAgresivo(hab)
        if modo == "perezoso":
            bicho = self.fabricarBichoPerezoso(hab)
        
        if bicho is not None:
            self.juego.agregarBicho(bicho)
    
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

        self.laberinto.agregarHabitacion(hab)

        return hab

    def fabricarPuertaL(self,n1,or1,n2,or2):
        lado1=self.laberinto.obtenerHabitacion(n1)
        lado2=self.laberinto.obtenerHabitacion(n2)

        ori1=getattr(self,'fabricar'+or1)()
        ori2=getattr(self,'fabricar'+or2)()

        puerta = self.fabricarPuerta()

        puerta.lado1=lado1
        puerta.lado2=lado2

        lado1.ponerElementoEn(ori1,puerta)
        lado2.ponerElementoEn(ori2,puerta)


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