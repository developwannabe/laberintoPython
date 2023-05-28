from LaberintoBuilder import LaberintoBuilder
import json

class Director():
    
    def __init__(self):
        self.builder = None
        self.dicc = None

    def procesar(self,unArchivo):
        self.leerConfig(unArchivo)
        self.iniBuilder()
        self.crearLaberinto()
        self.crearJuego()
        self.crearBichos()

    def leerConfig(self,unArchivo):
        with open(unArchivo, 'r', encoding='utf8') as file:
            self.dicc = json.load(file)

    def iniBuilder(self):
        if self.dicc['forma'] == "cuadrado":
            self.builder = LaberintoBuilder()

    def crearLaberinto(self):
        self.builder.fabricarLaberinto()
        for lab in self.dicc['laberinto']:
            self.crearLaberintoRecursivo(lab)

    def crearLaberintoRecursivo(self,unDic,padre):
        if unDic['tipo'] == 'habitacion':
            pad = self.builder.fabricarHabitacion(unDic['num'])

    def crearJuego(self):
        pass

    def crearBichos(self):
        pass