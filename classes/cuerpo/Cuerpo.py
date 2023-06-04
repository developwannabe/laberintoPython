class Cuerpo():
    
    def __init__(self):
        self.mIzquierda = None #Escudos (Defensa)
        self.mDerecha = None #Espada (Ataque)
        self.observadoresCuerpo = []


    def obtenermIzquierda(self):
        return self.mIzquierda
    
    def obtenermDerecha(self):
        return self.mDerecha
    
    def setmIzquierda(self,obj):
        self.mIzquierda = obj
        for obs in self.observadoresCuerpo:
            obs.mostrarCuerpo()

    def setmDerecha(self,obj):
        self.mDerecha = obj
        for obs in self.observadoresCuerpo:
            obs.mostrarCuerpo()