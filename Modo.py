import time
from abc import ABC, abstractmethod

class Modo():
    
    def actua(self,unBicho):
        self.dormir()
        self.caminar(unBicho)
        self.atacar(unBicho)

    def dormir(self):
        print('Bicho duerme')
        time.sleep(2)

    def caminar(self,unBicho):
        ori = unBicho.obtenerOrientacionAleatoria()
        unBicho.irA(ori)

    @abstractmethod
    def atacar(self,unBicho):
        pass

    def esAgresivo(self):
        return False
    
    def esPerezoso(self):
        return False
