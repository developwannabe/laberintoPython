from classes.ElementoMapa import ElementoMapa
from classes.Contenedor import Contenedor

class Habitacion(Contenedor):

    def entrar(self,ente):
        ente.posicion = self
        print(str(ente)," está en la habitación ",self.num,".")

    def esHabitacion(self):
        return True

    def __str__(self):
        ret= "Habitación "+str(self.num) +": "+ str(self.forma) 
        if len(self.hijos) > 0:
            ret = ret + "\n   -Hijos:"
            for i in self.hijos:
                ret = ret + "\n      -" + str(i)
        return ret
    
    def __repr__(self):
        ret= "Habitación "+str(self.num) +": "+ str(self.forma)
        if len(self.hijos) > 0:
            ret = ret + "\n   -Hijos:"
            for i in self.hijos:
                ret = ret + "\n      -" + str(i)
        return ret