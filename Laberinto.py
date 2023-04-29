
class Laberinto():

    def __init__(self):
        self.habitaciones = {}

    def agregarHabitacion(self,habitacion):
        self.habitaciones[habitacion.num] = habitacion

    def obtenerHabitacion(self,num):
        return self.habitaciones[num]
    
    def recorrer(self, funcion):
        funcion(self.habitaciones.values())
    
    def __str__(self):
        strdev = "Contenido del laberinto:\n"
        habs = self.habitaciones.values()
        for hab in habs:
            strdev = strdev + str(hab)
            strdev = strdev + "\n"
        return strdev

    def __repr__(self):
        strdev = "Contenido del laberinto:\n"
        habs = self.habitaciones.values()
        for hab in habs:
            strdev = strdev + str(hab)
            strdev = strdev + "\n"
        return strdev