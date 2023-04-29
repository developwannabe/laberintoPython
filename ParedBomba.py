from Pared import Pared

class ParedBomba(Pared):

    def __init__(self):
        super().__init__()
        self.activa = True

    def entrar(self):
        if self.activa:
            print("La bomba ha explotado.")
            self.activa = False
        else:
            print("Te has chocado con una pared.")