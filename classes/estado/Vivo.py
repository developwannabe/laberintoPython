from classes.estado.Estado import Estado

class Vivo(Estado):
    __instancia = None

    def actua(self,unBicho):
        unBicho.puedeActuar()

    def enteEsAtacadoPor(self,atacado,atacante):
        atacado.puedeSerAtacadoPor(atacante)

    def estaVivo(self):
        return True
    
    def __str__(self):
        return "Vivo"
    
    def __repr__(self):
        return "Vivo"