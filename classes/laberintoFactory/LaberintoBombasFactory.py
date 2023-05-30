from classes.laberintoFactory.LaberintoFactory import LaberintoFactory
from classes.elementoMapa.pared.ParedBomba import ParedBomba

class LaberintoBombasFactory(LaberintoFactory):

    def fabricarPared(self):
        return ParedBomba()