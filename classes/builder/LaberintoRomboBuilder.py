from classes.forma.Rombo import Rombo
from classes.builder.LaberintoBuilder import LaberintoBuilder
from classes.elementoMapa.contenedor.habitacion.Habitacion import Habitacion
from classes.orientacion.Noreste import Noreste
from classes.orientacion.Noroeste import Noroeste
from classes.orientacion.Sureste import Sureste
from classes.orientacion.Suroeste import Suroeste
from classes.comando.Abrir import Abrir

class LaberintoRomboBuilder(LaberintoBuilder):
    
    def fabricarForma(self):
        return Rombo()
    
    def fabricarNoreste(self):
        return Noreste.obtenerInstancia()
    
    def fabricarNoroeste(self):
        return Noroeste.obtenerInstancia()
    
    def fabricarSureste(self):
        return Sureste.obtenerInstancia()
    
    def fabricarSuroeste(self):
        return Suroeste.obtenerInstancia()
    
    def fabricarHabitacion(self,num):
        hab = Habitacion(num)

        forma = self.fabricarForma()
        forma.num= num
        hab.forma = forma

        hab.ponerElementoEn(self.fabricarNoreste(),self.fabricarPared())
        hab.ponerElementoEn(self.fabricarNoroeste(),self.fabricarPared())
        hab.ponerElementoEn(self.fabricarSureste(),self.fabricarPared())
        hab.ponerElementoEn(self.fabricarSuroeste(),self.fabricarPared())

        hab.agregarOrientacion(self.fabricarNoreste())
        hab.agregarOrientacion(self.fabricarNoroeste())
        hab.agregarOrientacion(self.fabricarSureste())
        hab.agregarOrientacion(self.fabricarSuroeste())

        self.laberinto.agregarHabitacion(hab)

        return hab
    
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

        armario.agregarOrientacion(self.fabricarNoreste())
        armario.agregarOrientacion(self.fabricarNoroeste())
        armario.agregarOrientacion(self.fabricarSureste())
        armario.agregarOrientacion(self.fabricarSuroeste())

        armario.ponerElementoEn(self.fabricarNoreste(),self.fabricarPared())
        armario.ponerElementoEn(self.fabricarNoroeste(),self.fabricarPared())
        armario.ponerElementoEn(self.fabricarSureste(),self.fabricarPared())
        armario.ponerElementoEn(self.fabricarSuroeste(),p1)

        padre.agregarHijo(armario)
        return armario