from ElementoMapa import ElementoMapa
from Contenedor import Contenedor

class Habitacion(Contenedor):

    def entrar(self):
        print("Estás en la habitación ",self.num,".")

    def esHabitacion(self):
        return True

    def __str__(self):
        ret= "Habitación: " + str(self.num) +"\n   -Norte: " + str(self.norte) +"\n   -Este: " + str(self.este) +"\n   -Oeste: " + str(self.oeste) +"\n   -Sur: " + str(self.sur)
        if len(self.hijos) > 0:
            ret = ret + "\n   -Hijos:"
            for i in self.hijos:
                ret = ret + "\n      -" + str(i)
        return ret
    
    def __repr__(self):
        ret= "Habitación: " + str(self.num) +"\n   -Norte: " + str(self.norte) +"\n   -Este: " + str(self.este) +"\n   -Oeste: " + str(self.oeste) +"\n   -Sur: " + str(self.sur)
        if len(self.hijos) > 0:
            ret = ret + "\n   -Hijos:"
            for i in self.hijos:
                ret = ret + "\n      -" + str(i)
        return ret