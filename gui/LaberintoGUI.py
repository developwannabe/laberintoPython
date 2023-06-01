from classes.builder.Director import Director
from classes.ente.Personaje import Personaje
import pygame
import time
class LaberintoGUI():
    
    def __init__(self):
        self.largoV = 1500
        self.anchoV = 900
        self.ancho = None
        self.alto = None
        self.ventana = None
        self.juego = None
        self.colorFondo = (255,255,255)
        self.fps = 1
        self.personaje = None
        self.personajeM = None
        self.capaPersonaje = None
        self.surface = None
        self.vidasP = None
        self.bichosP = {}
        self.bananasP = None
        self.armariosP = None
        self.rectAbrir = None
        self.rectCerrar = None
        self.textoAbrir = None
        self.botonAbrir = None
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
            monkeyIm=pygame.transform.scale(pygame.image.load("gui/img/monkey.png"),(self.anchoV/12,self.anchoV/12))
            colorFondo=(61,76,74)
            bichoA=pygame.transform.scale(pygame.image.load("gui/img/agresivo.png"),(self.anchoV/13,self.anchoV/13))
            bichoP=pygame.transform.scale(pygame.image.load("gui/img/perezoso.png"),(self.anchoV/13,self.anchoV/13))
            banana=pygame.transform.scale(pygame.image.load("gui/img/banana.png"),(self.anchoV/15,self.anchoV/15))
            armario=pygame.transform.scale(pygame.image.load("gui/img/closedwardrobe.png"),(self.anchoV/15,self.anchoV/15))
            running = True
            self.ventana.fill((0,0,0))
            self.capaLaberinto = pygame.Surface((self.anchoV,self.largoV))
            self.botonAbrir = pygame.Surface((200,50))
            self.capaLaberinto.fill(colorFondo)
            self.juego.laberinto.aceptar(self)
            self.mostrarPersonaje()
            self.mostrarVidasPersonaje()
            for bicho in self.juego.bichos:
                bicho.suscribirPosicion(self)
                bicho.suscribirVida(self)
                self.mostrarBicho(bicho)
            #self.mostrarLanzarBichos()
            while not self.juego.fase.esFinal() and running:
                keys = pygame.key.get_pressed()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False

                    if keys[pygame.K_UP]:
                        self.personaje.irAlNorte()
                    
                    if keys[pygame.K_DOWN]:
                        self.personaje.irAlSur()

                    if keys[pygame.K_RIGHT]:
                        self.personaje.irAlEste()

                    if keys[pygame.K_LEFT]:
                        self.personaje.irAlOeste()
                    
                    if keys[pygame.K_b]:
                        self.juego.lanzarBichos()

                    if keys[pygame.K_p]:
                        self.juego.abrirPuertas()

                    if keys[pygame.K_a]:
                        self.personaje.atacar()

                    if keys[pygame.K_c]:
                        com = self.personaje.obtenerComandos()
                        for i in com:
                            print(i)

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        pos = pygame.mouse.get_pos()
                        if self.rectAbrir.collidepoint(pos):
                            self.juego.abrirPuertas()
                        if self.rectCerrar.collidepoint(pos):
                            self.juego.cerrarPuertas()

                self.ventana.fill((0,0,0))
                self.ventana.blit(self.capaLaberinto,(0,0))
                self.ventana.blit(self.vidasP,(self.largoV-450,20))
                for bicho in self.bichosP.values():
                    if bicho[0] == '-Agresivo:':
                        self.ventana.blit(bichoA,bicho[1])
                    if bicho[0] == '-Perezoso:':
                        self.ventana.blit(bichoP,bicho[1])
                self.ventana.blit(monkeyIm, self.personajeM)
                self.ventana.blit(armario,self.armariosP)
                self.ventana.blit(banana,self.bananasP)
                self.mostrarAbrirPuertas()
                self.mostrarCerrarPuertas()
                pygame.display.update()

    def agregarPersonaje(self,nombre):
        personaje = Personaje()
        personaje.nick = nombre
        personaje.suscribirPosicion(self)
        personaje.suscribirVida(self)
        self.juego.agregarPersonaje(personaje)
        self.personaje = self.juego.personaje
    
    def mostrarAbrirPuertas(self):
        anch = 170 
        alt = 50
        color = (255, 255, 0)
        colorT = (0,0,0)
        self.rectAbrir = pygame.draw.rect(self.ventana, color, (900, 80, anch, alt))
        self.ventana.blit(pygame.font.Font(None, 32).render("Abrir Puertas", True, colorT),(910,90))
        
    def mostrarCerrarPuertas(self):
        anch = 180 
        alt = 50
        color = (255, 255, 0)
        colorT = (0,0,0)
        self.rectCerrar = pygame.draw.rect(self.ventana, color, (1080, 80, anch, alt))
        self.ventana.blit(pygame.font.Font(None, 32).render("Cerrar Puertas", True, colorT),(1090,90))
        
    def mostrarPersonaje(self):
        if self.personaje is None:
            return self
        unCont = self.juego.personaje.posicion
        an = unCont.getExtent()[0]
        al = unCont.getExtent()[1]
        a = unCont.getPunto()[0] + (an / 2) -30
        b = unCont.getPunto()[1] + (al/2) -50
        self.personajeM = (a,b)

    def mostrarBicho(self,bicho):
        self.bichosP[bicho.num] = ()
        unCont = bicho.posicion
        an = unCont.getExtent()[0]
        al = unCont.getExtent()[1]
        a = unCont.getPunto()[0] + (an / 2) +20
        b = unCont.getPunto()[1] + (al/2) +20
        self.bichosP[bicho.num]=(str(bicho.modo),(a,b))
    
    def mostrarBanana(self,banana):
        unCont = banana.padre
        an = unCont.getExtent()[0]
        al = unCont.getExtent()[1]
        a = unCont.getPunto()[0] + (an / 2) +20
        b = unCont.getPunto()[1] + (al/2) +20
        self.bananasP = (a,b)

    def vidasBicho(self,bicho):
        if bicho.vidas == 0:
            self.bichosP.pop(bicho.num)

    def mostrarVidasPersonaje(self):
        self.vidasP = pygame.font.Font(None,40).render("Vidas " +str(self.personaje) + ": " + str(self.personaje.vidas),True,(255,255,255))


    def visitarHabitacion(self,hab):
        self.dibujarContenedorRectangular(hab.forma,1)
    
    def visitarArmario(self,arm):
        self.mostrarArmario(arm)

    def mostrarArmario(self,arm):
        unCont = arm.padre
        a = unCont.getPunto()[0] -100
        b = unCont.getPunto()[1] -400
        arm.setExtent((0,0))
        arm.setPunto((a,b))
        self.armariosP = (a,b)
    
    def visitarBaul(self,baul):
        self.dibujarBaul(baul)

    def visitarBomba(self,bomba):
        pass#TODO:Dibujar Bomba

    def visitarBanana(self,banana):
        self.mostrarBanana(banana)

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
        pygame.draw.rect(self.capaLaberinto, (255, 0, 0), (unPunto[0], unPunto[1], an, al), 4)
