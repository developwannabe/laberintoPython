from Estado import Estado

class Muerto(Estado):
    
    def actua(unBicho):
        print(str(unBicho),' no puede actuar, está muerto.')

    def enteEsAtacadoPor(atacado,atacante):
        pass

    def estaVivo(self):
        return False
