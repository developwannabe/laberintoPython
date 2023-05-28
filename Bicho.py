from Ente import Ente

class Bicho(Ente):

    def actua(self):
        self.estado.actua(self)

    def obtenerOrientacionAleatoria(self):
        return self.posicion.obtenerOrientacionAleatoria()