from Hoja import Hoja

class Bomba (Hoja):

    def __init__(self):
        super().__init__()
        self.activa = True

    def esBomba(self):
        return True
    