from ElementoMapa import ElementoMapa
from Contenedor import Contenedor

class Habitacion(Contenedor):

    def entrar(self):
        print("Estás en la habitación ",self.num,".")

    def esHabitacion(self):
        return True

    def __str__(self):
        return "Habitación: " + str(self.num) +"\n   -Norte: " + str(self.norte) +"\n   -Este: " + str(self.este) +"\n   -Oeste: " + str(self.oeste) +"\n   -Sur: " + str(self.sur)
    
    def __repr__(self):
        return "Habitación: " + str(self.num) +"\n   -Norte: " + str(self.norte) +"\n   -Este: " + str(self.este) +"\n   -Oeste: " + str(self.oeste) +"\n   -Sur: " + str(self.sur)
