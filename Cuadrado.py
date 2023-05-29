from Forma import Forma

class Cuadrado(Forma):

    def __init__(self):
        super().__init__()

        self.norte = None
        self.este = None
        self.oeste = None
        self.sur = None

    def __str__(self):
        return "\n   -Norte: " + str(self.norte) +"\n   -Este: " + str(self.este) +"\n   -Oeste: " + str(self.oeste) +"\n   -Sur: " + str(self.sur)
    
    def __repr__(self):
        return "\n   -Norte: " + str(self.norte) +"\n   -Este: " + str(self.este) +"\n   -Oeste: " + str(self.oeste) +"\n   -Sur: " + str(self.sur)