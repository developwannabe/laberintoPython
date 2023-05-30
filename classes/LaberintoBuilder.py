from classes.Laberinto import Laberinto
from classes.Puerta import Puerta
from classes.Habitacion import Habitacion
from classes.Pared import Pared
from classes.Norte import Norte
from classes.Este import Este
from classes.Oeste import Oeste
from classes.Sur import Sur
from classes.Bomba import Bomba
from classes.Baul import Baul
from classes.Fuego import Fuego
from classes.Espada import Espada
from classes.Bicho import Bicho
from classes.Personaje import Personaje
from classes.Agresivo import Agresivo
from classes.Perezoso import Perezoso
from classes.Juego import Juego
from classes.Armario import Armario
from classes.Cuadrado import Cuadrado
from classes.Tunel import Tunel
from classes.Abrir import Abrir

class LaberintoBuilder():
    
    def __init__(self):
        self.juego = None
        self.laberinto = None
        self.dict = None

    def obtenerJuego(self):
        return self.juego
    
    def fabricarJuego(self):
        juego = Juego()
        juego.prototipo = self.laberinto
        juego.laberinto = juego.clonarLaberinto()
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
    
    def fabricarForma(self):
        return Cuadrado()
    
    def fabricarArmario(self,num):
        return Armario(num)
    
    def fabricarTunel(self):
        return Tunel()
    
    def fabricarTunelEn(self,padre):
        tunel = self.fabricarTunel()
        padre.agregarHijo(tunel)

    def fabricarArmarioEn(self,padre,num):
        armario = self.fabricarArmario(num)
        
        p1= self.fabricarPuerta()

        armario.forma= self.fabricarForma()
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
    
    def fabricarAbrir(self):
        return Abrir()

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

        com = self.fabricarAbrir()
        com.receptor = puerta
        puerta.agregarComando(com)

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