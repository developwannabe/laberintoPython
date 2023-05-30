from classes.Contenedor import Contenedor
class Laberinto(Contenedor):

    def __init__(self):
        super().__init__(0)

    def agregarHabitacion(self,habitacion):
        self.hijos.append(habitacion)

    def entrar(self,ente):
        hab1 = self.obtenerHabitacion(1)
        hab1.entrar(ente)
        print(self)

    def obtenerHabitacion(self,num):
        return self.hijos[num-1]
    
    def recorrer(self, funcion):
        for habi in self.hijos:
            habi.recorrer(funcion)
    
    def __str__(self):
        strdev = "Contenido del laberinto:\n"
        habs = self.hijos
        for hab in habs:
            strdev = strdev + str(hab)
            strdev = strdev + "\n\n"
        return strdev

    def __repr__(self):
        strdev = "Contenido del laberinto:\n"
        habs = self.hijos
        for hab in habs:
            strdev = strdev + str(hab)
            strdev = strdev + "\n\n"
        return strdev