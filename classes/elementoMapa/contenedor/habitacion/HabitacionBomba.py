from classes.elementoMapa.contenedor.habitacion.Habitacion import Habitacion

class HabitacionBomba(Habitacion):

    def __init__(self,num):
        super().__init__()
        self.activa = True
        self.num = num

    def entrar(self):
        if self.activa:
            print("La bomba ha explotado.")
            self.activa = False
        else:
            print("Estás en la habitación ",self.num)