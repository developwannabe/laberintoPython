from classes.builder.Director import Director
from classes.ente.Personaje import Personaje
import pygame
import time
class LaberintoGUI():
    
    def __init__(self):
        self.largo = 1150
        self.ancho = 800
        self.ventana = None
        self.juego = None
        self.colorFondo = (255,255,255)
        self.fps = 1
        self.personaje = None
        pygame.init()
        self.ventana = pygame.display.set_mode((self.largo,self.ancho))
        pygame.display.set_caption("No banana, no monkey")
    
    def iniciarJuego(self,json,nombre):
        director = Director()
        director.procesar(json)
        self.juego = director.obtenerJuego()
        self.agregarPersonaje(nombre)
        self.mostrarLaberinto()
        #self.dibujarLaberinto()

    def mostrarLaberinto(self):
        pass#TODO:Esto
        #self.calcularPosicion()
        #self.normalizar()
        #self.calcularDimensiones()
        #self.asignarPuntosReales()

    def dibujarLaberinto(self):
        if self.juego is not None:
            self.juego.laberinto.aceptar(self)
            #self.mostrarVidasPersonaje()
            #self.mostrarAbrirPuertas()
            #self.mostrarLanzarBichos()
            #self.mostrarCerrarPuertas()
            #self.mostrarPersonaje()
            #self.mostrarBichos()

    def agregarPersonaje(self,nombre):
        personaje = Personaje()
        personaje.nick = nombre
        self.juego.agregarPersonaje(personaje)
        self.personaje = self.juego.personaje
        #TODO: Personaje addDependent
    
    def visitarHabitacion(self,hab):
        self.dibujarContenedorRectangular(hab.forma,1)
    
    def visitarArmario(self,arm):
        self.dibujarArmario(arm)
    
    def visitarBaul(self,baul):
        self.dibujarBaul(baul)

    def visitarBomba(self,bomba):
        pass#TODO:Dibujar Bomba

    def visitarFuego(self,fuego):
        pass#TODO:Dibujar Fuego

    def visitarEspada(self,espada):
        pass#TODO:Dibujar Espada

    def visitarPared(self,pared):
        pass

    def visitarPuerta(self,puerta):
        pass#TODO:Dibujar puerta

    def visitarTunel(self,tunel):
        pass#TODO:Dibujar tunel



    def ejecutar(self):
        monkeyIm = pygame.image.load("gui/img/monkey.png")
        monkeyIm = pygame.transform.scale(monkeyIm,(100,100))
        snakeIm = pygame.image.load("gui/img/snake.png")
        snakeIm = pygame.transform.scale(snakeIm,(100,100))
        openwardrobeIM = pygame.image.load("gui/img/openwardrobe.png")
        closedwardrobeIM = pygame.image.load("gui/img/closedwardrobe.png")
        openwardrobeIM = pygame.transform.scale(openwardrobeIM,(100,100))
        closedwardrobeIM = pygame.transform.scale(closedwardrobeIM,(100,100))
        bool = True
        running = True
        abierto = False
        coords = 100
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            time.sleep(2)
            self.ventana.fill(self.colorFondo)
            self.ventana.blit(monkeyIm, (coords,coords))
            self.ventana.blit(snakeIm, (100,100))
            pygame.draw.rect(self.ventana, (255, 0, 0), (200, 200, 200, 150), 10)
            if abierto:
                self.ventana.blit(openwardrobeIM, (400,400))
                abierto = False
            else:
                self.ventana.blit(closedwardrobeIM, (400,400))
                abierto = True
            pygame.display.update()
            if bool:
                coords += 50
                bool = False
            else:
                coords -= 50
                bool = True

    def terminar(self):
        pygame.quit()
