class Cuerpo():
    
    def __init__(self):
        self.mIzquierda = None #Escudos (Defensa)
        self.mDerecha = None #Espada (Ataque)
        self.observadoresCuerpo = []

    def agregarObservadoresCuerpo(self,obs):
        self.observadoresCuerpo.append(obs)

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

    def obtenerComandos(self,ente): # Implementar en consola
        comandos = []
        if self.mIzquierda is not None:
            comandos.extend(self.mIzquierda.obtenerComandos(ente))
        if self.mDerecha is not None:
            comandos.extend(self.mDerecha.obtenerComandos(ente))
        return comandos