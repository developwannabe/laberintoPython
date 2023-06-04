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
from classes.elementoMapa.objeto.Espada import Espada
from classes.ente.Bicho import Bicho
from classes.ente.Personaje import Personaje
from classes.modo.Agresivo import Agresivo
from classes.modo.Perezoso import Perezoso
from classes.juego.Juego import Juego
from classes.elementoMapa.contenedor.Armario import Armario
from classes.forma.Cuadrado import Cuadrado
from classes.elementoMapa.hoja.Tunel import Tunel
from classes.comando.Abrir import Abrir
from classes.elementoMapa.objeto.Banana import Banana
from classes.comando.Coger import Coger
from classes.material.Madera import Madera
from classes.material.Metal import Metal
from classes.material.Diamante import Diamante

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
    
    def fabricarBanana(self,num):
        banana = Banana()
        banana.num = num
        com = self.fabricarCoger()
        com.receptor=banana
        banana.agregarComando(com)
        return banana
    
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
        com = Abrir()
        com.receptor=p1
        p1.agregarComando(com)


        p1.lado1=self
        p1.lado2=padre

        armario.forma= self.fabricarForma()
        p1.lado1= armario
        p1.lado2 = padre

        armario.agregarOrientacion(self.fabricarNorte())
        armario.agregarOrientacion(self.fabricarEste())
        armario.agregarOrientacion(self.fabricarOeste())
        armario.agregarOrientacion(self.fabricarSur())

        armario.ponerElementoEn(self.fabricarNorte(),self.fabricarPared())
        armario.ponerElementoEn(self.fabricarEste(),self.fabricarPared())
        armario.ponerElementoEn(self.fabricarOeste(),self.fabricarPared())
        armario.ponerElementoEn(self.fabricarSur(),p1)

        padre.agregarHijo(armario)
        return armario

    def fabricarBombaEn(self,padre):
        bomba = self.fabricarBomba()
        padre.agregarHijo(bomba)
    
    def fabricarMadera(self):
        return Madera()
    
    def fabricarMetal(self):
        return Metal()
    
    def fabricarDiamante(self):
        return Diamante()
    
    def fabricarEspadaEn(self,padre,num,material):
        espada = Espada()
        espada.num = num
        if material=="madera":
            espada.material = self.fabricarMadera()
        if material=="metal":
            espada.material = self.fabricarMetal()
        if material=="diamante":
            espada.material = self.fabricarDiamante()
        padre.agregarHijo(espada)
        com = Coger()
        espada.agregarComando(com)
        return espada

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

    def fabricarCoger(self):
        return Coger()
    
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

    def fabricarBananaEn(self,padre,num):
        padre.agregarHijo(self.fabricarBanana(num))

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