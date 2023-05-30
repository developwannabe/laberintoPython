from classes.elementoMapa.contenedor.Laberinto import Laberinto
from classes.elementoMapa.Puerta import Puerta
from classes.elementoMapa.contenedor.habitacion.Habitacion import Habitacion
from classes.elementoMapa.pared.Pared import Pared
from classes.orientacion.Norte import Norte
from classes.orientacion.Este import Este
from classes.orientacion.Oeste import Oeste
from classes.orientacion.Sur import Sur
from classes.elementoMapa.hoja.decorator.Bomba import Bomba
from classes.elementoMapa.contenedor.Baul import Baul
from classes.elementoMapa.hoja.decorator.Fuego import Fuego
from classes.elementoMapa.hoja.decorator.Espada import Espada
from classes.ente.Bicho import Bicho
from classes.modo.Agresivo import Agresivo
from classes.modo.Perezoso import Perezoso
from classes.fase.Inicio import Inicio
from classes.fase.Final import Final
import threading
import copy

class Juego():

    def __init__(self):
        self.laberinto = None
        self.personaje = None
        self.bichos = []
        self.prototipo = None
        self.hilos={}
        self.fase = Inicio()
        self.ganaPersonaje = True

    def obtenerHabitacion(self,num):
        return self.laberinto.obtenerHabitacion(num)
    
    #Métodos Personaje
    
    def obtenerHijosPosicion(self):
        return self.personaje.posicion.obtenerHijos()
    
    def agregarPersonaje(self,personaje):
        self.fase.agregarPersonaje(personaje,self)

    def puedeAgregarPersonaje(self,personaje):
        personaje.juego = self
        self.laberinto.entrar(personaje)

    #Métodos Prototype

    def clonarLaberinto(self):
        return copy.deepcopy(self.prototipo)
    
    #Métodos Mediator

    def buscarBicho(self):
        pos=self.personaje.posicion
        for bicho in self.bichos:
            if bicho.posicion == pos:
                return bicho
        return None
    
    def buscarPersonaje(self,unBicho):
        if unBicho.posicion == self.personaje.posicion:
            return self.personaje
        else:
            return None
        
    def muereBicho(self):
        if self.todosMuertos() and self.ganaPersonaje:
            print(str(self.personaje)," gana el juego.")
            self.finJuego()

    def todosMuertos(self):
        for bicho in self.bichos:
            if bicho.estaVivo():
                return False
        return True
    
    def terminarBichos(self):
        for bicho in self.bichos:
            self.terminarHilo(bicho)
    
    def terminarHilo(self,unBicho):
        unBicho.heMuerto()

    def personajeMuere(self):
        print(str(self.personaje), " ha muerto. Ganan los bichos.")
        self.ganaPersonaje = False
        self.terminarBichos()
        self.finJuego()

    def finJuego(self):
        self.fase = Final()
        
    
    #Métodos iterator

    def abrirPuertas(self):
        funcl = lambda x: x.abrir() if x.esPuerta() else None
        self.laberinto.recorrer(funcl)

    def cerrarPuerta(self,hab1,hab2):
        funcl = lambda x: x.cerrar() if x.esPuerta() and (x.lado1.num is hab1 or x.lado2.num is hab1) and (x.lado1.num is hab2 or x.lado2.num is hab2) else None
        self.laberinto.recorrer(funcl)

    #Hilos
    def lanzarBichos(self):
        self.fase.lanzarBichos(self)

    def puedeLanzarBichos(self):
        for bicho in self.bichos:
            self.lanzarHilo(bicho)
    
    def agregarBicho(self,unBicho):
        unBicho.juego = self
        self.bichos.append(unBicho)
        unBicho.num = len(self.bichos)

    def lanzarHilo(self,bicho):
        hilo = threading.Thread(target=bicho.actua)
        hilo.start()
        self.agregarHilo(bicho,hilo)

    def agregarHilo(self,bicho,hilo):
        self.hilos[bicho.num]=hilo

    #Métodos para el Factory Method

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
    
    #Final de los métodos para el Factory Method

    #Fabricación de laberintos

    #Fabricación con AbstractFactory
    def laberinto2EntregAF(self,AF):
        self.laberinto = self.fabricarLaberinto()

        hab1 = AF.fabricarHabitacion(1)
        hab2 = AF.fabricarHabitacion(2)
        hab3 = AF.fabricarHabitacion(3)
        hab4 = AF.fabricarHabitacion(4)

        p1 = AF.fabricarPuerta()
        p2 = AF.fabricarPuerta()
        p3 = AF.fabricarPuerta()
        p4 = AF.fabricarPuerta()

        p1.lado1= hab1
        p1.lado2= hab2

        p2.lado1= hab2
        p2.lado2= hab4

        p3.lado1 = hab4
        p3.lado2 = hab3

        bomba1 = AF.fabricarBomba()
        bomba1.component = p3

        p4.lado1 = hab3
        p4.lado2 = hab1

        baul1 = AF.fabricarBaul(1,hab2)
        baul2 = AF.fabricarBaul(2,hab3)

        bomba2 = AF.fabricarBomba()

        baul1.agregarHijo(bomba2)

        espada = AF.fabricarEspada()

        baul2.agregarHijo(espada)

        fuego = AF.fabricarFuego()

        hab4.agregarHijo(fuego)
        hab2.agregarHijo(baul1)
        hab3.agregarHijo(baul2)

        hab1.ponerElementoEn(AF.fabricarEste(),p1)
        hab1.ponerElementoEn(AF.fabricarSur(),p4)

        hab2.ponerElementoEn(AF.fabricarOeste(),p1)
        hab2.ponerElementoEn(AF.fabricarSur(),p2)

        hab3.ponerElementoEn(AF.fabricarNorte(),p4)
        hab3.ponerElementoEn(AF.fabricarEste(),bomba1)

        hab4.ponerElementoEn(AF.fabricarNorte(),p2)
        hab4.ponerElementoEn(AF.fabricarOeste(),bomba1)

        self.laberinto.agregarHabitacion(hab1)
        self.laberinto.agregarHabitacion(hab2)
        self.laberinto.agregarHabitacion(hab3)
        self.laberinto.agregarHabitacion(hab4)

        b1= AF.fabricarBichoPerezoso(hab1)
        b2= AF.fabricarBichoAgresivo(hab2)
        self.agregarBicho(b1)
        self.agregarBicho(b2)

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

        bomba1 = self.fabricarBomba()
        bomba1.component = p3

        p4.lado1 = hab3
        p4.lado2 = hab1

        baul1 = self.fabricarBaul(1,hab2)
        baul2 = self.fabricarBaul(2,hab3)

        bomba2 = self.fabricarBomba()

        baul1.agregarHijo(bomba2)

        espada = self.fabricarEspada()

        baul2.agregarHijo(espada)

        fuego = self.fabricarFuego()

        hab4.agregarHijo(fuego)
        hab2.agregarHijo(baul1)
        hab3.agregarHijo(baul2)

        hab1.ponerElementoEn(self.fabricarEste(),p1)
        hab1.ponerElementoEn(self.fabricarSur(),p4)

        hab2.ponerElementoEn(self.fabricarOeste(),p1)
        hab2.ponerElementoEn(self.fabricarSur(),p2)

        hab3.ponerElementoEn(self.fabricarNorte(),p4)
        hab3.ponerElementoEn(self.fabricarEste(),bomba1)

        hab4.ponerElementoEn(self.fabricarNorte(),p2)
        hab4.ponerElementoEn(self.fabricarOeste(),bomba1)

        self.laberinto.agregarHabitacion(hab1)
        self.laberinto.agregarHabitacion(hab2)
        self.laberinto.agregarHabitacion(hab3)
        self.laberinto.agregarHabitacion(hab4)

        b1= self.fabricarBichoPerezoso(hab1)
        b2= self.fabricarBichoAgresivo(hab2)
        self.agregarBicho(b1)
        self.agregarBicho(b2)


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
