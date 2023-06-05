from classes.builder.Director import Director
from classes.ente.Personaje import Personaje
import pygame

class LaberintoGUI():
    
    def __init__(self):
        self.largoV = 1500
        self.anchoV = 900
        self.ancho = None
        self.alto = None
        self.ventana = None
        self.juego = None
        self.personaje = None
        self.personajeM = None
        self.vidasP = None
        self.bichosP = {}
        self.bananasP = {}
        self.armariosP = {}
        self.rectAbrirC = None
        self.rectCerrar = None
        self.botonAbrir = None
        self.rectIniciar = None
        self.rectBIn = None
        self.rectCuerpo = None
        self.rectCom = []
        self.puertasP = {}
        self.bolsa = {}
        self.espadasP = {}
        self.armaP = None
        self.escudosP = {}
        self.defensaP = None
        self.bombasP = {}
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
            espadaMa=pygame.transform.scale(pygame.image.load("gui/img/espadaMadera.png"),(self.anchoV/20,self.anchoV/20))
            espadaMe=pygame.transform.scale(pygame.image.load("gui/img/espadaHierro.png"),(self.anchoV/20,self.anchoV/20))
            espadaDi=pygame.transform.scale(pygame.image.load("gui/img/espadaDiamante.png"),(self.anchoV/20,self.anchoV/20))
            bombaA=pygame.transform.scale(pygame.image.load("gui/img/bombaA.png"),(self.anchoV/20,self.anchoV/20))
            bombaI=pygame.transform.scale(pygame.image.load("gui/img/bombaI.png"),(self.anchoV/20,self.anchoV/20))
            escudo=pygame.transform.scale(pygame.image.load("gui/img/escudo.png"),(self.anchoV/26,self.anchoV/26))
            armarioC=pygame.transform.scale(pygame.image.load("gui/img/closedwardrobe.png"),(self.anchoV/12,self.anchoV/12))
            armarioA=pygame.transform.scale(pygame.image.load("gui/img/openwardrobe.png"),(self.anchoV/12,self.anchoV/12))
            mostrarInventario = False
            mostrarCuerpo = False
            running = True
            self.ventana.fill((0,0,0))
            self.capaLaberinto = pygame.Surface((self.anchoV,self.largoV))
            self.botonAbrir = pygame.Surface((200,50))
            self.capaLaberinto.fill(colorFondo)
            self.juego.laberinto.aceptar(self)
            self.mostrarPersonaje()
            self.mostrarVidasPersonaje()
            self.personaje.bolsa.observarBolsa(self)
            self.personaje.cuerpo.agregarObservadoresCuerpo(self)
            self.mostrarBolsa(self.personaje.bolsa)
            for bicho in self.juego.bichos:
                print(bicho.vidas)
                bicho.suscribirPosicion(self)
                bicho.suscribirVida(self)
                self.mostrarBicho(bicho)
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

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        pos = pygame.mouse.get_pos()
                        if self.rectAbrir.collidepoint(pos):
                            self.juego.abrirPuertas()
                        if self.rectCerrar.collidepoint(pos):
                            self.juego.cerrarPuertas()
                        if self.rectIniciar.collidepoint(pos):
                            self.juego.lanzarBichos()
                        if self.rectBIn.collidepoint(pos):
                            mostrarInventario = not mostrarInventario
                            mostrarCuerpo = False
                        if self.rectAbrirC.collidepoint(pos):
                            mostrarCuerpo = not mostrarCuerpo
                            mostrarInventario = False
                        for com in self.rectCom:
                            if com[0].collidepoint(pos):
                                com[1].ejecutar(self.personaje)

                self.ventana.fill((0,0,0))
                self.ventana.blit(self.capaLaberinto,(0,0))
                for puerta in self.puertasP.values():
                    if puerta[1] == "abierta":
                        pygame.draw.rect(self.ventana, colorFondo, (puerta[0][0]-10, puerta[0][1]-10, 60, 60))
                self.ventana.blit(self.vidasP,(self.largoV-450,20))
                for bicho in self.bichosP.values():
                    if bicho[0] == '-Agresivo:':
                        self.ventana.blit(bichoA,bicho[1])
                    if bicho[0] == '-Perezoso:':
                        self.ventana.blit(bichoP,bicho[1])
                for armario in self.armariosP.values():
                    if armario[0] == 'abierto':
                        self.ventana.blit(armarioA,armario[1])
                for obj in self.bolsa.values():
                    if obj[0] == "Banana":
                        self.ventana.blit(banana,obj[1])
                    if obj[0] == "Espada":
                        if obj[1] == 'madera':
                            self.ventana.blit(espadaMa,obj[2])
                        if obj[1] == 'metal':
                            self.ventana.blit(espadaMe,obj[2])
                        if obj[1] == 'diamante':
                            self.ventana.blit(espadaDi,obj[2])
                    if obj[0] == "Escudo":
                        self.ventana.blit(escudo,obj[1])
                for bomba in self.bombasP.values():
                    if bomba[0] == "Activa":
                        self.ventana.blit(bombaA,bomba[1])
                    if bomba[0] == "Inactiva":
                        self.ventana.blit(bombaI,bomba[1])
                for espada in self.espadasP.values():
                    if espada[0] == 'madera':
                        self.ventana.blit(espadaMa,espada[1])
                    if espada[0] == 'metal':
                        self.ventana.blit(espadaMe,espada[1])
                    if espada[0] == 'diamante':
                        self.ventana.blit(espadaDi,espada[1])
                for bananas in self.bananasP.values():
                    self.ventana.blit(banana,bananas)
                for escudos in self.escudosP.values():
                    self.ventana.blit(escudo,escudos)
                self.mostrarAbrirPuertas()
                self.mostrarCerrarPuertas()
                self.mostrarIniciarJuego()
                if mostrarInventario:
                    self.mostrarComandos(self.personaje.bolsa)
                    self.mostrarBInventario("Cerrar")
                    self.mostrarAbrirCuerpo("Abrir")
                elif mostrarCuerpo:
                    self.mostrarBInventario("Abrir")
                    self.mostrarAbrirCuerpo("Cerrar")
                    self.mostrarComandos(self.personaje.cuerpo)
                else:
                    self.mostrarComandos()
                    self.mostrarBInventario("Abrir")
                    self.mostrarAbrirCuerpo("Abrir")
                    
                if self.armaP is not None:
                    if self.armaP[0] == "Espada":
                        if self.armaP[1] == 'Madera':
                            self.ventana.blit(espadaMa,self.armaP[2])
                        if self.armaP[1] == 'Metal':
                            self.ventana.blit(espadaMe,self.armaP[2])
                        if self.armaP[1] == 'Diamante':
                            self.ventana.blit(espadaDi,self.armaP[2])
                self.ventana.blit(monkeyIm, self.personajeM)
                if self.defensaP is not None:
                    if self.defensaP[0] == "Escudo":
                        self.ventana.blit(escudo,self.defensaP[1])
                for armario in self.armariosP.values():
                    if armario[0] == 'cerrado':
                        self.ventana.blit(armarioC,armario[1])
                pygame.display.update()

            self.juego.terminarBichos()#Por si se cierra la ventana

    def agregarPersonaje(self,nombre):
        personaje = Personaje()
        personaje.nick = nombre
        personaje.suscribirPosicion(self)
        personaje.suscribirVida(self)
        self.juego.agregarPersonaje(personaje)
        self.personaje = self.juego.personaje
    
    def mostrarAbrirPuertas(self):
        self.rectAbrir = pygame.draw.rect(self.ventana, (255, 255, 0), (910, 80, 170, 50))
        self.ventana.blit(pygame.font.Font(None, 32).render("Abrir Puertas", True, (0,0,0)),(920,90))
        
    def mostrarCerrarPuertas(self):
        self.rectCerrar = pygame.draw.rect(self.ventana, (255, 255, 0), (1090, 80, 180, 50))
        self.ventana.blit(pygame.font.Font(None, 32).render("Cerrar Puertas", True, (0,0,0)),(1100,90))

    def mostrarIniciarJuego(self):
        self.rectIniciar = pygame.draw.rect(self.ventana, (255, 255, 0), (1280, 80, 160, 50))
        self.ventana.blit(pygame.font.Font(None, 32).render("Iniciar Juego", True, (0,0,0)),(1290,90))

    def mostrarBInventario(self,texto):
        self.rectBIn = pygame.draw.rect(self.ventana, (255, 255, 0), (1040, 750, 80, 50))
        self.ventana.blit(pygame.font.Font(None, 32).render("Inventario", True, (255,255,255)),(910,760))
        self.ventana.blit(pygame.font.Font(None, 32).render(texto, True, (0,0,0)),(1050,760))
    
    def mostrarAbrirCuerpo(self,texto):
        self.rectAbrirC = pygame.draw.rect(self.ventana, (255, 255, 0), (1130, 750, 160, 50))
        self.ventana.blit(pygame.font.Font(None, 32).render(texto+" Cuerpo", True, (0,0,0)),(1140,760))
        
    def mostrarComandos(self,cont=None):
        i = 0
        a = 910
        b = 150
        self.rectCom = []
        if cont is None:
            obtenerDe = self.personaje
        else:
            obtenerDe = cont
        for com in obtenerDe.obtenerComandos(self.personaje):
            ex = len(str(com))*12
            self.rectCom.append((pygame.draw.rect(self.ventana, (255, 255, 0), (a, b, ex, 50)),com))
            self.ventana.blit(pygame.font.Font(None, 32).render(str(com), True, (0,0,0)),(a + 10,b + 10))
            b += 60
            i += 1

    def mostrarPersonaje(self):
        if self.personaje is None:
            return self
        unCont = self.juego.personaje.posicion
        an = unCont.getExtent()[0]
        al = unCont.getExtent()[1]
        a = unCont.getPunto()[0] + (an / 2) -30
        b = unCont.getPunto()[1] + (al/2) -50
        if unCont.esArmario():
            a += 30
            b+=50
        self.personajeM = (a,b)
        self.mostrarCuerpo()

    def mostrarCuerpo(self):
        self.mostrarArma()
        self.mostrarDefensa()

    def mostrarArma(self):
        self.armaP = None
        if (arma:=self.personaje.cuerpo.obtenermDerecha()) is not None:
            a = self.personajeM[0] + 30
            b = self.personajeM[1] + 20
            if arma.esEspada():
                self.armaP = ("Espada",str(arma.material),(a,b))
    
    def mostrarDefensa(self):
        self.defensaP = None
        if (defensa:=self.personaje.cuerpo.obtenermIzquierda()) is not None:
            a = self.personajeM[0] + 10
            b = self.personajeM[1] + 35
            if defensa.esEscudo():
                self.defensaP = ("Escudo",(a,b))

    def mostrarBicho(self,bicho):
        self.bichosP[bicho.num] = ()
        unCont = bicho.posicion
        an = unCont.getExtent()[0]
        al = unCont.getExtent()[1]
        a = unCont.getPunto()[0] + (an / 2) +20
        b = unCont.getPunto()[1] + (al/2) +20
        self.bichosP[bicho.num]=(str(bicho.modo),(a,b))
    
    def mostrarBanana(self,banana):
        self.bananasP[str(banana)] = ((-100,-100))
        if banana.padre.esHabitacion():
            unCont = banana.padre
            an = unCont.getExtent()[0]
            al = unCont.getExtent()[1]
            a = unCont.getPunto()[0] + an - 100
            b = unCont.getPunto()[1] + an - 100
            self.bananasP[str(banana)]=((a,b))

    def vidasBicho(self,bicho):
        if bicho.vidas == 0:
            self.bichosP.pop(bicho.num)

    def mostrarVidasPersonaje(self):
        self.vidasP = pygame.font.Font(None,40).render("Vidas " +str(self.personaje) + ": " + str(self.personaje.vidas),True,(255,255,255))


    def visitarHabitacion(self,hab):
        self.dibujarContenedorRectangular(hab.forma,1)
    
    def visitarArmario(self,arm):
        arm.suscribirAbierto(self)
        self.mostrarArmario(arm)

    def mostrarArmario(self,arm):
        self.armariosP[arm.num] = ()
        unCont = arm.padre
        a = unCont.getPunto()[0]  + 20
        b = unCont.getPunto()[1] + 10
        arm.setExtent((0,0))
        arm.setPunto((a,b))
        if arm.estaAbierto():
            self.armariosP[arm.num] = ("abierto",(a,b))
        else:
            self.armariosP[arm.num] = ("cerrado",(a,b))
    
    def mostrarPuerta(self,puerta):
        self.puertasP[str(puerta)] = ()
        if puerta.lado1.getPunto()[0] > puerta.lado2.getPunto()[0]:
            a = puerta.lado1.getPunto() [0]
            b = puerta.lado1.getPunto()[1] + puerta.lado1.getExtent()[1]/2
        elif puerta.lado2.getPunto()[0] > puerta.lado1.getPunto()[0]:
            a = puerta.lado2.getPunto() [0] 
            b = puerta.lado2.getPunto()[1] + puerta.lado2.getExtent()[1]/2
        else:
            if puerta.lado1.getPunto()[1] > puerta.lado2.getPunto()[1]:
                a = puerta.lado1.getPunto()[0] + puerta.lado1.getExtent()[0] / 2
                b = puerta.lado1.getPunto() [1]
            else:
                a = puerta.lado2.getPunto()[0] + puerta.lado2.getExtent()[0]/2
                b = puerta.lado2.getPunto() [1]
        if puerta.estaAbierta():
            self.puertasP[str(puerta)] = ((a,b),"abierta")
        else:
            self.puertasP[str(puerta)] = ((a,b),"cerrada")
    
    def mostrarBolsa(self,bolsa):
        self.bolsa = {}
        a = 910
        b = 800
        for obj in bolsa.hijos:
            if obj.esBanana():
                self.bolsa [str(obj)] = ("Banana",(a,b))
            if obj.esEspada():
                if obj.material.esMadera():
                    self.bolsa [str(obj)] = ("Espada","madera",(a,b))
                if obj.material.esMetal():
                    self.bolsa [str(obj)] = ("Espada","metal",(a,b))
                if obj.material.esDiamante():
                    self.bolsa [str(obj)] = ("Espada","diamante",(a,b))
            if obj.esEscudo():
                self.bolsa [str(obj)] = ("Escudo",(a,b))
            a += 70

    def mostrarObjeto(self,obj):
        if obj.esBanana():
            self.mostrarBanana(obj)
        if obj.esEspada():
            self.mostrarEspada(obj)
        if obj.esEscudo():
            self.mostrarEscudo(obj)

    def visitarEscudo(self,escudo):
        escudo.agregarObservadorPosicion(self)
        self.mostrarEscudo(escudo)

    def visitarBomba(self,bomba):
        bomba.agregarObservadoresActiva(self)
        self.mostrarBomba(bomba)

    def visitarBanana(self,banana):
        banana.agregarObservadorPosicion(self)
        if banana.padre.esBolsa():
            self.mostrarBanana(banana)

    def visitarEspada(self,espada):
        espada.agregarObservadorPosicion(self)
        self.mostrarEspada(espada)
    
    def mostrarEspada(self,espada):
        self.espadasP[str(espada)] = ((-100,-100))
        if espada.padre.esHabitacion():
            if espada.material.esMadera():
                a = espada.padre.getPunto()[0]  + 20
                b = espada.padre.getPunto()[1] + espada.padre.getExtent()[0] -100
                self.espadasP[str(espada)] = ("madera",(a,b))
            if espada.material.esMetal():
                a = espada.padre.getPunto()[0]  + 120
                b = espada.padre.getPunto()[1] + espada.padre.getExtent()[0] -100
                self.espadasP[str(espada)] = ("metal",(a,b))
            if espada.material.esDiamante():
                a = espada.padre.getPunto()[0]  + 220
                b = espada.padre.getPunto()[1] + espada.padre.getExtent()[0] -100
                self.espadasP[str(espada)] = ("diamante",(a,b))
    
    def mostrarEscudo(self,escudo):
        self.escudosP[str(escudo)] = ((-100,-100))
        if escudo.padre.esHabitacion():
            a = escudo.padre.getPunto()[0] + 40
            b = escudo.padre.getPunto()[1] + escudo.padre.getExtent()[0] -300
            self.escudosP[str(escudo)] = (a,b)

    def mostrarBomba(self,bomba):
        self.bombasP[str(bomba)] = ("",(-100,-100))
        unCont = bomba.padre
        an = unCont.getExtent()[0]
        al = unCont.getExtent()[1]
        a = unCont.getPunto()[0] + an - 200
        b = unCont.getPunto()[1] + an - 100
        if bomba.activa:
            self.bombasP[str(bomba)]=("Activa",(a,b))
        else:
            self.bombasP[str(bomba)]=("Inactiva",(a,b))

    def visitarPared(self,pared):
        pass # Son dibujadas junto al contenedor rectangular

    def visitarPuerta(self,puerta):
        if puerta.lado1.esHabitacion() and puerta.lado2.esHabitacion():
            puerta.suscribirAbierto(self)
            self.mostrarPuerta(puerta)

    def visitarTunel(self,tunel):
        pass#No se dibujará, solo será jugado por consola.

    def dibujarContenedorRectangular(self,forma,escala):
        unPunto = forma.punto
        an = forma.extent[0] / escala
        al = forma.extent[1] / escala
        pygame.draw.rect(self.capaLaberinto, (255, 0, 0), (unPunto[0], unPunto[1], an, al), 4)