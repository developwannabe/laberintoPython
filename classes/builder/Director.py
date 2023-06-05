from classes.builder.LaberintoBuilder import LaberintoBuilder
from classes.builder.LaberintoRomboBuilder import LaberintoRomboBuilder
import json

class Director():
    
    def __init__(self):
        self.builder = None
        self.dicc = None
        self.forma = None

    def procesar(self,unArchivo):
        self.leerConfig(unArchivo)
        self.iniBuilder()
        self.crearLaberinto()
        self.crearJuego()
        self.crearBichos()

    def obtenerJuego(self):
        return self.builder.obtenerJuego()

    def leerConfig(self,unArchivo):
        with open(unArchivo, 'r', encoding='utf8') as file:
            self.dicc = json.load(file)

    def iniBuilder(self):
        if self.dicc['forma'] == "cuadrado":
            self.forma = "Cuadrado"
            self.builder = LaberintoBuilder()
        if self.dicc['forma'] == "rombo":
            self.forma = "Rombo"
            self.builder = LaberintoRomboBuilder()

    def crearLaberinto(self):
        self.builder.fabricarLaberinto()
        for lab in self.dicc['laberinto']:
            self.crearLaberintoRecursivo(lab,'root')

        for puerta in self.dicc['puertas']:
            self.builder.fabricarPuertaL(puerta[0],puerta[1],puerta[2],puerta[3])

    def crearLaberintoRecursivo(self,unDic,padre):
        #Contenedores
        if unDic['tipo'] == 'habitacion':
            pad = self.builder.fabricarHabitacion(unDic['num'])
        if unDic['tipo'] == 'armario':
            pad = self.builder.fabricarArmarioEn(padre,unDic['num'])
        #Hojas
        if unDic['tipo'] == 'bomba':
            pad = self.builder.fabricarBombaEn(padre,unDic['num'])
        if unDic['tipo'] == 'tunel':
            pad = self.builder.fabricarTunelEn(padre)

        #Objetos
        if unDic['tipo'] == 'banana':
            pad = self.builder.fabricarBananaEn(padre,unDic['num'])
        if unDic['tipo'] == 'espada':
            pad = self.builder.fabricarEspadaEn(padre,unDic['num'],unDic['material'])
        if unDic['tipo'] == 'escudo':
            pad = self.builder.fabricarEscudoEn(padre,unDic['num'])
        
        #Hijos
        hijos = unDic.get('hijos',[])
        for hijo in hijos:
            self.crearLaberintoRecursivo(hijo,pad)


    def crearJuego(self):
        self.builder.fabricarJuego()

    def crearBichos(self):
        bichos = self.dicc.get('bichos',[])
        for bicho in bichos:
            self.builder.fabricarBichoL(bicho['modo'],bicho['posicion'])