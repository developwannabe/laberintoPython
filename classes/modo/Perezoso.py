from classes.modo.Modo import Modo
import time

class Perezoso(Modo):
    
    def atacar(self,unBicho):
        unBicho.atacar()
        unBicho.cambiarModo()
    
    def dormir(self):
        time.sleep(4)
    
    def esPerezoso(self):
        return True
    
    def __str__(self):
        return "-Perezoso:"
    
    def __repr__(self):
        return "-Perezoso:"