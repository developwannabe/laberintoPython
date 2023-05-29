from Estado import Estado

class Muerto(Estado):
    
    def actua(unBicho):
        print(str(unBicho),' no puede actuar, está muerto.')

    def enteEsAtacadoPor(self,atacado,atacante):
        print(str(atacante), " no puede atacar a ",str(atacado)," porque está muerto.")

    def estaVivo(self):
        return False
    
    def __str__(self):
        return "Muerto"
    
    def __repr__(self):
        return "Muerto"
