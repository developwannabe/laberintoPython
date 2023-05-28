from Modo import Modo

class Agresivo(Modo):
    
    def atacar(self,unBicho):
        unBicho.atacar()
    
    def esAgresivo(self):
        return True
    
    def __str__(self):
        return "-Agresivo"
    
    def __repr__(self):
        return "-Agresivo"