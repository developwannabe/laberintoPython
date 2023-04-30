
class Laberinto():

    def __init__(self):
        self.habitaciones = {}

    def agregarHabitacion(self,habitacion):
        self.habitaciones[habitacion.num] = habitacion

    def obtenerHabitacion(self,num):
        return self.habitaciones[num]
    
    def recorrer(self, funcion):
        for habi in list(self.habitaciones.values()):
            habi.recorrer(funcion)
    
    def __str__(self):
        strdev = "Contenido del laberinto:\n"
        habs = self.habitaciones.values()
        for hab in habs:
            strdev = strdev + str(hab)
            strdev = strdev + "\n\n"
        return strdev

    def __repr__(self):
        strdev = "Contenido del laberinto:\n"
        habs = self.habitaciones.values()
        for hab in habs:
            strdev = strdev + str(hab)
            strdev = strdev + "\n\n"
        return strdev