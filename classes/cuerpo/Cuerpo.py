class Cuerpo():
    
    def __init__(self):
        mIzquierda = None #Escudos (Defensa)
        mDerecha = None #Espada (Ataque)
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
        self.mIzquierda = obj
        for obs in self.observadoresCuerpo:
            obs.mostrarCuerpo()