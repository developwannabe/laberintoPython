from Estado import Estado

class Vivo(Estado):
    __instancia = None

    def actua(self,unBicho):
        unBicho.puedeActuar()

    def enteEsAtacadoPor(atacado,atacante):
        pass

    def estaVivo(self):
        return True