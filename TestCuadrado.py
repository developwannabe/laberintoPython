import unittest
import sys
from io import StringIO
from classes.builder.Director import Director
from classes.ente.Personaje import Personaje

class TestCuadrado(unittest.TestCase):

    def setUp(self):
        super().setUp()
        sys.stdout_save =sys.stdout
        sys.stdout = StringIO()#Deshabilitamos la salida para facilitar la lectura de los test
        director = Director()
        director.procesar('json/lab4hab4bichostunel.json')
        self.juego = director.obtenerJuego()
        personaje = Personaje()
        personaje.nick = "Prueba"
        self.juego.agregarPersonaje(personaje)
        sys.stdout=sys.stdout_save#Volvemos a habilitarla

    def testIniciales(self):
        self.assertEqual(self.juego is not None, True)
        self.assertEqual(self.juego.esJuego(),True)
        self.assertEqual(len(self.juego.laberinto.hijos),4)
        print("TEST INICIAL SUPERADO.\n")
    
    def testHabitaciones(self):
        #Habitación 1
        hab1 = self.juego.laberinto.hijos[0]
        self.assertEqual(hab1.esHabitacion(),True)
        self.assertEqual(hab1.num,1)
        self.assertEqual(len(hab1.hijos),4)
        self.assertEqual(hab1.forma.esCuadrado(),True)
        self.assertEqual(hab1.forma.norte.esPared(),True)
        self.assertEqual(hab1.forma.este.esPuerta(),True)
        self.assertEqual(hab1.forma.oeste.esPared(),True)
        self.assertEqual(hab1.forma.sur.esPuerta(),True)
        #Habitación 2
        hab2 = self.juego.laberinto.hijos[1]
        self.assertEqual(hab2.esHabitacion(),True)
        self.assertEqual(hab2.num,2)
        self.assertEqual(len(hab2.hijos),2)
        self.assertEqual(hab2.forma.esCuadrado(),True)
        self.assertEqual(hab2.forma.norte.esPuerta(),True)
        self.assertEqual(hab2.forma.este.esPuerta(),True)
        self.assertEqual(hab2.forma.oeste.esPared(),True)
        self.assertEqual(hab2.forma.sur.esPared(),True)
        #Habitación 3
        hab3 = self.juego.laberinto.hijos[2]
        self.assertEqual(hab3.esHabitacion(),True)
        self.assertEqual(hab3.num,3)
        self.assertEqual(len(hab3.hijos),2)
        self.assertEqual(hab3.forma.esCuadrado(),True)
        self.assertEqual(hab3.forma.norte.esPared(),True)
        self.assertEqual(hab3.forma.este.esPared(),True)
        self.assertEqual(hab3.forma.oeste.esPuerta(),True)
        self.assertEqual(hab3.forma.sur.esPuerta(),True)
        #Habitación 4
        hab4 = self.juego.laberinto.hijos[3]
        self.assertEqual(hab4.esHabitacion(),True)
        self.assertEqual(hab4.num,4)
        self.assertEqual(len(hab4.hijos),1)
        self.assertEqual(hab4.forma.esCuadrado(),True)
        self.assertEqual(hab4.forma.norte.esPuerta(),True)
        self.assertEqual(hab4.forma.este.esPared(),True)
        self.assertEqual(hab4.forma.oeste.esPuerta(),True)
        self.assertEqual(hab4.forma.sur.esPared(),True)

        print("ESTRUCTURA DE LAS HABITACIONES COMPROBADAS.\n")


    def testBichos(self):
        bichos = self.juego.bichos
        #Bicho 1
        b1 = bichos[0]
        self.assertEqual(b1.num,1)
        self.assertEqual(b1.modo.esAgresivo(),True)
        self.assertEqual(b1.posicion,self.juego.laberinto.hijos[0])
        self.assertEqual(b1.juego,self.juego)
        self.assertEqual(b1.estado.estaVivo(),True)
        #Bicho 2
        b2 = bichos[1]
        self.assertEqual(b2.num,2)
        self.assertEqual(b2.modo.esPerezoso(),True)
        self.assertEqual(b2.posicion,self.juego.laberinto.hijos[1])
        self.assertEqual(b2.juego,self.juego)
        self.assertEqual(b2.estado.estaVivo(),True)
        #Bicho 3
        b3 = bichos[2]
        self.assertEqual(b3.num,3)
        self.assertEqual(b3.modo.esAgresivo(),True)
        self.assertEqual(b3.posicion,self.juego.laberinto.hijos[2])
        self.assertEqual(b3.juego,self.juego)
        self.assertEqual(b3.estado.estaVivo(),True)
        #Bicho 4
        b4 = bichos[3]
        self.assertEqual(b4.num,4)
        self.assertEqual(b4.modo.esPerezoso(),True)
        self.assertEqual(b4.posicion,self.juego.laberinto.hijos[3])
        self.assertEqual(b4.juego,self.juego)
        self.assertEqual(b4.estado.estaVivo(),True)
        
        print("TEST DE LOS BICHOS SUPERADO.\n")

    def testPersonaje(self):
        personaje = self.juego.personaje
        self.assertEqual(personaje.nick,"Prueba")
        self.assertEqual(personaje.posicion,self.juego.obtenerHabitacion(1))
        self.assertEqual(personaje.estado.estaVivo(),True)
        self.assertEqual(personaje.juego, self.juego)
        self.assertEqual(personaje.bolsa.esBolsa(),True)
        self.assertEqual(len(personaje.bolsa.hijos),0)
        self.assertEqual(personaje.cuerpo.esCuerpo(),True)
        self.assertEqual(personaje.cuerpo.mDerecha is None, True)
        self.assertEqual(personaje.cuerpo.mIzquierda is None, True)
        print("TEST DEL PERSONAJE SUPERADO.")

unittest.main()