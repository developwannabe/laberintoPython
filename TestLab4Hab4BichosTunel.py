import unittest
import sys
from io import StringIO
from classes.builder.Director import Director
from classes.ente.Personaje import Personaje

class TestLab4Hab4BichosTunel(unittest.TestCase):

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
        self.assertEqual(len(hab1.hijos),3)
        self.assertEqual(hab1.forma.esCuadrado(),True)
        self.assertEqual(hab1.forma.norte.esPared(),True)
        self.assertEqual(hab1.forma.este.esPuerta(),True)
        self.assertEqual(hab1.forma.oeste.esPared(),True)
        self.assertEqual(hab1.forma.sur.esPuerta(),True)
        #Habitación 2
        hab2 = self.juego.laberinto.hijos[1]
        self.assertEqual(hab2.esHabitacion(),True)
        self.assertEqual(hab2.num,2)
        self.assertEqual(len(hab2.hijos),1)
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
        self.assertEqual(len(hab4.hijos),2)
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
        print("TEST DEL PERSONAJE SUPERADO.\n")

    def testPuertas(self):
        #Puerta 1
        p1 = self.juego.obtenerHabitacion(1).forma.sur
        self.assertEqual(p1.esPuerta(),True)
        self.assertEqual(p1.lado1,self.juego.obtenerHabitacion(1))
        self.assertEqual(p1.lado2,self.juego.obtenerHabitacion(2))
        self.assertEqual(p1.comandos[0].esAbrir(),True)
        self.assertEqual(p1.comandos[0].receptor,p1)
        #Puerta 2
        p2 = self.juego.obtenerHabitacion(2).forma.este
        self.assertEqual(p2.esPuerta(),True)
        self.assertEqual(p2.lado1,self.juego.obtenerHabitacion(2))
        self.assertEqual(p2.lado2,self.juego.obtenerHabitacion(4))
        self.assertEqual(p2.comandos[0].esAbrir(),True)
        self.assertEqual(p2.comandos[0].receptor,p2)
        #Puerta 3
        p3 = self.juego.obtenerHabitacion(4).forma.norte
        self.assertEqual(p3.esPuerta(),True)
        self.assertEqual(p3.lado1,self.juego.obtenerHabitacion(4))
        self.assertEqual(p3.lado2,self.juego.obtenerHabitacion(3))
        self.assertEqual(p3.comandos[0].esAbrir(),True)
        self.assertEqual(p3.comandos[0].receptor,p3)
        #Puerta 4
        p4 = self.juego.obtenerHabitacion(3).forma.oeste
        self.assertEqual(p4.esPuerta(),True)
        self.assertEqual(p4.lado1,self.juego.obtenerHabitacion(3))
        self.assertEqual(p4.lado2,self.juego.obtenerHabitacion(1))
        self.assertEqual(p4.comandos[0].esAbrir(),True)
        self.assertEqual(p4.comandos[0].receptor,p4)
        print("TEST DE PUERTAS SUPERADO.\n")

    def testArmarios(self):
        #Armario 1
        arm1 = None
        pad1 = None
        for hijo in (pad1:=self.juego.obtenerHabitacion(1)).hijos:
            if hijo.esArmario():
                arm1 = hijo
        self.assertEqual(arm1.num,1)
        self.assertEqual(arm1.padre,pad1)
        self.assertEqual(len(arm1.hijos),1)
        self.assertEqual(arm1.forma.esCuadrado(),True)
        self.assertEqual(arm1.forma.norte.esPared(),True)
        self.assertEqual(arm1.forma.este.esPared(),True)
        self.assertEqual(arm1.forma.oeste.esPared(),True)
        self.assertEqual((p1:=arm1.forma.sur).esPuerta(),True)
        self.assertEqual(p1.estaAbierta(),False)
        self.assertEqual(p1.comandos[0].esAbrir(),True)
        self.assertEqual(p1.comandos[0].receptor,p1)
        #Armario 2
        arm2 = None
        pad2 = None
        for hijo in (pad2:=self.juego.obtenerHabitacion(4)).hijos:
            if hijo.esArmario():
                arm2 = hijo
        self.assertEqual(arm2.num,2)
        self.assertEqual(arm2.padre,pad2)
        self.assertEqual(len(arm2.hijos),0)
        self.assertEqual(arm2.forma.esCuadrado(),True)
        self.assertEqual(arm2.forma.norte.esPared(),True)
        self.assertEqual(arm2.forma.este.esPared(),True)
        self.assertEqual(arm2.forma.oeste.esPared(),True)
        self.assertEqual((p2:=arm1.forma.sur).esPuerta(),True)
        self.assertEqual(p2.estaAbierta(),False)
        self.assertEqual(p2.comandos[0].esAbrir(),True)
        self.assertEqual(p2.comandos[0].receptor,p2)

    def testTuneles(self):
        tunel = None
        padre = None
        for hijo in (padre:=self.juego.obtenerHabitacion(3)).hijos:
            if hijo.esTunel():
                tunel = hijo
        self.assertEqual(tunel.padre,padre)
        self.assertEqual(tunel.laberinto,None)
        print("TEST DE TÚNELES SUPERADO.\n")
    
    def testbombas(self):
        #Bomba 1
        bomba1 = None
        pad1 = None
        for hijo in (pad1:=self.juego.obtenerHabitacion(1)).hijos:
            if hijo.esBomba():
                bomba1 = hijo
        self.assertEqual(bomba1.num,1)
        self.assertEqual(bomba1.activa,True)
        self.assertEqual(bomba1.padre,pad1)
        self.assertEqual(bomba1.comandos[0].esEntrar(),True)
        self.assertEqual(bomba1.comandos[0].receptor,bomba1)
        #Bomba 2
        bomba2 = None
        pad2 = None
        for hijo in (pad2:=self.juego.obtenerHabitacion(4)).hijos:
            if hijo.esBomba():
                bomba2 = hijo
        self.assertEqual(bomba2.num,2)
        self.assertEqual(bomba2.activa,True)
        self.assertEqual(bomba2.padre,pad2)
        self.assertEqual(bomba2.comandos[0].esEntrar(),True)
        self.assertEqual(bomba2.comandos[0].receptor,bomba2)
        print("TEST DE BOMBAS SUPERADO.")

    def testObjetos(self):
        #Objetos Habitación 1
        hab1 = self.juego.obtenerHabitacion(1)
        #Banana 1
        arm1 = hab1.hijos[0]
        self.assertEqual((banana1:=arm1.hijos[0]).esBanana(),True)
        self.assertEqual((com1:=banana1.comandos[0]).esCoger(),True)
        self.assertEqual(com1.receptor,banana1)
        #Escudo
        self.assertEqual((escudo:=hab1.hijos[1]).esEscudo(),True)
        self.assertEqual(escudo.num,1)
        self.assertEqual(escudo.comandos[0].esCoger(),True)
        self.assertEqual(escudo.comandos[0].receptor,escudo)
        #Objetos Habitación 2
        hab2 = self.juego.obtenerHabitacion(2)
        #Espada metal
        self.assertEqual((espada1:=hab2.hijos[0]).esEspada(),True)
        self.assertEqual(espada1.num,1)
        self.assertEqual(espada1.comandos[0].esCoger(),True)
        self.assertEqual(espada1.comandos[0].receptor,espada1)
        self.assertEqual(espada1.material.esMetal(),True)
        #Objetos Habitación 3
        hab3 = self.juego.obtenerHabitacion(3)
        #Espada metal
        self.assertEqual((espada2:=hab3.hijos[0]).esEspada(),True)
        self.assertEqual(espada2.num,1)
        self.assertEqual(espada2.comandos[0].esCoger(),True)
        self.assertEqual(espada2.comandos[0].receptor,espada2)
        self.assertEqual(espada2.material.esDiamante(),True)
        print("TEST DE OBJETOS SUPERADO.\n")

    def testFuncionalidades(self):
        #Abrir puertas
        self.juego.abrirPuertas()
        p1 = self.juego.obtenerHabitacion(1).forma.sur
        p2 = self.juego.obtenerHabitacion(2).forma.este
        p3 = self.juego.obtenerHabitacion(4).forma.norte
        p4 = self.juego.obtenerHabitacion(3).forma.oeste
        self.assertEqual(len(p1.comandos),2)
        self.assertEqual(p1.esPuerta(),True)
        self.assertEqual(p1.comandos[0].esEntrar(),True)
        self.assertEqual(p1.comandos[0].receptor,p1)
        self.assertEqual(p1.comandos[1].esCerrar(),True)
        self.assertEqual(p1.comandos[1].receptor,p1)
        self.assertEqual(len(p2.comandos),2)
        self.assertEqual(p2.esPuerta(),True)
        self.assertEqual(p2.comandos[0].esEntrar(),True)
        self.assertEqual(p2.comandos[0].receptor,p2)
        self.assertEqual(p2.comandos[1].esCerrar(),True)
        self.assertEqual(p2.comandos[1].receptor,p2)
        self.assertEqual(len(p3.comandos),2)
        self.assertEqual(p3.esPuerta(),True)
        self.assertEqual(p3.comandos[0].esEntrar(),True)
        self.assertEqual(p3.comandos[0].receptor,p3)
        self.assertEqual(p3.comandos[1].esCerrar(),True)
        self.assertEqual(p3.comandos[1].receptor,p3)
        self.assertEqual(len(p4.comandos),2)
        self.assertEqual(p4.esPuerta(),True)
        self.assertEqual(p4.comandos[0].esEntrar(),True)
        self.assertEqual(p4.comandos[0].receptor,p4)
        self.assertEqual(p4.comandos[1].esCerrar(),True)
        self.assertEqual(p4.comandos[1].receptor,p4)
        #Cerrar puertas
        self.juego.cerrarPuertas()
        self.assertEqual(len(p1.comandos),1)
        self.assertEqual(p1.esPuerta(),True)
        self.assertEqual(p1.comandos[0].esAbrir(),True)
        self.assertEqual(p1.comandos[0].receptor,p1)
        self.assertEqual(len(p2.comandos),1)
        self.assertEqual(p2.esPuerta(),True)
        self.assertEqual(p2.comandos[0].esAbrir(),True)
        self.assertEqual(p2.comandos[0].receptor,p2)
        self.assertEqual(len(p3.comandos),1)
        self.assertEqual(p3.esPuerta(),True)
        self.assertEqual(p3.comandos[0].esAbrir(),True)
        self.assertEqual(p3.comandos[0].receptor,p3)
        self.assertEqual(len(p4.comandos),1)
        self.assertEqual(p4.esPuerta(),True)
        self.assertEqual(p4.comandos[0].esAbrir(),True)
        self.assertEqual(p4.comandos[0].receptor,p4)
        #Comandos personaje posición Habitación 1
        personaje = self.juego.personaje
        self.assertEqual(len(coms:=personaje.obtenerComandos(personaje)),5)
        coms[0].ejecutar(personaje)#Abrir armario 1
        coms= personaje.obtenerComandos(personaje)
        coms[0].ejecutar(personaje)#Entrar en armario 1 
        coms= personaje.obtenerComandos(personaje)
        coms[0].ejecutar(personaje)#Coger Banana
        self.assertEqual(len(bolsa:=personaje.bolsa.hijos),1)
        self.assertEqual((banana:=bolsa[0]).esBanana(),True)
        self.assertEqual(len((coms:=banana.obtenerComandos(personaje))),2)
        coms[0].ejecutar(personaje)#Soltar banana
        self.assertEqual(banana.padre,personaje.posicion)
        coms= personaje.obtenerComandos(personaje)
        coms[0].ejecutar(personaje)#Volver a coger banana
        print(coms)
        coms= personaje.bolsa.hijos[0].obtenerComandos(personaje)
        vida = personaje.vidas
        coms[1].ejecutar(personaje)#Comer banana
        self.assertEqual(personaje.vidas, vida + banana.vida) #Se le sumará la vida de la banana
        coms= personaje.obtenerComandos(personaje)
        coms[0].ejecutar(personaje)#Irse del armario
        #TODO:Coger escudo
        #TODO:Equipar escudo
        #TODO:Coger espada
        #TODO:Equipar espada
        #TODO:Coger otra espada
        #TODO:Equipar otra espada
        #TODO:Atacar bicho con espada
        #TODO:Atacar bicho sin espada
        
unittest.main()