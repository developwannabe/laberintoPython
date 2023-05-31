from classes.builder.Director import Director
from classes.ente.Personaje import Personaje
import pygame
import time
class LaberintoGUI():
    
    def __init__(self):
        self.largoV = 1150
        self.anchoV = 800
        self.ancho = None
        self.alto = None
        self.ventana = None
        self.juego = None
        self.colorFondo = (255,255,255)
        self.fps = 1
        self.personaje = None
        self.surface = None
        pygame.init()
        self.ventana = pygame.display.set_mode((self.largoV,self.anchoV))
        pygame.display.set_caption("No banana, no monkey")
    
    def iniciarJuego(self,json,nombre):
        director = Director()
        director.procesar(json)
        self.juego = director.obtenerJuego()
        self.agregarPersonaje(nombre)
        self.mostrarLaberinto()
        self.dibujarLaberinto()

    def mostrarLaberinto(self):
        self.calcularPosicion()
        self.normalizar()
        self.calcularDimensiones()
        self.asignarPuntosReales()

    def calcularPosicion(self):
        h1= self.juego.obtenerHabitacion(1)
        h1.setPunto((0,0))
        h1.calcularPosicion()

    def normalizar(self):
        minX = 0
        minY = 0
        for hijo in self.juego.laberinto.hijos:
            if hijo.getPunto()[0] < minX:
                minX = hijo.getPunto()[0]
            if hijo.getPunto()[1] < minY:
                minY = hijo.getPunto()[1]
        
        for hijo in self.juego.laberinto.hijos:
            unPunto = hijo.getPunto()
            hijo.setPunto((unPunto[0] + abs(minX),unPunto[1]+abs(minY)))

    def calcularDimensiones(self):
        maxX = 0
        maxY = 0
        for hijo in self.juego.laberinto.hijos:
            if hijo.getPunto()[0] > maxX:
                maxX = hijo.getPunto()[0]
            if hijo.getPunto()[1] > maxY:
                maxY = hijo.getPunto()[1]
        maxX += 1
        maxY += 1
        self.ancho = int(self.anchoV/maxX) * 0.95
        self.alto = int(self.anchoV/maxY) * 0.95

    def asignarPuntosReales(self):
        x = 0
        y = 0
        origen = (10,10)
        for hijo in self.juego.laberinto.hijos:
            x = origen[0] + (hijo.getPunto()[0] * self.ancho)
            y = origen[1] + (hijo.getPunto()[1] * self.alto)
            hijo.setExtent((self.ancho,self.alto))
            hijo.setPunto((x,y))

    
    def dibujarLaberinto(self):
        if self.juego is not None:
            running = True
            self.ventana.fill((255,255,255))
            self.surface = pygame.Surface((self.anchoV,self.largoV))
            self.surface.fill((255,255,255))
            self.juego.laberinto.aceptar(self)
            #self.mostrarVidasPersonaje()
            #self.mostrarAbrirPuertas()
            #self.mostrarLanzarBichos()
            #self.mostrarCerrarPuertas()
            #self.mostrarPersonaje()
            #self.mostrarBichos()
            while running:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                self.ventana.fill((255,255,255))
                self.ventana.blit(self.surface,(0,0))
                pygame.display.update()

    def agregarPersonaje(self,nombre):
        personaje = Personaje()
        personaje.nick = nombre
        self.juego.agregarPersonaje(personaje)
        self.personaje = self.juego.personaje
        #TODO: Personaje addDependent
    
    def visitarHabitacion(self,hab):
        self.dibujarContenedorRectangular(hab.forma,1)
    
    def visitarArmario(self,arm):
        pass
        #TODO:self.dibujarArmario(arm)
    
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

    def dibujarContenedorRectangular(self,forma,escala):
        unPunto = forma.punto
        an = forma.extent[0] / escala
        al = forma.extent[1] / escala
        pygame.draw.rect(self.surface, (0, 0, 0), (unPunto[0], unPunto[1], an, al), 2)

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
            self.ventana.blit(monkeyIm, (coords,coords))
            self.ventana.blit(snakeIm, (100,100))
            if abierto:
                self.ventana.blit(openwardrobeIM, (400,400))
                abierto = False
            else:
                #self.ventana.blit(closedwardrobeIM, (400,400))
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
