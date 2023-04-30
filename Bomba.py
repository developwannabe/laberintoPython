from Decorator import Decorator

class Bomba (Decorator):

    def __init__(self):
        super().__init__()
        self.activa = True

    def esBomba(self):
        return True
    
    def entrar(self):
        if self.activa:
            print("La bomba ha explotado.")
            self.activa = False
        else:
            self.component.entrar()
    
    def __str__(self):
        if self.component is not None:
            return str(self.component) + " decorado con bomba."
        else:
            return "Bomba"
    
    def __repr__(self):
        if self.component is not None:
            return str(self.component) + " decorado con bomba."
        else:
            return "Bomba"