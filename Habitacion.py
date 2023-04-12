from ElementoMapa import ElementoMapa

class Habitacion(ElementoMapa):

    def __init__(self,num):
        self.num = num
        self.norte = None
        self.este = None
        self.oeste = None
        self.sur = None

    def entrar(self):
        print("Estás en la habitación ",self.num,".")

    def __str__(self):
        return "Habitación: " + str(self.num) +"\n   -Norte: " + str(self.norte) +"\n   -Este: " + str(self.este) +"\n   -Oeste: " + str(self.oeste) +"\n   -Sur: " + str(self.sur)
    
    def __repr__(self):
        return "Habitación: " + str(self.num) +"\n   -Norte: " + str(self.norte) +"\n   -Este: " + str(self.este) +"\n   -Oeste: " + str(self.oeste) +"\n   -Sur: " + str(self.sur)
