from classes.estado.Estado import Estado

class Abierta(Estado):
    
    def abrir(self,unaPuerta):
        print("La puerta ya está abierta.")

    def estaAbierta(self):
        return True
    
    def esAbierta(self):
        return True
    
    def __str__(self):
        return "Abierta"
    
    def __repr__(self):
        return "Abierta"
